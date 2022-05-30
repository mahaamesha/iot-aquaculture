/*
 Basic ESP8266 MQTT example
 This sketch demonstrates the capabilities of the pubsub library in combination
 with the ESP8266 board/library.
 It connects to an MQTT server then:
  - publishes "hello world" to the topic "outTopic" every two seconds
  - subscribes to the topic "inTopic", printing out any messages
    it receives. NB - it assumes the received payloads are strings not binary
  - If the first character of the topic "inTopic" is an 1, switch ON the ESP Led,
    else switch it off
 It will reconnect to the server if the connection is lost using a blocking
 reconnect function. See the 'mqtt_reconnect_nonblocking' example for how to
 achieve the same result without blocking the main loop.
 To install the ESP8266 board, (using Arduino 1.6.4+):
  - Add the following 3rd party board manager under "File -> Preferences -> Additional Boards Manager URLs":
       http://arduino.esp8266.com/stable/package_esp8266com_index.json
  - Open the "Tools -> Board -> Board Manager" and click install for the ESP8266"
  - Select your ESP8266 in "Tools -> Board"
*/

#include <WiFi.h>	// ESP32
//#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// ds18b20
#include <OneWire.h>
#include <DallasTemperature.h>
int TEMP_PIN = 4;	// pin D4 - GPIO4 - ADC2_0
OneWire wiring(TEMP_PIN);
DallasTemperature ds18b20(&wiring);

// pH4502c
int PH_PIN = 34;	// pin D34 - GPIO34 - ADC1_6
int samples = 10;
float adc_resolution = 1024.0;

// turbidity sensor
int TURB_PIN = 35;	// pin D35 - GPIO35 - ADC1_7

// Update these with values suitable for your network.
const char* ssid = "Wi-Fe";
const char* password = "gorill4a";
const char* mqtt_server = "test.mosquitto.org";

WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE	(50)
char msg[MSG_BUFFER_SIZE];


// Function temperature
float read_temperature() {
  ds18b20.setResolution(9);
  ds18b20.requestTemperatures();
  float dataSuhu = ds18b20.getTempCByIndex(0);
  
  return dataSuhu;
}
// (END) Function temperature


// Function pH
float read_pH() {
  int measuring = 0;

  for(int i=0;i<samples;i++){
    measuring += analogRead(PH_PIN);	// pin PH_PIN in void setup()
    delay(10);
  }

  float voltage = 5/adc_resolution*measuring/samples;
  float pH = 16.15 + ((2.5 - voltage)/0.18);
  
  return pH;
}
// (END) Function pH


// Function turbidity
float round_to_dp( float in_value, int decimal_place ) {
  float multiplier = powf( 10.0f, decimal_place );
  in_value = roundf( in_value * multiplier ) / multiplier;
  return in_value;
}

float read_turbidity() {
  float volt = 0;
  float ntu = 0;
  
  for(int i=0; i<800; i++) {
    volt += ((float)analogRead(TURB_PIN)/1023)*5;
  }
  volt = volt/800;
  volt = round_to_dp(volt,2);
  if(volt < 2.5) {
	ntu = 3000;
  } else {
	ntu = -1120.4 * volt*volt + 5742.3 * volt - 4352.9; 
  }
  
  return ntu;
}
// (END) Function turbidity

// Function MQTT
void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is active low on the ESP-01)
  } else {
    digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP32Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("ourSensorOut", "Hello World !!!");
      // ... and resubscribe
      client.subscribe("ourSensorOut"); //only for checking that the message has been received
      client.subscribe("ourSensorIn");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
// Function MQTT


void setup() {
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  // ph4502c
  pinMode(PH_PIN, INPUT);
}

void loop() {  
  // MQTT
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  unsigned long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;

	float temperature = read_temperature();
	float pH = read_pH();
	float turbidity = read_turbidity();

	String message = String(temperature) + "," + String(pH) + "," + String(turbidity);
    client.publish("ourSensorOut", message.c_str());
  }
  // (END) MQTT
}
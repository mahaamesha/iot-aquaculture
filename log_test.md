# Testing
by @mahaamesha

<br>

## Table of Contents

- [About](#about)
- [Note](#note)
    - [0419](#0419)
    - [0429_01](#0429_01)

<br>

## About <a name = "about"></a>

Log activity of testing.

[`19-Apr-22`](test/0419/)       Test DHT11 to read temperature, humidity \
[`29-Apr-22`](test/0429_01/)    Test MQTT using HiveMQCloud \
[`29-Apr-22`](test/0429_02/)    Test nodered to receive message from ESP8266 via MQTT \
[`07-Mei-22`](test/0507_01/)    Make `camera.py` to take picture with pizero camera \
[`07-Mei-22`](test/0507_02/)    Make loop to run `main.py` from `fish-length-opencv` for every image captured \


<br>

## To Do <a name = "todo"></a>
- [ ] Make `program.ino` to send data from ESP8266 via MQTT
- [ ] Initalize database in server raspi
- [ ] Make flows in `Nodered` to receive message from MQTT
- [ ] Make function to filter `msg.payloads`, then extract each measurements
- [ ] Make flows to upload each measurements into InfluxDB
- [ ] Connect Grafana with InfluxDB
- [ ] Create dashboard, then create panel for every measurements

- [ ] Integrate `main.py` from `fish-length-opencv` repository with Nodered

<br>

## Note <a name = "note"></a>

### Test DHT11 <a name = "0419"></a>
- Use library DHT11, modifiy `DHTTester.ino` from example

### Test MQTT using HiveMQCloud <a name = "0429_01"></a>
I try to secure data that I send via MQTT.
- Access this [HiveMQCloud-Clusters](https://console.hivemq.cloud/clusters/)
- Follow the instruction in GETTING STARTED for ESP8266 in this [link](https://console.hivemq.cloud/clients/arduino-esp8266?uuid=fb39fa06a52049ecac3a88801077b1b7).

<br>
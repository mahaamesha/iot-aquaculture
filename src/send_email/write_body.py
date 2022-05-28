import os
import json
import sys


# Replace value in send_email/data_email.json based on tmp/data.json
def send_datajson_to_dataemailjson():
    working_path = os.path.dirname(__file__)
    
    path1 = os.path.join(working_path, '../../tmp/data.json')
    with open(path1, 'r') as f1:
        data1 = json.load(f1)

        path2 = os.path.join(working_path, 'data_email.json')
        with open(path2, 'r') as f2:
            data2 = json.load(f2)

            # From tmp/data.json
            for key1 in data1.keys():
                for key2 in data2.keys():
                    if key1 == key2:
                        data2[key2] = data1[key2]['value']
                
    with open(path2, 'w') as f:
        json.dump(data2, f, indent=4)


# Save parameter value in send_email/data_email.json into new variable
def save_dataemailjson_to_variable(dict_param):
    working_path = os.path.dirname(__file__)
    path = os.path.join(working_path, 'data_email.json')
    with open(path, 'r') as f:
        data = json.load(f)
        for key in data.keys():
            dict_param.update( {key: data[key]} )
    
    return dict_param


# Get msg.payload from nodered, then replace value of num_fish & fishlength in dict_param
def save_msgpayload_to_variable(dict_param):
    str_payload = sys.argv[1]
    obj = json.loads(str_payload)

    for key in obj.keys():
        dict_param[key] = obj[key]
    
    return dict_param



# Use dict_param, then use it in template, return body_html as a string
def template(dict_param):
    p = dict_param

    body = """\
    <!DOCTYPE html>
    <html>
        <body>
            <h1>IoT Aquaculture Report</h1>
            
            <p>
                Below is the result: <br/>
                <table>
                    <tr>
                        <th>Parameter</th>
                        <th>Value</th>
                    </tr>
                    <tr>
                        <td>Temperature (&deg;C)</td>
                        <td>%s</td>
                    </tr>
                    <tr>
                        <td>pH</td>
                        <td>%s</td>
                    </tr>
                    <tr>
                        <td>Turbidity (NTU)</td>
                        <td>%s</td>
                    </tr>
                    <tr>
                        <td>Number of fish</td>
                        <td>%s</td>
                    </tr>
                    <tr>
                        <td>Average fish length (mm)</td>
                        <td>%s</td>
                    </tr>
                </table>
            </p>
        </body>
    </html>
    """ %(p['temperature'], p['pH'], p['turbidity'], p['num_fish'], p['fishlength'])

    return body


# Overwrite send_email/body.html from string body_html
def make_body_html(body_html=None):
    working_path = os.path.dirname(__file__)
    path = os.path.join(working_path, 'body.html')
    with open(path, 'w'):
        pass
    with open(path, 'w') as f:
        f.write(body_html)


if __name__ == '__main__':
    # Replace value in send_email/data_email.json based on tmp/data.json
    send_datajson_to_dataemailjson()
    
    param = {}
    # Save parameter value in send_email/data_email.json into new variable
    param = save_dataemailjson_to_variable(dict_param=param)
    # Get msg.payload from nodered, then replace value of num_fish & fishlength in dict_param
    param = save_msgpayload_to_variable(dict_param=param)

    # Use dict_param, then use it in template, return body_html as a string
    body = template(dict_param=param)

    # Overwrite send_email/body.html from string body_html
    make_body_html(body_html=body)
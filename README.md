# iot-aquaculture
by @mahaamesha, @AldianNurAzmar, @kemalrizky

<br/>

## Contents <a name = 'contents'></a>
- [About](#about)
- [Note](#note)
- [Usage](#usage)
- [Flow](#flow)

<br/>


## About <a name = 'about'></a>
This is an iot project in fishery field.
The main purposes of this projetc are:
- Monitoring water quality
- Monitoring average length of fish

> For the second purposes, I build the system program as independent project which can be accessed in [`fish-length-opencv`](https://github.com/mahaamesha/fish-length-opencv) repository.

Block diagram: \
<img width="70%" src="https://raw.githubusercontent.com/mahaamesha/iot-aquaculture/master/img/blockDiagram.png">

Important to be known about **SNI** standard water quality in catfish fishery.
| Parameter | Value |
| :- | :- |
| Temperature (&deg;C) | 25 - 30 |
| pH | 6.5 - 8.0 |
| Turbidity (NTU) | 0 - 50 |

<br/>
<br/>

## Note <a name = 'note'></a>
Note here.

<br/>
<br/>

## Usage <a name = 'usage'></a>
- Dont forget to change `isTest` state into `False` in [camera.py](src\camera.py) & [send_email.py](src\send_email\send_email.py)
    
    ```python
    # In send_email.py
    if __name__ == '__main__':
        print('Sending email ...')
        main(isTest=False)

    # In camera.py
    if __name__ == '__main__':
        print('Run camera.py ... ', end='')
        main(isTest=False)
    ```

- Tips:\
    Remove old folder
    ```
    rm -rf fish-length-opencv/ iot-aquaculture/
    ```
    
    Clone projects from GitHub repository
    ```
    git clone https://github.com/mahaamesha/fish-length-opencv.git && git clone https://github.com/mahaamesha/iot-aquaculture.git
    ```


<br/>
<br/>

## Flow <a name = 'flow'></a>
This is the flow which I have build using `Node-Red` for interconect.
- The main flow\
    Later, I will change the injection time. For example call the `sub2` everyday at 09.00 WIB.\
    <img width="70%" src="https://raw.githubusercontent.com/mahaamesha/iot-aquaculture/master/img/flow.jpg">

- Subflow: sub1\
    <img width="70%" src="https://raw.githubusercontent.com/mahaamesha/iot-aquaculture/master/img/sub1.jpg">

- Subflow: sub2\
    <img width="70%" src="https://raw.githubusercontent.com/mahaamesha/iot-aquaculture/master/img/sub2.1.jpg">
    <img width="70%" src="https://raw.githubusercontent.com/mahaamesha/iot-aquaculture/master/img/sub2.2.jpg">
    <img width="70%" src="https://raw.githubusercontent.com/mahaamesha/iot-aquaculture/master/img/sub2.3.jpg">

- Subflow: sub3\
    <img width="70%" src="https://raw.githubusercontent.com/mahaamesha/iot-aquaculture/master/img/sub3.jpg">

<br/>
<br/>


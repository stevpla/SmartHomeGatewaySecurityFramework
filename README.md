# SmartHomeGatewaySecurityFramework
openHAB authorization and authentication scheme delegating user's roles and allowing different access levels on Things. OAuth2.0 service and JWT (Json Web Token) are used as well as a python Proxy server for our proposed scenario. OAuth service is implemented by [ControlThings Server](https://as.controlthings.gr/) , an open source authorization server responsible for json web tokens generation. [Python Proxy Server](https://github.com/mmlab-aueb/identity-authentication-authorization) and [ControlThings Server](https://as.controlthings.gr/) are implemented and supported by [Nikos Fotiou](https://github.com/nikosft) (Researcher at AUEB). In case of any questions about ControlThings or/and IAA Python Proxy Server may contact with Nikos Fotiou.

## Proposed System Architecture

<img src="system.png" >

## Prerequisites

Tools and software you need to deploy project successfully. 
### Linux environment for Application
* **Operating System**<br>
The project has been build upon Ubuntu 20.04.01 LTS
* **Python v3.8**<br>
Python 3.7 or > v3.0 should be fine!
* **IDE**<br>
PyCharm 2020.2.1 (Community Edition)<br>
[Alternatively, any other IDE you want]
### Linux enivornment for openHAB Gateway
* **openHAB Gateway Setup**<br>
Install [openHAB software](https://www.openhab.org/docs/installation/linux.html#installation) for linux and configure this machine as Gateway. A good option is [rasberry pi 3 model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) as a machine.
### IAA Python Proxy Server
* **Proxy Server Setup**<br>
Install proxy server on a seperate machine as system image depicted. More details about the essential libaries and python version can be found at this Github [repository](https://github.com/mmlab-aueb/identity-authentication-authorization) by [Nikos Fotiou](https://github.com/nikosft).
### ControlThings as an authorization OAuth2.0 server
[ControlThings](https://as.controlthings.gr/) is a web-authorization server which any client can access and request a json web token. Client can register http resources and create guest users and finally correlate guest with a set of resources this guest has access to.

## Deploy Project

After setting up all essential tools, first, you have to do:
```sh
$ git clone https://github.com/stevpla/SmartHomeGatewaySecurityFramework.git
```
to download project at your space. Then move into project directory with:
```sh
$ cd SmartHomeGatewaySecurityFramework/openHABAccessControl/
```
and then there are three options to run the application.

```sh
1. Console-free without having continuous output logging on the terminal (nohup use)
  $ nohup python3.8 main.py &
2. Logging output on the terminal
  $ python3.8 main.py
3. Through IDE
```
### Deploy using only 2 python scripts (access_token_request.py for steps 5, 6 and http_resource_request.py for steps 7, 10)
Instead of running main.py, you can do the 2 steps using only the 2 python scripts. Each script has its own parameters. So:
```sh
$ python3.8 access_token_request.py <client_id> <client_secret>
$ python3.8 http_resource_request.py <json_token_file_path> <MY_HTTP_URL>
```



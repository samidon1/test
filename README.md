# postman-sdwan
Postman collections for SD-WAN programmability

### Requirements
To use this application you will need:

Postman 7.20+
Python 3.7+
Cisco SD-WAN 19.2+

### Install and Setup
Clone the code to local machine.

Download and install postman from https://www.postman.com/downloads/
(version 7.20)

git clone https://github.com/rudreshveerappaji/postman-sdwan.git
cd postman-sdwan/

Setup Python Virtual Environment (requires Python 3.7+)

python3.7 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

Setup local environment variables to provide vManage instance details.

Examples:

```
(Linux)
export vmanage_host=<vmanage-ip>
export vmanage_port=<vmanage-port>
export username=<username>
export password=<password>
```
```
(Windows)
set vmanage_host=<vmanage-ip>
set vmanage_port=<vmanage-port>
set username=<username>
set password=<password>
```

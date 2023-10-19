[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/bSpPyDkw)

<h1>The Wireless WREN Watcher</h1>
<h2>CDTS Jacob Turner, Isaiah Laureano, Justin Mar, Simeon Olawale-Apanpa, Bryce Valverde</h2>
<h3>Instructor: COL Chris Morrell, Advisors: Glenn Robertson, John Muir, Evaluator: Dr Blair, Product Owner: CDT Simeon Olawale-Apanpa.
<h2>Packages</h2>
For this to work, run the following in the CMD line to install the proper libraries.:<br>
````pip install sockets````<br>
````pip install requests````<br>
````apt install network-manager-openconnect openconnect````
````sudo apt-get install network-manager-openconnect network-manager-openconnect-gnome````
  
Must connect to each SSID and VPN through networkmanager GUI so that the necessary files are generated to /etc/NetworkManager/system-connections

nmcli con
nmcli con up id WREN
nmcli con down id WREN_BYOD
nmcli con up uuid [UUID_of_VPN]
  
The goal of this sprint is to implement a python program onto a raspberry pi which monitors a wireless WREN access point IOT report wireless outages to a WREN monitor server by checking certain services for a stable connection. This will help improve troubleshooting for CIO/G6 as it provides more granular data on what specifically might be the issue on the cadet side. With the creation of this solution, these wireless WREN watching devices can be used in many different locations to paint a holistic picture of what services are running appropriately in what areas.

* Replace this README with text that includes your project name, members, and a brief description.

* Github records a log of all your activity.  It will be obvious when you have not committed anything for a long time.
* User must install the python requests and sockets module before running the client.
* must install dns.resolver package to run DNS queries.

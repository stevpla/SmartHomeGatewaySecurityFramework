#!/bin/sh

printf "Installing ufw tool on Rasbian and configurating connections..\n\n"

#Run this sh as 
# $ ./ufw_conf.sh <ProxyIP>

#Commands
#1. install ufw
sudo apt install ufw
#2. allow ssh connections from any IP
sudo ufw allow ssh #sudo ufw allow 22
#3. enable ufw
sudo ufw enable
#4. deny all connections except PROXY IP - Proxy IP as a parameter
#UFW is configured to deny all incoming connections. Generally, this simplifies the process
#of creating a secure firewall policy by requiring you
#to create rules that explicity allow specific ports and IP addresses through.
sudo ufw allow from $1 to any port 8080
#5. now see the rules
sudo ufw status verbose

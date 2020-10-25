# We want to create a script to find lab resources and be able to find where they are in the lab enviroment.
# A bit like an iDRAC opensource

# define list
ip_dict = {}
ip_list = []
network_list = []
host_ip = []
network_count = 0
# python sockets (to find current ip address or network segment you want to discover)
import os
import socket
import subprocess
import concurrent.futures

for i in range(0, 3):
    split_ip = socket.gethostbyname(socket.gethostname()).split('.')[i]
    host_ip.append(split_ip)

host_ip = ".".join(host_ip)
host_ip = host_ip + "."

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
# print(host_ip, ip)
for i in range(0, 254):
    network_list.append(host_ip + str(i))

print("Discovering devices...")

def discover(ip):

    output = subprocess.Popen(["ping.exe", ip], stdout=subprocess.PIPE).communicate()[0]
    if b'unreachable' in output:
        pass
        #print(ip, "Offline")
        #ip_dict[ip] = "Offline"
    else:
        #print(ip, "Online")
        ip_dict[ip] = "Online"
        ip_list.append(ip)


with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
    executor.map(discover, network_list)

# for each ip:
print("Number of discoverable devices: ", len(ip_list))
for key in (ip_dict):
    print(key, '->', ip_dict[key])

# incert into table to host infomation and uuid

# give list of actions against list of nodes

# - IPMI chassis LED

# - get os info

# - list lsusb to see if the device plugged in to which node

exit()

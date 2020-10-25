import os
import socket
import subprocess
import concurrent.futures
from getmac import get_mac_address
from LabNode import LabNode

# define list
ip_dict = {}
ip_list = []
mac_list = []
network_list = []
network_scan = []
host_ip = []
network_count = 0


def os_type():
    global osys
    if os.name == "nt":
        osys = "win"
    else:
        osys = "linux"



def ip_setup():
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


# print("Discovering devices...")


def discoverwin(ip):
    global network_scan
    output = subprocess.Popen(["ping.exe", ip], stdout=subprocess.PIPE).communicate()[0]
    if b'unreachable' in output:
        pass
        print(ip, "Offline")
        # ip_dict[ip] = "Offline"
    else:
        ip_dict[ip] = "Online"
        ip_list.append(ip)
        ip_mac = get_mac_address(ip=ip)
        mac_list.append(ip_mac)
        try:
            test_ip = socket.gethostbyaddr(ip)
            print(ip, "Online", ip_mac, test_ip[0])
            network_scan.append(LabNode(test_ip[0], ip_mac, ip))
        except:
            print(ip, "Online", ip_mac)
            network_scan.append(LabNode("none", ip_mac, ip))
            pass


def discoverlinux(ip):
    status, result = sp.getstatusoutput("ping -c1 -w2 " + ip)
    if status == 0:
        print("System " + ip + " is UP !")
        ip_dict[ip] = "Online"
        ip_list.append(ip)
        ip_mac = get_mac_address(ip=ip)
        mac_list.append(ip_mac)
        try:
            test_ip = socket.gethostbyaddr(ip)
            print(ip, "Online", ip_mac, test_ip[0])
            network_scan.append(LabNode(test_ip[0], ip_mac, ip))
        except:
            print(ip, "Online", ip_mac)
            network_scan.append(LabNode("none", ip_mac, ip))
            pass
    else:
        print("System " + ip + " is DOWN !")



def networkScan():
    global host_ip
    os_type()

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

    if osys == "win":
        with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
            executor.map(discoverwin, network_list)
    elif osys == "linux:":
        with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
            executor.map(discoverlinux, network_list)

    print(len(mac_list), mac_list)

    # for each ip:
    print("Number of discoverable devices: ", len(ip_list))
    for key in (ip_dict):
        print(key, '->', ip_dict[key])

    return network_scan





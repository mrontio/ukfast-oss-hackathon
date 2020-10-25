from LabNode import LabNode
import subprocess
import subprocess as sp

def ipmiPowerOn(node):
    print('Powering on %s with ipmi', node.name)

def ipmiPowerOff(node):
    print('Powering off %s with ipmi', node.name)

def ipmiPowerCycle(node):
    print('Power cycling %s with ipmi', node.name)

def ipmiBlinkLED(node, password):
    print('Sending LED blink to ipmi', node.name)
    password = input("enter password for machine %s: " %(node.name))
    status, result = sp.getstatusoutput("ipmitool -I lanplus -H {} -U root -p password {} -C 17 chassis identify".format(ip, password))
    print(status)
    print(result)



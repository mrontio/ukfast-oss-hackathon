from LabNode import LabNode
import subprocess
import subprocess as sp

def establishConnection():
    status, result = sp.getstatusoutput("ipmitool -H server-ipmi -U root -p local*99 chassis identify 1")
    print(status)
    print(result)


def ipmiPowerOn(node):
    print('Powering on %s with ipmi', node.name)

def ipmiPowerOff(node):
    print('Powering off %s with ipmi', node.name)

def ipmiPowerCycle(node):
    print('Power cycling %s with ipmi', node.name)

def ipmiBlinkLED(node):
    print('Sending LED blink to ipmi', node.name) 

establishConnection()

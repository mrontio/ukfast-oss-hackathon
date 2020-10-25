from LabNode import LabNode
import subprocess
import subprocess as sp

def establishConnection():
    status, result = sp.getstatusoutput("ipmitool -H server-ipmi -U root -p local*99 chassis identify 1")
    print(status)
    print(result)


establishConnection()
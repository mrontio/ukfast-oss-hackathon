import sys
import os
from LabNode import LabNode
from LabNode import Lab
from Network import networkScan


def printLabs(labList):
        i = 1
        for lab in labList:
                print("%d: %sxo" % (i, lab.name))

def printLabTopdown(lab):
        rackRow = []
        string = ''
        for y in range(1, int(lab.height) + 1):
                rack_iterator = 0
                for x in range(0, int(lab.width)):
                         string += ('    ***************')
                         string += ('     ')
                string += '\n'

                rackList = []
                for i in range(1, int(lab.width) + 1):
                        print(i)
                        rackList.append(lab.getRack(y, i))

                for i in range(0,4):
                        for rack in rackList:
                                node = rack.getNode(i)
                                if node != None:
                                        string += '{1:2}: * {0:11} *'.format(node.name, rack.num)
                                else:
                                        string += '{0:2}: *             *'.format(rack.num)
                                string += '     '
                        string += '\n'


                for x in range(0, int(lab.width)):
                        string += '    ***************'
                        string += '     '
                string = string + '\n'


        print(string)
                
def printHelpLab():
        print('v    view rack')
        print('h    view help')
        print('q    quit')

def printHelpRack():
        print('v    view rack details')
        print('h    view help')
        print('i    set ipmi address')
        print('p    send poweron ipmi to machine')
        print('o    send poweroff ipmi to machine')
        print('r    send reboot ipmi to machine')
        print('b    blink ID LED of machine')
        print('q    quit rack view')

def printMachineDetails(node):
        print('Name: %s\nIP: %s\nMAC: %s\nIPMI IP: %s\nDescription: %s\n' % (node.name, node.ip_addr, node.ip_addr, node.ipmi_addr, node.desc))
        
def createRackView(num, lab):
        rack = lab.getRackByNum(num)
        print('*--------------------------------------------*')
        i = 0
        for node in rack.nodeList:
                print('%2d: * %10s: %10s, %10s  *' % (i, node.name, node.ip_addr, node.mac_addr))
                i += 1
        print('*--------------------------------------------*')
        finished = False
        while not finished :
                option = input('> ')
                if (option == '') or (option == 'h'):
                        printHelpRack()
                elif (option == 'v'):
                        machid = int(input('Which machine? '))
                        printMachineDetails(rack.getNode(machid))
                elif (option == 'i'):
                        machid = int(input('Which machine? '))
                        ipmi_addr = input('Please provide the IPMI address: ')
                        rack.getNode(machid).setIPMIAddr(ipmi_addr)
                elif (option == 'p'):
                        machid = int(input('Which machine? '))
                        ipmiPowerOn(rack.getNode(machid))
                        print('IPMI Signal sent')
                elif (option == 'p'):
                        machid = int(input('Which machine? '))
                        ipmiPowerOff(rack.getNode(machid))
                        print('IPMI Signal sent')
                elif (option == 'r'):
                        machid = int(input('Which machine? '))
                        ipmiReboot(rack.getNode(machid))
                        print('IPMI Signal sent')
                elif (option == 'b'):
                        machid = int(input('Which machine? '))
                        ipmiBlink(rack.getNode(machid))
                        print('IPMI Signal sent')
                
                elif (option == 'q'):
                        finished = True
                        
        
def createLabView(labList):
        printLabs(labList)
        labNum = int(input('Which lab would you like to view? '))
        lab = labList[labNum - 1]
        printLabTopdown(lab)

        finished = False
        while not finished :
                option = input('> ')                
                if (option == ''):
                        printHelpLab()
                elif (option == 'v'):
                        rackNum = int(input("Which rack? "))
                        createRackView(rackNum, lab)
                        printLabTopdown(lab)
                elif (option == 'q'):
                        finished = True

                        
def dummyNetworkScan():
        networkscan = []
        networkscan.append(LabNode('cerberos', '1::0', '172.28.108.22'))
        networkscan.append(LabNode('iris', '2::0', '172.28.108.32'))
        networkscan.append(LabNode('clx8', '2::0', '172.28.108.32'))
        return networkscan



def scanDialogue():
        return networkScan()

def chooseLab(labList):
        if labList == [] :
                print('No labs found.')
        else :
                for i in range(0, len(labList)) :
                        print('ID', i, ':', labList[i].name, ')')
                lab = input("Which lab ID? (n for new)")
                if lab != 'n':
                        return labList[i]
        print('Creating new lab.')
        name = input('Name: ')
        width = input('Rows of racks: ')
        height = input('Racks per row: ')

        lab = Lab(name, width, height)
        labList.append(lab)
        return lab



def createNode(netlist):
        i = 1
        for node in netlist :
                print('%d: %s %s %s' % (i, node.mac_addr, node.ip_addr, node.name))
                i = i + 1
        conf = int(input('Which would you like to configure? '))
        node = netlist[conf - 1]

        x = input('Which rack row? ')
        y = input('Which rack? ')
        node.setLabPosition(x, y)

        name = input('Set name? (blank for current) ')
        if name != '':
                node.name = name

        desc = input('Set description? (blank for none) ')
        if desc != '':
                node.setDesc(desc)

        return node

def configureScan(netlist, labList):
        lab = chooseLab(labList)
        finished = False
        while finished == False:
                node = createNode(netlist)
                lab.addNode(node)
                print('added %s to %s lab' % (node.name, lab.name))
                again = input('Add another? [y/N]')
                if again != 'y':
                        finished = True






def begin(labList):
        print(f'Welcome to lab explorer!')
        if labList == [] :
                doScan = input('No configuration file found, scan network? [y/N]: ')
                if doScan == 'y' :
                        netlist = scanDialogue()
                        configureScan(netlist, labList)

        createLabView(labList)



        return labList









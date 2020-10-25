import sys
import os
from LabNode import LabNode
from LabNode import Lab



def printLabs(labList):
        i = 1
        for lab in labList:
                print("%d: %sxo" % (i, lab.name))

def printLabTopdown(lab):
        rackRow = []
        string = ''
        numeration = 1
        for y in range(1, int(lab.height) + 1):
                rack_iterator = 0
                for x in range(0, int(lab.width)):
                        string += ('    ***************')
                        string += ('         ')
                        numeration += 1
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
                                string += '         '
                        string += '\n'
                        

                for x in range(0, int(lab.width)):
                        string += '    ***************'
                        string += '         '
                string = string + '\n'
                        
                
        print(string)
                
                        
                
def printHelpLab():
        print('v    view rack')
        print('h    view help')
        print('l    change lab')
        print('n    create new lab')
        print('q    quit')

def createRackView(num, lab):
        rack = lab.getRackByNum(num)
        print('*----------------------------------------*')
        for node in rack.nodeList:
                print('* %10s: %10s, %10s  *' % (node.name, node.ip_addr, node.mac_addr))
        print('*----------------------------------------*')
        
        
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
                        rackNum = int(input("Which rack?"))
                        createRackView(rackNum, lab)
                elif (option == 'q'):
                        finished = True

                        
def dummyNetworkScan(begin, end, submask):
        networkscan = []
        networkscan.append(LabNode('cerberos', '1::0', '172.28.108.22'))
        networkscan.append(LabNode('iris', '2::0', '172.28.108.32'))
        networkscan.append(LabNode('clx8', '2::0', '172.28.108.32'))
        return networkscan


def scanDialogue():
        ipBegin = input('Ip range beginning [X.X.X.X]: ')
        ipEnd   = input('Ip range end [X.X.X.X]: ')
        subMask = input('Subnet mask: ')
        return dummyNetworkScan(ipBegin, ipEnd, subMask)

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
        print('Found computers:')
        for i in range(0, len(netlist)) :
                print('ID', i, ':', netlist[i].ip_addr, '=', netlist[i].mac_addr, '(', netlist[i].name, ')')

        doConf = input('Configure? [y/N]:')
        if doConf == 'y' :
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
                        
                
                      
                
        
        
        
        

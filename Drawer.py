import sys
from LabNode import LabNode
from LabNode import Lab

def createLabView(labList):
        print('doing nothing')

                        
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

        name = input('Set name? (blank for current/none) ')
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
                        lab.addNode(netlist)
                        print('added %s to %s lab' % (node.name, lab.name))
                        again = input('Add another? [y/N]')
                        if again != 'y':
                                finished = True
                        
                
                
                

def begin(labList):
        print(f'Welcome to lab explorer!')
        if labList != [] :
                createLabView(labList)
        else :
                doScan = input('No configuration file found, scan network? [y/N]: ')
                if doScan == 'y' :
                        netlist = scanDialogue()
                        configureScan(netlist, labList)


        return labList
                        
                
                      
                
        
        
        
        

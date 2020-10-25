class LabNode:
    def __init__(self, name, mac_addr, ip_addr):
        self.name = name
        self.mac_addr = mac_addr
        self.ip_addr = ip_addr
        self.labPosX = None
        self.labPosY = None

    def ipmiStatus(self):
        print('polling ipmi from machine', self.name)
        # Do IPMI magic and return
        return 'being real cool'

    def setDesc(self, desc):
        self.desc = desc

    def setLabPosition(self, x, y):
        self.labPosX = x
        self.labPosY = y

class Lab:
    def __init__(self, name, height, width):
        self.name = name
        self.nodeList = []
        self.height = height
        self.width = width

        # Initialize rack list
        for i in range(1, height*width):
            self.racks[i] = Rack()
            
        

    def addNode(self, labNode):
        self.nodeList.append(labNode)
        self.racks[(labNode.labPosY * self.width) + labNode.labPosX].addNode(labNode)

    def getNode(self, i):
        return self.nodeList[i]

    def getNodes(self):
        return self.nodeList

class Rack:
    def __init__(self, units):
        self.units = units
        self.nodeList = []

    def addNode(self, node):
        self.nodeList.append(node)
    

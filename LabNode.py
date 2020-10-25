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

    def addNode(self, labNode):
        self.nodeList.append(labNode)

    def getNode(self, i):
        return nodeList[i]

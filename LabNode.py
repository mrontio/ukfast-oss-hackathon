from json import JSONEncoder

class LabNode:
    def __init__(self, name, mac_addr, ip_addr):
        self.name = name
        self.mac_addr = mac_addr
        self.ip_addr = ip_addr;
        

    def ipmi_status(self):
        print("polling ipmi from machine", self.name)
        # Do IPMI magic and return
        return 'being real cool'

    def give_desc(self, desc):
        self.desc = desc
    
    
        

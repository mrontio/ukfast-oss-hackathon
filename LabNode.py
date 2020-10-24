class LabNode:
    name = None 
    mac_addr = None
    def __init__(self, mac_addr, name):
        self.name = name
        self.mac_addr = mac_addr

    def ipmi_status(self):
        print("polling ipmi from machine", self.name)
        # Do IPMI magic and return
        return 'being real cool'

        

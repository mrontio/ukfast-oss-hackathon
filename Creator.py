import json
from json import JSONEncoder
from LabNode import LabNode

class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

diction = {}
diction['node'] = []
diction['node'].append(Encoder().encode(LabNode('icx3', '49:49:::::00', '192.168.1.256')))
diction['node'].append(Encoder().encode(LabNode('icx4', '43:49:::::00', '193.168.1.256')))

with open('.lab_explorer_cfg.json', 'w') as jsonfile:
        json.dump(diction, jsonfile)


with open('.lab_explorer_cfg.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        print(data['node'])
        # for p in data:
        #         print(p['node'])

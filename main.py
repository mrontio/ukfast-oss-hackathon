#!/usr/bin/python

from LabNode import LabNode
from LabNode import Lab
import Creator
import Drawer

def main():
        labList = Creator.loadLabs()

        Drawer.begin(labList)

        Creator.storeLabs(labList)
                
        exit()

# if main.py is launched as main program, run main()
if __name__ == '__main__':
        main()
        
        

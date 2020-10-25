#!/usr/bin/python

from LabNode import LabNode
import Creator

def main():
        labList = Creator.loadLabs()

        # pass labList  to creator functions

        # draw with pretty ui

        Creator.storeLabs(labList)
                
        exit()

# if main.py is launched as main program, run main()
if __name__ == '__main__':
        main()
        
        

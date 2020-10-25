import pickle
import os

def storeLabs(labList):
        if labList != [] :
                with open('.lab_explorer_cfg.p', 'wb') as pfile:
                        pickle.dump(labList, pfile)
        else :
                try: 
                        os.remove('.lab_explorer_cfg.p')
                except:
                        return
        

def loadLabs():
        try :
                with open('.lab_explorer_cfg.p', 'rb') as pfile:
                        return pickle.load(pfile)
        except:
                return []


                


                





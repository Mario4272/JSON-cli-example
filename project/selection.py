#!/usr/bin/env python3

#%%
class JSONData():
    
    def getNodesFromJSON(self, selector, dict):
        nodes = []
         
        if selector.startswith('#'):
            #getIdentifiers
            pass 

        elif selector.startswith('.'):
            #getClassNames
            pass

        else:
            #getClasses
            pass
        
        #Get Compound Selectors
        if selector.count > 1:
            for selector in (selector for selector in x if not selector.startswith('#')):
            #TODO - get compound responses
        else:
            pass
        
        return nodes
    
    #TODO
    # def getClass(self, req, dict):
    #     pass
    
    # def getClassName(self, req, dict):
    #     pass
    
    # def getIdentifier(self, req, dict):
    #     pass
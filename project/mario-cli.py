#!/usr/bin/env python3
#author = "Mario Fialho"
#Cantina Coding Example

#%%
import sys
import click
import urllib, urllib.request, json
import re
import colorama
from colorama import Fore, Back, Style
import time
from pprint import pprint
import jsondatafile

#%%
jsonUrl = 'https://raw.githubusercontent.com/jdolan/quetoo/master/src/cgame/default/ui/settings/SystemViewController.json'

#%%
@click.command()

#%%
def main():
    print("Getting JSON from GitHub") 
    time.sleep(1.5)
    data_dict = jsondatafile.JSONData(jsonUrl).json_dict
    #FOR TESTING - REMOVE
    #Pretty Print JSON
    pprint(data_dict)
    
    print ('***JSON Loaded***')
    
    # Get selector     
    accepted_inputs = {'class', 'classNames', 'identifier'} #TODO #regex
    valid = True

#%%
    while valid == False:
        print (Fore.RED + 'What are you looking for...e.g. You can enter things like')
        print (Fore.GREEN + 'View Name: e.g. "StackView", or')
        print (Fore.GREEN + 'ViewType: e.g. "identifier", or')
        print (Fore.GREEN + 'Compound Selectors: e.g. CvarSelect#multisample')        
        selector = input(Fore.RED + 'Please enter a Selector:')

        # Ensure correct selector is entered    
        if selector in accepted_inputs:
            print(selector)
            print ('Good Choice! -  let me get that for you')
            break

        elif valid == False:
            # Print out an error
            print("Invalid Selector - Please use only options shown")
            time.sleep(1.5)
            # Ask for the name again (if it's incorrect, while loop starts again)
            print (Fore.RED + 'What are you looking for...e.g. You can enter things like')
            print (Fore.GREEN + '"View Name: e.g. "StackView", or')
            print (Fore.GREEN + 'ViewType: e.g. "identifier", or')
            print (Fore.GREEN + 'Compound Selectors: e.g. CvarSelect#multisample')
            selector = input(Fore.RED + 'Please enter a correct "Selector":')
            
#%%      
        if selector.count > 1: 
           dict_list = []

           #print nodes
           pprint(dict_list)

        else:
            selector = input(Fore.RED + 'Nothing can sometimes be something, but not in this case.  Please enter a correct "Selector":')
            

if __name__ == "__main__":
    main()
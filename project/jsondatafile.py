#!/usr/bin/env python3
#jsondatafile.py

import urllib, json
import urllib.request


class JSONData(object):
    
    def __init__ (self, url):
        response = urllib.request.urlopen(url)
        self.json_dict = json.loads(response.read())




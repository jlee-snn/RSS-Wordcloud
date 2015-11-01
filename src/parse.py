# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:15:30 2015

@author: chris
"""

##### This take the opencalais JSON output and attempt to parse it into data that will be used to feed the word cloud


import json
import re

with open("testarticle.txt.json") as json_file:
    data = json.load(json_file)
z = []
for key in data.keys():
    if re.search('SocialTag', key) and data[key]['importance'] == '1':
        z.append(data[key])
print z 
type(z)  
        
#print data['http://d.opencalais.com/dochash-1/de4738cd-0ed2-3753-9ddf-c334afb29248/SocialTag/1']['importance']
#print data['http://d.opencalais.com/dochash-1/de4738cd-0ed2-3753-9ddf-c334afb29248/SocialTag/2']
#print data['http://d.opencalais.com/dochash-1/de4738cd-0ed2-3753-9ddf-c334afb29248/SocialTag/3']
        
        
type(z)

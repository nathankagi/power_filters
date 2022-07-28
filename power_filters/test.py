# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:06:47 2022

@author: Nathan.Kagi
"""

import json

# Data to be written
butt = {
        'name': 'Butterworth',
        'a1': 1,
        'a2': 1,
        'b2': 1
        }

bes = {
        'name': 'Bessel',
        'a1': 0.7560,
        'a2': 0.9996,
        'b2': 0.4772
        }

crit = {
        'name': 'Critical Damping',
        'a1': 0.5098,
        'a2': 1.0197,
        'b2': 0.2599
        }

filters = {
        butt['name'] : butt,
        bes['name'] : bes,
        crit['name'] : crit
        }

    
# with open("test.json", "w") as outfile:
#     json.dump(filters, outfile)


# with open('parameters.json') as json_file:
#     data = json.load(json_file)
    
    #print(data['filters']['type']['a1'])
    
    # for i in data['filters']:
    #     print(i)
    #     print(i['type'])
    #     print(i['order'])
    
# def concatenate(**kwargs):
#     result = ""
#     # Iterating over the keys of the Python kwargs dictionary
#     key = kwargs['a']
#     print(key)
#     for arg in kwargs:
#         result += arg
#     return result

# print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
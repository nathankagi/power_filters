# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:06:47 2022

@author: Nathan.Kagi
"""

import json

# # Data to be written
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

# def TestClass:
#     def __init__(self, *args, **kwargs):
#         pass
    
#     def design_filter(self, **kwargs):
#         """
        

#         Parameters
#         ----------
#         **kwargs : TYPE
#             DESCRIPTION.

#         Returns
#         -------
#         None.

#         """
#         self._assign_params()
#         self._assign_props(kwargs)
    
# with open("test.json", "w") as outfile:
#     json.dump(filters, outfile)


# with open('parameters.json') as json_file:
#     data = json.load(json_file)
    
    #print(data['filters']['type']['a1'])
    
    # for i in data['filters']:
    #     print(i)
    #     print(i['type'])
    #     print(i['order'])
    

from filter import Filter
filt = Filter(order = 2, optimisation='bessel')
# print(filt._filter_params)
# filt.order = 2
# print(filt._filter_params)
# filt.order = 4
# print(filt._filter_params)
# print(filt._filter_props)
print(filt.design_filter(order=2, C1=20e-6, w0=20000))












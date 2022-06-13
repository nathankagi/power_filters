# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:08:49 2021

@author: Nathan.Kagi

Design of a second-order low-pass filter
"""

import math

# need to define two of the three
L1 = 0
C1 = 0
w0 = 0

# these will be defined by first parameters
Rd = 0
Cd = 0

# PT coefficients
"""
k1 = Rd * Cd
k2 = L1(C1 + Cd)
k3 = L1 * C1 * Rd * Cd
"""
k1 = 0
k2 = 0
k3 = 0

# third-order PT parameters, structure of tuple -> name, a1, a2, b2
# coef = [('Butterworth', 1, 1, 1),
#         ('Bessel', 0.7560, 0.9996, 0.4772),
#         ('Critical Damping', 0.5098, 1.0197, 0.2599)]

butt = {
        'name': 'Butterworth',
        'a1': 1,
        'a2': 1.6180,
        'b2': 1,
        'a3': 0.6180,
        'b3': 1
       }

bes = {
       'name': 'Bessel',
        'a1': 0.6656,
        'a2': 1.1402,
        'b2': 0.4128,
        'a3': 0.6216,
        'b3': 0.3245
       }

crit = {
        'name': 'Critical Damping',
        'a1': 0.3856,
        'a2': 0.7712,
        'b2': 0.1487,
        'a3': 0.7712,
        'b3': 0.1487
       }

filters = {
        'Butterworth': butt,
        'Bessel': bes,
        'Critical Damping': crit
        }

def calc_L1(C1, w0, filter_type):
    num = filters[filter_type]['a1']*filters[filter_type]['b2']
    den = C1*(w0**2)*(filters[filter_type]['a1']*filters[filter_type]['a2'])
    L1 = num/den
    return L1

def calc_C1(L1, w0, filter_type):
    num = filters[filter_type]['a1']*filters[filter_type]['b2']
    den = L1*(w0**2)*(filters[filter_type]['a1']*filters[filter_type]['a2'])
    C1 = num/den
    return C1

def calc_w0(L1, C1, filter_type, wb = 0, Gb = 0):
    if wb == 0:
        # Calculates w0 if previous design parameters C1 and L1 have been defined.
        num = filters[filter_type]['a1']*filters[filter_type]['b2']
        den = L1*C1*(filters[filter_type]['a1']*filters[filter_type]['a2'])
        w0 = math.sqrt(num/den)
    elif (wb > 0) and (abs(Gb) > 0):
        # Calculates w0 from design parameters wb (cutoff frequency) and Gb (damping at defined frequency in db)
        """
        should impliment **kwargs instead if statements, could do later 
        when building as class? Not super important at this stage
        """
        G = math.pow(10,(Gb/20))
        num = G*filters[filter_type]['a1']*filters[filter_type]['b2']
        den = filters[filter_type]['a1']*filters[filter_type]['a2']
        w0 = wb * math.sqrt(num/den)
    return w0

def calc_Cd(L1, C1, w0, filter_type):
    num = filters[filter_type]['a1']*filters[filter_type]['a2'] + filters[filter_type]['a2']
    den = L1*(w0**2)
    Cd = (num/den)-C1
    return Cd

def calc_Rd(L1, C1, Cd, w0, filter_type):
    num = filters[filter_type]['a1']+filters[filter_type]['a2']
    den = Cd*w0
    Rd = num/den
    return Rd

"""
w0 = calc_w0(L1, C1, filter_type)
C1 = calc_C1(L1, w0, filter_type)
Cd = calc_Cd(L1, C1, w0, filter_type)
Rd = calc_Rd(L1, C1, Cd, w0, filter_type)
"""



    
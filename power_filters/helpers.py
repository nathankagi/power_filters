# -*- coding: utf-8 -*-

import numpy as np


class SecondOrder:

    @property
    def C1():
        return calc_C1

    @staticmethod
    def calc_L1(C1, w0, parameters):
        num = parameters.a1*parameters.b2
        den = C1*(w0**2)*(parameters.a1*parameters.a2)
        L1 = num/den
        return L1

    @staticmethod
    def calc_C1(L1, w0, parameters):
        num = parameters.a1*parameters.b2
        den = L1*(w0**2)*(parameters.a1*parameters.a2)
        C1 = num/den
        return C1

    @staticmethod
    def calc_w0(L1, C1, parameters, wb=0, Gb=0):
        if wb == 0:
            # Calculates w0 if previous design parameters C1 and L1 have been defined.
            num = parameters.a1*parameters.b2
            den = L1*C1*(parameters.a1*parameters.a2)
            w0 = np.sqrt(num/den)
        elif (wb > 0) and (abs(Gb) > 0):
            # Calculates w0 from design parameters wb (cutoff frequency) and Gb (damping at defined frequency in db)
            G = math.pow(10, (Gb/20))
            num = G*filters[filter_type]['a1']*filters[filter_type]['b2']
            den = filters[filter_type]['a1']*filters[filter_type]['a2']
            w0 = wb * np.sqrt(num/den)
        return w0

    @staticmethod
    def calc_Cd(L1, C1, w0, parameters):
        num = filters[filter_type]['a1'] * \
            filters[filter_type]['a2'] + filters[filter_type]['a2']
        den = L1*(w0**2)
        Cd = (num/den)-C1
        return Cd

    @staticmethod
    def calc_Rd(L1, C1, Cd, w0, parameters):
        num = filters[filter_type]['a1']+filters[filter_type]['a2']
        den = Cd*w0
        Rd = num/den
        return Rd


class FourthOrder:
    def __init__(self, damping_stage: int):
        pass

    def test(self):
        pass

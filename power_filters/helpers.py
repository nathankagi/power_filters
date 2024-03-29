# -*- coding: utf-8 -*-

import numpy as np
import functools
from collections import namedtuple


class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __getattribute__(self, attr):
        obj = object.__getattribute__(self, attr)
        if hasattr(obj, '__get__'):
            return obj.__get__(self, type(self))
        return obj

    def __setattr__(self, attr, val):
        try:
            obj = object.__getattribute__(self, attr)
        except AttributeError:
            # This will be raised if we are setting the attribute for the first time
            # i.e inside `__init__` in your case.
            object.__setattr__(self, attr, val)
        else:
            if hasattr(obj, '__set__'):
                obj.__set__(self, val)
            else:
                object.__setattr__(self, attr, val)


class SecondOrder:
    @staticmethod
    def L1(properties, parameters):
        num = parameters['a1']*parameters['b2']
        den = properties['C1']*(properties['w0']**2) * \
            (parameters['a1']+parameters['a2'])
        L1 = num/den
        return L1

    @staticmethod
    def C1(properties, parameters):
        num = parameters['a1']*parameters['b2']
        den = properties['L1']*(properties['w0']**2) * \
            (parameters['a1']+parameters['a2'])
        C1 = num/den
        return C1

    @staticmethod
    def w0(properties, parameters, wb=0, Gb=0):
        if wb == 0:
            # Calculates w0 if previous design parameters C1 and L1 have been defined.
            num = parameters['a1']*parameters['b2']
            den = properties['L1']*properties['C1'] * \
                (parameters['a1']+parameters['a2'])
            w0 = np.sqrt(num/den)
        elif (wb > 0) and (abs(Gb) > 0):
            # Calculates w0 from design parameters wb (damping frequency) and Gb (damping at defined frequency in db)
            G = np.power(10, (Gb/20))
            num = G*parameters['a1']*parameters['b2']
            den = parameters['a1']*parameters['a2']
            w0 = wb * np.sqrt(num/den)
        return w0

    @staticmethod
    def Cd(properties, parameters):
        num = parameters['a1'] * parameters['a2'] + parameters['b2']
        den = properties['L1']*(properties['w0']**2)
        Cd = (num/den)-properties['C1']
        return Cd

    @staticmethod
    def Rd(properties, parameters):
        num = parameters['a1']+parameters['a2']
        den = properties['Cd']*properties['w0']
        Rd = num/den
        return Rd


class FourthOrder:
    def __init__(self, damping_stage: int):
        pass

    def test(self):
        pass

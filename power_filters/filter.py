# -*- coding: utf-8 -*-

import numpy as np
import json
from helpers import *


class Filter:
    def __init__(self, order: int, optimisation: str, damping_stage=2, **kwargs):
        self._load_params()

        self.order = order
        self.optimisation = optimisation
        self._damping_stage = damping_stage

        self._assign_params()
        self._assign_props(kwargs)

    def design_filter(self, **kwargs):
        self._assign_params()
        self._assign_props(kwargs)

    def _load_params(self):
        try:
            with open('parameters.json') as _param_file:
                self._params = json.load(_param_file)
        except:
            pass

    def _init_params(self):
        self._filter_params = {
            "a1": None,
            "a2": None,
            "b2": None,
            "a3": None,
            "b3": None
        }

    def _init_props(self):
        self._primary_props = {
            'C1': None,
            'L1': None,
            'w0': None,
            'C2': None,
            'L2': None
        }

    def _assign_params(self):
        self._init_params()
        if self.optimisation and self.order:
            for __param in self._params[self.optimisation][str(self.order)]['parameters'].keys():
                self._filter_params[__param] = self._params[self.optimisation][str(
                    self.order)]['parameters'][__param]

    def _assign_props(self, props):
        self._init_props()
        for __prop in props:
            self._primary_props[__prop] = props[__prop]

    @property
    def optimisation(self):
        if not hasattr(self, '_optimisation'):
            self._optimisation = 'critical'
        return self._optimisation

    @optimisation.setter
    def optimisation(self, optimisation):
        try:
            self._optimisation = str(optimisation)
        except ValueError:
            raise ValueError("filter optimisation must be a string") from None
        self._assign_params()

    @property
    def order(self):
        if not hasattr(self, '_order'):
            self._order = 2
        return self._order

    @order.setter
    def order(self, order):
        try:
            self._order = int(order)
        except ValueError:
            raise ValueError("order must be of type integer") from None
        self._assign_params()

    @property
    def f0(self):
        return self.w0 / (np.pi*2)

    # @f0.setter
    # def f0(self, frequency: int):
    #     if frequency > 0:
    #         self.w0 = 2 * np.pi * frequency
    #     else:
    #         raise ValueError(f'Invalid frequency value: {frequency}')

    # primary property
    @property
    def w0(self):
        return self._w0

    # @w0.setter
    # def w0(self, frequency):
    #     if frequency > 0:
    #         self._w0 = frequency
    #     else:
    #         raise ValueError(f'Invalid frequency value: {frequency}')

    # primary property
    @property
    def C1(self):
        return self._C1

    # primary property
    @property
    def L1(self):
        pass

    @property
    def Cd(self):
        pass

    @property
    def Rd(self):
        pass

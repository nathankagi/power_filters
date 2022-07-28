# -*- coding: utf-8 -*-

import numpy as np
import json
from helpers import *


class Filter:
    def __init__(self, order: int, filter: str, damping_stage=2, **kwargs):
        self.order = order
        self.filter_type = filter
        self._damping_stage = damping_stage

        self._load_params()
        self._assign_params()
        self._assign_props(kwargs)

    def design_filter(**kwargs):
        self._assign_props(kwargs)

    def _load_params(self):
        try:
            with open('parameters.json') as _param_file:
                _params = json.load(_param_file)
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
        for __param in _params[self.filter_type][self.order]['parameters'].keys():
            self._filter_params[__param] = _params[self.filter_type][self.order]['parameters'][__param]

    def _assign_props(self, props):
        self._init_props()
        for __prop in props:
            self._primary_props[__prop] = props[__prop]

    @property
    def filter_type(self):
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter):
        try:
            self._filter_type = str(filter_type)
        except ValueError:
            raise ValueError("filter type must be a string") from None

        self._assign_params()

    @property
    def order(self):
        if not self._order:
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

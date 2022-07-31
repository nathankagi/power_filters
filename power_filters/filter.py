# -*- coding: utf-8 -*-

import numpy as np
import json
import functools

from helpers import SecondOrder, FourthOrder


class Filter:
    def __init__(self, order: int, optimisation: str, damping_stage=2, *args, **kwargs):
        self._load_params()

        # class default variables
        self.__default_order = 2
        self.__default_optimisation = 'critical'
        self._elements = []

        self.order = order
        self.optimisation = optimisation
        self._damping_stage = damping_stage

        self._init_props()
        self._assign_params()

    def design_filter(self, *args, **kwargs):

        self._check_args(kwargs)

        if 'order' in kwargs:
            self.order = kwargs.pop('order')
        if 'optimisation' in kwargs:
            self.optimisation = kwargs.pop('optimisation')

        self._assign_params()

        # for __prop in self._filter_props:
        #     if self._filter_props[__prop] is None:
        #         self._filter_props[__prop] = getattr(
        #             self._filter_eqs['Class'], str(__prop))(self._filter_props, self._filter_params)

        # should return dict containing filter information
        #   - filter parameters, properties, etc.
        return None

    def _load_params(self):
        try:
            with open('parameters.json') as _param_file:
                self._params = json.load(_param_file)
        except:
            pass

    def _init_params(self):
        self._filter_params = {}

    def _init_props(self):
        self._filter_props = {}
        for __prop in self._params[str(self.order)]['elements']:
            self._filter_props[__prop] = {}
            self._filter_props[__prop]['value'] = None
            if self.order == 2:
                if hasattr(SecondOrder, __prop):
                    self._filter_props[__prop]['eq'] = getattr(
                        SecondOrder, __prop)
            elif self.order == 4:
                if hasattr(FourthOrder, __prop):
                    self._filter_props[__prop]['eq'] = getattr(
                        FourthOrder, __prop)

    def _assign_params(self):
        self._init_params()
        if self.optimisation and self.order:
            for __param in self._params[str(self.order)][self.optimisation]['parameters'].keys():
                self._filter_params[__param] = self._params[str(
                    self.order)][self.optimisation]['parameters'][__param]

    def _assign_props(self, props=None):
        self._init_props()
        if props is not None:
            for __prop in props:
                if __prop in self._filter_props:
                    self._filter_props[__prop] = props[__prop]

    def _check_args(self, kwargs):
        pass

    @property
    def optimisation(self):
        if not hasattr(self, '_optimisation'):
            self._optimisation = self.__default_optimisation
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
            self._order = self.__default_order
        return self._order

    @order.setter
    def order(self, order):
        try:
            self._order = int(order)
        except ValueError:
            raise ValueError("order must be of type integer") from None
        self._assign_params()

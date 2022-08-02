# -*- coding: utf-8 -*-

import numpy as np
import json
import functools
from collections import deque

from helpers import SecondOrder, FourthOrder, Element


class Filter(object):
    def __init__(self, order: int, optimisation: str, damping_stage=2, *args, **kwargs):
        self._load_params()

        # class default variables
        self.__default_order = 2
        self.__primary_attrs = 2
        self.__default_optimisation = 'critical'
        self._elements = deque([0]*self.__primary_attrs,
                               maxlen=self.__primary_attrs)

        self.order = order
        self.optimisation = optimisation
        self._damping_stage = damping_stage

        self._init_props()
        self._assign_params()

    def test(self):
        return self.C1

    def design_filter(self, *args, **kwargs):
        if 'order' in kwargs:
            self.order = kwargs.pop('order')
        if 'optimisation' in kwargs:
            self.optimisation = kwargs.pop('optimisation')

        self._assign_params()
        self._assign_props(kwargs)

        for __attr in kwargs:
            if __attr in list(self._filter_props.keys()):
                self._prop_setter(__attr, kwargs[__attr])

        for __prop in self._filter_props:
            if self._filter_props[__prop] not in set().union(*(d.keys() for d in list(self._elements))):
                try:
                    self._filter_props[__prop] = getattr(self._solvers(), __prop)(
                        self._filter_props, self._filter_params)
                except:
                    pass

        return self._filter_props

    # ===================
    # Attribute methods
    # "attributes" are class attributes for each of the filter elements
    # these are python @property objects
    # ===================

    # define all the properties in the helpers -> use setattr to assign attribute in SecondOrder to Filter class

    def _clear_attr(self):
        for __prop in self._params[str(self.order)]['elements']:
            try:
                delattr(self, __prop)
            except:
                # don't delete properties that dont exist
                pass

    def _init_attr(self):
        for __prop in self._params[str(self.order)]['elements']:
            try:
                setattr(self, str(__prop), self._filter_props[__prop](
                    self._filter_props, self._filter_params))
            except:
                pass
                # print(f"Failted to set attribute {__prop}")

    # ===================
    # Parameter methods
    # "parameters" are filter constants used for calculating attributes
    # ===================
    def _load_params(self):
        try:
            with open('parameters.json') as _param_file:
                self._params = json.load(_param_file)
        except:
            pass

    def _init_params(self):
        self._filter_params = {}

    def _assign_params(self):
        self._init_params()
        if self.optimisation and self.order:
            for __param in self._params[str(self.order)][self.optimisation]['parameters'].keys():
                self._filter_params[__param] = self._params[str(
                    self.order)][self.optimisation]['parameters'][__param]

    # ===================
    # Property methods
    # "properties" are the methods for calculating each of the filter elements
    # ===================
    def _init_props(self):
        self._filter_props = {}
        for __prop in self._params[str(self.order)]['elements']:
            if hasattr(self._solvers(), __prop):
                self._filter_props[__prop] = getattr(
                    self._solvers(), __prop)

    def _assign_props(self, props=None):
        self._init_props()
        if props is not None:
            for __prop in props:
                if __prop in self._filter_props and __prop in list(self._filter_props.keys()):
                    self._filter_props[__prop] = props[__prop]
                else:
                    # ignore arguments that are not valid filter elements
                    pass

    def _check_args(self, kwargs):
        pass

    # returns correct helper class which contains filter equations
    def _solvers(self):
        if self.order == 2:
            return SecondOrder
        elif self.order == 4:
            return FourthOrder

    @ property
    def optimisation(self):
        if not hasattr(self, '_optimisation'):
            self._optimisation = self.__default_optimisation
        return self._optimisation

    @ optimisation.setter
    def optimisation(self, optimisation):
        try:
            self._optimisation = str(optimisation)
        except ValueError:
            raise ValueError("filter optimisation must be a string") from None
        self._assign_params()

    @ property
    def order(self):
        if not hasattr(self, '_order'):
            self._order = self.__default_order
        return self._order

    @ order.setter
    def order(self, order):
        self._clear_attr()
        try:
            self._order = int(order)
        except ValueError:
            raise ValueError("order must be of type integer") from None
        self._assign_params()
        self._init_attr()

    @ property
    def f0(self):
        pass

    @ property
    def w0(self):
        pass

    def _prop_setter(self, attr, value):
        self._elements.appendleft({attr: value})

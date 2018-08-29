#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Last modified: 2018-08-29 18:40:54
"""This is the example module.

This module does stuff.
"""

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'lsieun'

class Building(object):
    def __init__(self, floors):
        self._floors = [None] * floors
    
    def __setitem__(self, floor_number, data):
        self._floors[floor_number] = data

    def __getitem__(self, floor_number):
        return self._floors[floor_number]


if __name__ == '__main__':
    building1 = Building(4) # Construct a building with 4 floors
    building1[0] = "Reception"
    building1[1] = "ABC Corp"
    building1[2] = "DEF Inc"
    print(building1[2])
    for company in building1:
        print(company)


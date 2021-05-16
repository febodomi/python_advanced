# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:45:33 2021

@author: Domonkos
"""

import importlib
importlib.reload(mypackage)

import mypackage

mypackage.hello('Domonkos')
mypackage.moduleA.welcome('Domonkos')


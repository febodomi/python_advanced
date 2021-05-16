# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 15:29:02 2021

@author: Domonkos
"""

import sys
  
  
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')
  
print("Exit")
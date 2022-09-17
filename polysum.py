# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:20:55 2022

@author: manish.joshi
"""

import math

sum1 = 0
perimeter1 = 0

def polysum(n,s):
    area1 = (n * (s ** 2)) / (4 * math.tan(math.pi / n))
    print('area', area1)
    perimeter1 = (n*s)
    print('perim1', perimeter1)
    sum1 = round(area1 + (perimeter1**2),4)
    return sum1 
 
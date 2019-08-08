# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:09:23 2019

@author: Deepika
"""
import math
def solution(A, B):
    # write your code in Python 3.6
    ra = int(math.sqrt(A))
    rb = int(math.sqrt(B))
    my_list = list(range(ra,rb+1))
    my_list = [x**2 for x in my_list]
    count = 0
    while True:
      my_list = [math.sqrt(x) for x in my_list]
      my_list = list(filter(lambda x: x.is_integer() and x>=2, my_list))
      if not my_list:
        break
      count = count + 1
    return count
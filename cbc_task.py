# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:37:46 2019

@author: Deepika
"""
def solution(A):
    # write your code in Python 3.6
    # Remove negative integers
    A = list(filter(lambda x: x>0, A))
    # If empty after removing
    if not A:
      ans = 1
    else:
      # Get the max element
      max_ele = max(A)
      # Create the list within that range to compare
      compare = list(range(1, max_ele+1))
      # See if all the elements present already in A
      missing = list(filter(lambda x: x not in A, compare))
      # If all <=max already present
      if not missing:
        ans = max_ele + 1
      else:
        # Sort the missing elements and take the 1st one as smallest positive integer
        ans = sorted(missing)[0]
    return ans
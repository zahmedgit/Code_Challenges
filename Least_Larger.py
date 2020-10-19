#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

Given an array of numbers and an index, return the index of the least number larger than the element at the given index, or -1 
if there is no such index ( or, where applicable, Nothing or a similarly empty value ).

Notes
Multiple correct answers may be possible. In this case, return any one of them.
The given index will be inside the given array.
The given array will, therefore, never be empty.

Example
least_larger( [4, 1, 3, 5, 6], 0 )  ->  3
least_larger( [4, 1, 3, 5, 6], 4 )  -> -1


"""


def least_larger(a, i): 
    ans=-1
    for n in range(len(a)):
        if ans==-1:
            if a[n]>a[i]:
                ans=n
        else:
            if a[n]> a[i] and a[n]<a[ans]:
                ans=n
    return ans
    


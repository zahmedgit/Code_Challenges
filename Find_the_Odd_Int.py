#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

"""


def find_it(seq):
    counts={}
    if len(seq)==1:
        return seq[0]
    for num in seq:
        if num in counts:
            counts[num]+=1
        else:
            counts[num]=1
    for num,count in counts.items():
        if count%2==1:
            return num


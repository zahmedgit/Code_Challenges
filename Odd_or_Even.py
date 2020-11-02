#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

Given a list of numbers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).

Example:
odd_or_even([0])          ==  "even"
odd_or_even([0, 1, 4])    ==  "odd"
odd_or_even([0, -1, -5])  ==  "even"



"""


def odd_or_even(arr):
    if arr==[]:
        return 'even'
    total=0
    for n in arr:
        total+=n
    return 'even' if total%2==0 else 'odd'
    


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]


"""


def sort_array(source_array):
    
    if source_array==[]:
        return []
    odds=sorted([x for x in source_array if x%2==1])
    if odds==[]:
        return source_array
    n=0
    for i in range(len(source_array)):
        if source_array[i]%2==1:
            source_array[i]=odds[n]
            n+=1
    return source_array
    


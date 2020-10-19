#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

In this kata you will be given a list consisting of unique elements except for one thing that appears twice.

Your task is to output a list of everything inbetween both occurrences of this element in the list.

Examples:
[0, 1, 2, 3, 4, 5, 6, 1, 7, 8] => [2, 3, 4, 5, 6]
['None', 'Hello', 'Example', 'hello', 'None', 'Extra'] => ['Hello', 'Example', 'hello']
[0, 0] => []
[True, False, True] => [False]
['e', 'x', 'a', 'm', 'p', 'l', 'e'] => ['x', 'a', 'm', 'p', 'l']
Notes
All elements will be the same datatype.
All used elements will be hashable.



"""


def duplicate_sandwich(arr):
    counts={}
    end=0
    for i,j in enumerate(arr):
        if j not in counts:
            counts[j]=1
        else:
            counts[j]+=1
            end=i
            break
    start=0
    while start<end:
        if arr[start]==arr[end]:
            break
        start+=1
    if end-start==1:
        return []
    return [arr[x] for x in range(start+1,end)]
    


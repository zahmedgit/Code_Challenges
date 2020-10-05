#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

There are some stones on Bob's table in a row, and each of them can be red, green or blue, indicated by the characters R, G, 
and B. Help Bob find the minimum number of stones Bob needs to remove from the table so that each pair of adjacent stones is 
unique.

Examples:

"RGBRGBRGGB"   => 1
"RGGRGBBRGRR"  => 3
"RRRRGGGGBBBB" => 9

"""


def solution(stones):
    count=0
    check=stones[0]
    for x in range(1,len(stones)):
        if stones[x]==check:
            count+=1
        else:
            check=stones[x]
    return count
    


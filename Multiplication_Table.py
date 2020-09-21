#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]

"""


def multiplication_table(size):
    arr=[]
    for x in range(1,size+1):
        arr.append([y*x for y in range(1,size+1)])  
    return arr
    


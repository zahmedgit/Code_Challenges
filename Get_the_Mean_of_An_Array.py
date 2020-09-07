#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty.

"""


def get_average(marks):
    sum=0
    for num in marks:
        sum+=num
    return int(sum/len(marks))
    


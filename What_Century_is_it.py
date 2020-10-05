#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.

Examples
"1999" --> "20th"
"2011" --> "21st"
"2154" --> "22nd"
"2259" --> "23rd"
"1124" --> "12th"
"2000" --> "20th"


"""


import math
def what_century(year):
    num=math.ceil(int(year)/100)
    if num >3 and num < 20:
        return str(num)+'th'
    elif num%10==1:
        return str(num)+'st'
    elif num%10==2:
        return str(num)+'nd'
    elif num%10==3:
        return str(num)+'rd'
    else:
        return str(num)+'th'
    


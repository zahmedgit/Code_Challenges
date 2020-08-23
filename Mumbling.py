#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

"""

def accum(s):
    i=0
    string=[]
    for l in s:
        string.append(l.upper() + i*(l.lower()))
        i+=1
    return '-'.join(string)

# Simplified into one-liner
def accum_v2(s):
    return '-'.join((s[i].upper()+i*(s[i].lower()) for i in range(len(s))))


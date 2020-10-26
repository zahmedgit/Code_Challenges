#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.



"""


def find_short(s):
    words=s.split()
    short=len(words[0])
    for word in words:
        if len(word)<short:
            short=len(word)
    return short # short: shortest word length
    


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, 
otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False

"""


def scramble(s1, s2):
    s1_counts={}
    s2_counts={}
    for letter in s1:
        if letter in s1_counts:
            s1_counts[letter]+=1
        else:
            s1_counts[letter]=1
            
    for letter in s2:
        if letter in s2_counts:
            s2_counts[letter]+=1
        else:
            s2_counts[letter]=1
    for s in s2_counts:
        if s not in s1_counts or s2_counts[s]>s1_counts[s]:
            return False
    return True
    


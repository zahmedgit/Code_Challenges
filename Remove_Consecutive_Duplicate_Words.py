#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

Your task is to remove all consecutive duplicate words from string, leaving only first words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta alpha beta gamma delta'



"""


def remove_consecutive_duplicates(s):
    if s=='':
        return ''
    words=s.split()
    after=[words[0]]
    for word in words[1:]:
        if after[-1]!=word:
            after.append(word)
    return ' '.join(after)
    


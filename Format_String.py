#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

"""


def namelist(names):
    res = []
    if len(names)==0:
        return ''
    if len(names) == 1:
        return names[0]['name']
    if len(names)==2:
        return str(names[0]['name']+' & '+names[1]['name'])
    for name in names[0:-1]:
        res.append(name['name'])
    comma = ', '.join(res)
    return str(comma+' & '+names[-1]['name'])


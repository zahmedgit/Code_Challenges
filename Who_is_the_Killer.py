#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

Some people have been killed!
You have managed to narrow the suspects down to just a few. Luckily, you know every person who those suspects have seen on the 
day of the murders.

Task.
Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:

{'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}
and also a list of the names of the dead people:

['Lucas', 'Bill']
return the name of the one killer, in our case 'James' because he is the only person that saw both 'Lucas' and 'Bill'



"""


def killer(suspect_info, dead):
    for suspect in suspect_info:
        count=0
        for p in dead:
            if p in suspect_info[suspect]:
                count+=1
        if count==len(dead):
            return suspect
    return ''
    


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false


"""


import re
def validate_pin(pin):
    if len(pin)!=4 and len(pin)!=6:
        return False
    if re.search(r'^\d{4}$',pin) or re.search(r'^\d{6}$',pin):
        return True
    return False
    


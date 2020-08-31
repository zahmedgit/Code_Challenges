#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

"""


def valid_parentheses(string):
    parens = []
    for char in string:
        if char == '(':
            parens.append(char)
        elif char == ')':
            if len(parens) > 0:
                parens.pop()
            else:
                return False
        
    return len(parens) == 0 


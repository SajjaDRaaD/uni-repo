#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def all_unique(lst):
    return len (lst) == len(set(lst))

x=[1,1,2,2,3,2,4,5,6]
y=[1,2,3,4,5]
all_unique(x) #false
all_unique(y) #true


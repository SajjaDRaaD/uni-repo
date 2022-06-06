#!/usr/bin/env python
# coding: utf-8

# In[9]:


l=[]
i = 0
while i<20:
    i+=1
    l.insert(i-1,i)
b = 0
while  b<20:
    print(l[b:b+2])
    b+=2


# In[ ]:





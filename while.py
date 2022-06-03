#!/usr/bin/env python
# coding: utf-8

# In[1]:



l=[]
i = 0
while i<50:
    i+=1
    l.insert(i-1,i)
b = 0
while  b<50:
    print(l[b:b+2])
    b+=2


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


T = (11,22,33,44)
T[0]=55   #TypeError

# In[3]:


T=(55,)+T[1:4]
T[0]  #55


# In[4]:


T   #(55, 22, 33, 44)

# In[ ]
# In[6]:


T = (11,22,33,44)
y = list(T)
y[0]=55
T = tuple(y)
T[0]   #55


# In[7]:


T  #(55, 22, 33, 44)


# In[ ]:





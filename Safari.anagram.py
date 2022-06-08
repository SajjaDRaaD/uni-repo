#!/usr/bin/env python
# coding: utf-8

# In[6]:


from collections import Counter
def anagram(first,second):
    return Counter(first) == Counter(second)

anagram("efgh5", "5gehf") #True


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import Counter
import sys

def anagram(first,second) :
    return Counter(first) == Counter(second)

str1 = "javad"
str2 = "vajad"

print(sys.getsizeof(str1))
anagram(str1,str2)


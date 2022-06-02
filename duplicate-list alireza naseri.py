#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def all_unique(list) :
    return len(list) == len(set(list))

x = [1,1,2,2,3,2,3,4,5,6]
y = [1,2,3,4,5]

# Printing iterables before conversion
print("The list before conversion is : " + str(x))
print("The list before conversion is : " + str(y))
 
# Iterables after conversion are
# notice distinct and elements
print("The list after conversion is : " + str(set(x)))
print("The list after conversion is : " + str(set(y)))

all_unique(x) #Flase
all_unique(y) #True


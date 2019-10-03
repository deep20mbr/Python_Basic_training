#!/usr/bin/env python
# coding: utf-8

# In[1]:


#How to access elements in a tuple
dimension=(200,500)
print(dimension[0])


# In[2]:


print(dimension[1])


# In[6]:


#Zen of Python
#This is nothing but the guidelines to write python code.
#It describes how python is simple yet can handle complex things


# In[7]:


import this


# In[9]:


#PEP-8
#It stands for Python enhancement Proposal-8
#This is again a kind of guideline to follow which says we need to maintain code consistency.


# In[ ]:


#Tuple is immutable.However we can update the values by using collapse and rebuild method like below


# In[10]:


dimensions=(200,300)
print(dimensions)


# In[11]:


dimensions=(100,200)
print(dimensions)


# In[12]:


#we can also change data type to List and use it


# In[13]:


#implementation of if condition.


# In[14]:


cars=['audi','bmw','benz','maruti']
#conditions:
#1.If maruti comes up-all letters need to be capitalized
#2.If any other than it needs to be formatted in a titled case.


# In[26]:


for x in cars:
    if x=='maruti':
        print(x.upper())
    else:
        print(x.title())


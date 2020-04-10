#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


np.random.seed()


# In[5]:


np.random.randint(1,3,10)


# In[6]:


2 * np.random.random(10)+1


# In[7]:


np.random.uniform(1,3,10)


# In[8]:


np.random.normal(size=(4,4))


# In[9]:


np.random.binomial(n=5,p=0.5,size=10)


# In[10]:


data = np.arange(10)
np.random.choice(data, 5)


# In[11]:


np.random.choice(data, 5,replace=False)


# In[12]:


np.random.permutation(data)


# In[15]:


np.random.shuffle(data)
print(data)


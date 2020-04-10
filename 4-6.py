#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


matrix = np.array([
    [1,2],
    [3,4]
])


# In[3]:


another_matrix = np.dot(matrix, matrix.T)


# In[4]:


print(another_matrix)


# In[7]:


U,s,V = np.linalg.svd(another_matrix, 2)


# In[8]:


S = np.array([
    [s[0], 0],
    [0, s[1]]
])


# In[9]:


print(U)


# In[10]:


print(s)


# In[11]:


print(V)


# In[12]:


np.dot(U,np.dot(S,V))


# In[13]:


print(S)


# In[ ]:





# In[ ]:





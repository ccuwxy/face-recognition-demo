#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


vector_a = np.array([1,2,3])


# In[6]:


vector_b = np.array([2,3,4])


# In[7]:


np.dot(vector_a,vector_b)


# In[8]:


vector_a.dot(vector_b)


# In[9]:


np.dot(vector_a,vector_b.T)


# In[10]:


matrix_a = np.array([[1,2],
                   [3,4]])


# In[11]:


matrix_b = np.dot(matrix_a,matrix_a.T)


# In[12]:


matrix_b


# In[13]:


#求范数（默认二范数）
np.linalg.norm([1,2])


# In[14]:


np.linalg.norm([1,2],1)


# In[15]:


np.linalg.norm([1,2,3,4],np.inf)


# In[16]:


np.linalg.norm([1,2,3,4],-np.inf)


# In[17]:


np.linalg.norm(matrix_b)


# In[18]:


np.linalg.det(matrix_a)


# In[19]:


np.trace(matrix_a)


# In[20]:


np.linalg.matrix_rank(matrix_a)


# In[21]:


vector_a * vector_b


# In[22]:


vector_a ** vector_b


# In[23]:


np.linalg.pinv(matrix_a)


# In[24]:


np.linalg.inv(matrix_a)


# In[ ]:





# In[ ]:





# In[ ]:





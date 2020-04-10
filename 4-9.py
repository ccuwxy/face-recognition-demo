#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


image = cv2.imread("tp.jpg")
image.shape


# In[3]:


print(image)


# In[4]:


cv2.imwrite("tp.bak.jpg",image)


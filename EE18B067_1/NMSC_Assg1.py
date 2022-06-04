#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import math


# In[13]:


a = np.zeros(16) #initialising the array storing integral values
a[0] = 2/math.pi #initialising with I0

for i in range(15):
    a[i+1] = 1/math.pi - a[i]*(2*(i+1)*(2*i+1))/(math.pi**2) #recurrence relation

print(np.around(a,7)) #rounding to 7 digits to compare with wolfram alpha


# In[14]:


#wolfram alpha array

a_w = np.asarray([0.63662,0.18930,0.088144,0.050384,0.032433,0.022561,0.016574,0.012679,0.010006,0.0080938,0.0066802,0.0056060,0.0047708,0.0041089,0.0035754,0.0031393])


# In[16]:


print(np.around(np.abs(a-a_w),5))


# In[ ]:





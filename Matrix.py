#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

A = np.array([[8,-1,-1,-1,-1,-1,-1,-1,0,-1,0],[-1,6,-1,-1,0,0,-1,0,-1,-1,0],[-1,-1,4,-1,-1,0,0,0,0,0,0,],[-1,-1,-1,7,-1,-1,0,-1,0,0,0],[-1,0,-1,-1,6,-1,-1,-1,0,0,0],[-1,0,0,-1,-1,4,-1,0,0,0,0],[-1,-1,0,-1,-1,-1,4,0,0,0,0],[-1,0,0,-1,-1,0,0,3,0,0,0],[0,-1,0,0,0,0,0,0,1,0,0],[-1,-1,0,0,0,0,0,0,0,3,-1],[0,0,0,0,0,0,0,0,0,-1,1]])
eigvals, eigvecs = la.eig(A)
eigvals = eigvals.real
print(eigvals)

lambda2 = eigvals[5]
print(lambda2)

v2 = eigvecs[:,5].reshape(11,1)
print(v2)


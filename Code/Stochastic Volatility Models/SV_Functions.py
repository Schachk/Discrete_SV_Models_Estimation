#!/usr/bin/env python
# coding: utf-8

# ## Stochastic Volatility Functions

# In[3]:


import numpy as np
import pandas as pd
import random as rd
import math


# In[4]:


def sv_simul(μ, ϕ, τ, T, h0):
    z = np.random.normal(0, 1, T)
    u  = np.random.normal(0, τ**2, T)
    ϵ = []
    r = []
    h = []

    h.append(μ + ϕ*(h0 - μ) + u[0])
    ϵ.append(z[0] * np.exp(h[0] / 2))
    r.append(μ + ϵ[0])

    for t in range(1, T):
        h.append(μ + ϕ*(h[t-1] - μ) + u[t])
        ϵ.append(z[t] * np.exp(h[t] / 2))
        r.append(μ + ϵ[t])
        
    return r, h, ϵ


# In[21]:


def sv_simul_v2(μ, ϕ, σ1, σ2, T, h0):
    ξ = np.random.normal(0, σ2**2, T)
    ϵ = []
    y = []
    h = []
    
    h.append(μ + ϕ*(h0 - μ) + ξ[0])
    ϵ.append(float(np.random.normal(0, σ1**2 * np.exp(h[0]), 1)))
    y.append(μ + ϵ[0])
    
    for t in range(1, T):
        h.append(μ + ϕ*(h[t-1] - μ) + ξ[t])
        ϵ.append(float(np.random.normal(0, σ1**2 * np.exp(h[t]), 1)))
        y.append(μ + ϵ[t])
        
    return y, h, ϵ
    


# In[19]:


# Inputs
μ = 1
ϕ = 0.4
σ1 = 0.76
σ2 = 1
T = 500
h0 = 0


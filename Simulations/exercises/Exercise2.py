# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:35:22 2020

@author: Victoria Monteiro
"""

from pylab import*

#Criando funcao que retorna a força resultante
k, m, b, F0 = 2.0, 1.0, 0.02, 0.5
omega = 0.99*sqrt(k/m)

def F(x, v, t):
    return -k*x - b*v + F0*cos(omega*t) 

#Criando uma funcao Euler-Cromer

def EulerCromer (t0, tf, dt, x0, v0, F, m, n_trans):    
    #Setting step for time
    t = arange(t0, tf + dt, dt)
    n = len(t)
    
    
    x = zeros(n, float)
    v = zeros(n, float) 
    
    x[0] = t0    #initial value
    v[0] = v0    #initial value

    
    #Se n_trans = 0
    if n_trans == 0:
        n_trans = 1
    
    for i in range(n_trans, n):
        v[i] = v[i - 1] + F(x[i - 1], v[i - 1], t[i - 1]) / (m*dt)
        x[i] = x[i - 1] + v[i]*dt
        
    return x, v





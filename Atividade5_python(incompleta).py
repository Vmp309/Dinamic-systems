# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:26:03 2020

@author: Victoria Monteiro Pontes
"""

from pylab import *

"""Variáveis e arrays necessários"""

n = 2000
x = zeros(n, float)
y = zeros(n, float)

x[0] = 0
y[0] = 0
    
for i in range (n - 1):
    guessX = randint(6)+1
    
    guessY = randint(6)+1
    
    if guessX <= 2:
        dx = -1   
        x[i + 1] = x[i] + dx 
        
    elif 2 <= guessX <=4:
        dx = 0   
        x[i + 1] = x[i] + dx 
        
    elif 4 <= guessX <= 6:
        dx = 1
        x[i + 1] = x[i] + dx 
   
    if guessY <= 2:
        dy = -1
        y[i + 1] = y[i] + dy
        
    elif  2 <= guessY <= 4:
        dy = 0
        y[i + 1] = y[i] + dy
        
    elif 4 <= guessY <= 6:
        dy = 1
        y[i + 1] = y[i] + dy
    
plot(x,y)
show()

            
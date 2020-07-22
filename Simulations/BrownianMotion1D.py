# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 16:49:16 2020

@author: Victoria Monteiro Pontes
"""

from pylab import *
n = 1000
x = zeros(n, float)
for i in range(n-1):
    if (randint(6)+1 <=3):
        dx = -1
    else:
        dx = 1

    x[i+1] = x[i] + dx
        
plot(x)
xlabel('i')
ylabel('x(i)')
show()


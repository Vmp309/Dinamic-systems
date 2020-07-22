# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 17:00:16 2020

@author: Victoria Monteiro Pontes
"""

from pylab import *

#Atribuindo aos arrays o valores dos dados
#Array para o tempo t(s)
t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Array para a posicao do y(m)
y = [0, 15, 60, 135, 240, 375, 540, 735, 960, 1215]

#Showing the graph
plot(t, y, '-bo')
xlabel('t(s)')
ylabel('y(m)')

dt = t[- 1] - t[0]
dy = y[- 1] - y[0]

deltaT = t[1] - t[0]

#Velocidade media
v = dy/dt
print(v)

#Aceleracao media, obs: Precisamos definir as velocidade instantaneas para 
#saber v_inst (v instante)
n = len(y)
v_inst = zeros(n, float)

for i in range(1, n):
    v_inst[i] = (y[i] - y[i-1])/deltaT

#Aceleracao media
a = (v_inst[-1] - v_inst[0])/dt
print(a)


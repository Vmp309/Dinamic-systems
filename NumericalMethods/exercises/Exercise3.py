# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 12:48:14 2020

@author: Victoria Monteiro Pontes
"""

from pylab import *

dataT = loadtxt('trajectory.txt')

"""Lendo e armazenando os dados de cada coluna em um array diferente"""
t = dataT[:, 0]

x = dataT[:, 1]

y = dataT[:, 2]

"""Plotagem do gráfico de x e y em funcao de t"""
plot (t, x, t, y)
title('Gráfico de x (em azul) e y(em laranja) em função de t')
xlabel('t')
show()

plot(x, y)
title('Gráfico da trajetória do projétil')
xlabel('X')
ylabel('Y')
show()

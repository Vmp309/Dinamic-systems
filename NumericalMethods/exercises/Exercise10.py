# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:36:32 2020

@author: Victoria Monteiro
"""

from pylab import *
latitude=33.3 # graus, pulou sobre o Novo México
latitude=latitude/360*2*pi # convertendo em radianos para ser empregado na função g(x)

# fórmula para calcular g em função da altura (x) e da latitude
def g(x):
    return 9.780327*(1+0.0053024*sin(latitude)**2-0.0000058*sin(2*latitude)**2)-3.086e-6*x # fórmula (3) do artigo

# fórmula para calcular a densidade do ar em função da altura (x)
def densidade(x):
    return 1.225*exp(-x/8882) # fórmula (1) do artigo

C=0.003 # é uma constante (que depende da área que o paraquedista oferece ao ar transversalmente à direção do seu movimento e de um coeficiente de arrasto).
# Considere uma aceleração contrária a queda da seguinte forma:
def arrasto(x,v):
    return C*densidade(x)*v**2

tf=100 # tempo final da simulação
dt=0.001
n = int(ceil(tf/dt))+1
t = linspace(0.0, tf, n)
x=zeros(n)
v=zeros(n)
a=zeros(n)

def F(x,v):
    return -g(x)+arrasto(x,v)

x[0]=38970 # m, altura da qual pulou
v[0]=0 # pulou (de uma cápsula conectada a um balão) com velocidade nula
a[0] = F(x[0], v[0])

# Método de Euler Cromer
for i in range (1, n):
    v[i] = v[i - 1] - dt*F(x[i - 1], v[i - 1])
    x[i] = x[i - 1] - dt*v[i - 1]
    a[i] = F(x[i], v[i])

# faça o gráfico da velocidade para cada instante de tempo e compare com a figura 4 do artigo

plot(t, v)
xlabel('t (s)')
ylabel('v (m/s)')

"""Comparando com o gráfico plotado com o gráfico do artigo é possível
perceber uma diferença nos valores encontrados no "pico" do gráfico.
O gráfico plotado tem máximo de 300 enquanto o gráfico do artigo apresenta valor
380 no pico, uma diferença muito grande. Entretanto o formato do gráfico plotado
se apresenta semelhante ao gráfico do artigo.  
OBS: Os sinais nas linhas 42 e 43 foram trocados de positivo para negativo 
apenas para facilitar a comparação entre gráficos."""




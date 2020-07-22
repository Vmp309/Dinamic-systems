# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 10:00:00 2020
Constrói os gráficos para posição, velocidade e aceleração
de uma bola de tênis caindo, a partir de dados experimentais.
Os dados de posição foram capturados por um detetor de movimento
a uma taxa de um ponto por milissegundo.
Compara os dados experimentais com um modelo dinâmico, levando em conta
as seguintes forças associadas aos seguintes fenômenos: 
    1 - gravidade
    2 - viscosidade com o ar
    3 - colisão com o chão
    4 - dissipação de energia durante a colisão (inelástica) 

@author: Hugo Cavalcante
"""

from pylab import *
### Lê os dados do arquivo de texto
t, x = loadtxt('fallingtennisball02.txt', usecols = (0,1), unpack = True)

### Gráfico da posição em função do tempo
#plot(t,x)
#xlabel('t (s)')
#ylabel('x (m)')
###

dt = t[1] -t[0]   # cálculo do intervalo de tempo entre pontos

# cálculo da velocidade (forma vetorizada)
v = (x[1:] -x[0:-1])/dt

### Gráfico da velocidade em função do tempo
# plot(t[0:-1],v)
# xlabel('t (s)')
# ylabel('v (m/s)')
###

# cálculo da aceleração
a = (v[1:] -v[0:-1])/dt

### Note que a cada derivada o número de pontos é reduzido em uma unidade
print("Número de elementos em x: ", len(x))
print("Número de elementos em v: ", len(v))
print("Número de elementos em a: ", len(a))

### Gráficos combinados em uma figura (com subplot)

"""figure()
subplot(3,1,1)
subplots_adjust(hspace = 0.25)
plot(t,x)
#xlabel('t (s)')
ylabel('x (m)')
subplot(3,1,2)
plot(t[0:-1],v)
#xlabel('t (s)')
ylabel('v (m/s)')
subplot(3,1,3)
plot(t[0:-2],a/1000)
xlabel('t (s)')
ylabel('a (km/s²)')  """

###### Construção do modelo:  
#dt = 1e-5
g = 9.8 # módulo da aceleração da gravidade em m/s²
D = 0.0245 
tf = 2.497 #0.59 #0.56
## estimativa da "constante de mola" durante a colisão
k = -amax(a)/amin(x)
### formas alternativas para a colisão (mola não-linear)
#k2 = 0.3*amax(a)/(amin(x)**4)
Db = 13.965
kvb = 55.0
dTeto = 23.965
kvbTeto = 55.0



def F(x,v):

    #return -g -D*sign(v)*v**2
    if x <= 0.0:
        return -g -D*v*abs(v) -kvb*v -k*x
    
    if x >= 2.0:
        return -g -D*v*abs(v) -kvb*v - Db*v*abs(v)

    else:
        #return -g -D*v*abs(v) -k*x
        #return -g -Db*v*abs(v) -k*x #-k2*(x**3)*abs(x) 
        return -g -D*v*abs(v)

n = int(ceil(tf/dt))+1
t_model = linspace(0.0, tf, n)
x_model = zeros(n) 
v_model = zeros(n)
a_model = zeros(n)

x_model[0] = 1.6
v_model[0] = -20.0 
a_model[0] = F(x_model[0], v_model[0])

# Método de Euler Cromer
for i in range(1,n):
    v_model[i] = v_model[i-1] + dt*F(x_model[i-1], v_model[i-1])
    x_model[i] = x_model[i-1] + dt*v_model[i]
    a_model[i] = F(x_model[i], v_model[i])    


#dt = 1e-3
#n = int(ceil(tf/dt))+1

#### gráfico comparando os dados experimentais e o modelo até n pontos
#### 1 s = 1000 pontos

figure()
ax1 = subplot(3,1,1)
subplots_adjust(hspace = 0.25)
#plot(t[0:n],x[0:n])
plot(t_model, x_model)
xlabel('t (s)')
ylabel('x (m)')
ax2 = subplot(3,1,2, sharex = ax1)
#plot(t[0:n],v[0:n])
plot(t_model,v_model)
xlabel('t (s)')
ylabel('v (m/s)')
subplot(3,1,3, sharex = ax1)
#plot(t[0:n],a[0:n])
plot(t_model,a_model)
xlabel('t (s)')
ylabel('a (m/s²)')


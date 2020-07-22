# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:13:32 2020

@author: Victoria Monteiro Pontes
"""

"""Abra o 'livro adotado na disciplina'. Procure a tabela 4.1 (table 4.1,
 página 45). A tabela mostra a posição e o tempo do corredor Usain Bolt em 
100m rasos. Use os dados desta tabela para fazer um 'plot' parecido ao da 
figura 4.2.

 Não esqueça de usar 'xlabel' e 'ylabel' para colocar as unidades empregadas 
 em cada eixo do gráfico. Faça o upload de um arquivo com o código Python 
 gerar um gráfico similar ao da figura 4.2 empregado a tabela 4.1."""
 
 # O eixo x representará o tempo em segundos(s) enquanto o eixo y representará
 # a distância percorrida em metros(m)

from pylab import *
 
# Valores do eixo x
x = [0, 1, 2, 3, 4, 5, 6]

# Valores do eixo y
y = [0.0, 3.4, 11.1, 21.3, 33.2, 45.8, 57.9]

xlabel('tempo (s)')  
ylabel('metros (m)')  

plot(x, y, '-bo')

show()
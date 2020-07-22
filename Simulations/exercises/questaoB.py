# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:49:28 2020

@author: Victoria Monteiro
"""

from pylab import *

from teste_integral import *

#definicao da funcao de seno ao quadrado
def f(x):
    return sin(x) * sin(x)

#Testando a funcao definite_integral com o a funcao f como parametro
y = definite_integral(f, 0, 2*pi)

print(y)

"""Como a resposta está correta (retorna valor muito aproximado de pi), 
definite_integral esta funcionando"""
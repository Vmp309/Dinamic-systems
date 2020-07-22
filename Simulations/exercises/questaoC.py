# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:49:28 2020

@author: Victoria Monteiro
"""

from pylab import *

from teste_integral import *

#Testando a funcao definite_integral com cos(x) como parâmetro
#o resultado esperado da integral definida de cos(x) em [0, 2*pi] é 0
n = 1000
x = linspace(0, 2*pi, n)

y = definite_integral(cos, 0, 2*pi)

print(y)

"""Comparação: o resultado obtido não é zero e sim um valor muito proximo a ele
 devido a dificuldade de representação do valor zero absoluto"""   


 
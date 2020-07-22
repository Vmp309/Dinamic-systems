# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:55:50 2020

@author: Victoria Monteiro
"""

from pylab import *

#parametro f: funcao a ser integrada
#parametro a: inicio do intervalo
#parametro b: fim do intervalo


#funcao poli para fazer pequenos testes
def poli(x):
    return x + 1 

def definite_integral (f, a, b):
    n = 1000
    x = linspace(a, b, n)
    resultado = 0
    
    for j in range(n):
        if j > 0:
            resultado += f(x[j]) * (x[j] - x[j - 1])  
        
    return resultado



"""
#polinômio qualquer para testar definite_integral



def definite_integral(a, b):
    n = 1000
    x = linspace(a, b, n)
    resultado = 0

    for i in range (n):
        if (i != 0):
            resultado += poli(x[i]) * (x[i] - x[i-1])
        
    return resultado

print(definite_integral(0, 2*pi))"""

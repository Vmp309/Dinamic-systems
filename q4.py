# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:59:36 2020

@author: vick_
"""


from numpy import *

def sinal(x):
    if x > 0:
        return 1; """Número positivo"""
    else: 
        return -1; """Número negativo"""
    
    
def poli(t):
      return 2*t**2+4*t-7

def raiz(f,a,b):
      n=100
      sinalA = sinal(poli(a))
      sinalB = sinal(poli(b))
      
      while True:
            n=n+100
            x=linspace(a,b,n)
            for i in range(n):
                print("Resultado do polinomio:")
                print(poli(x[i]))
                print("Posicao no eixo x:")
                print(x[i])
                if sinal(poli(x[i])) == sinalB:
                        return(x[i])

a=-3.2
b=-3
r=raiz(poli,a,b)
print(r, ' é raiz do polinômio')


"""1. Por que a execução deste código aparenta não terminar?
Resposta: Olhando para a raiz do polinômio (cálculo feito manualmente) que está entre os valores armazenados nas variáveis "a" e "b", podemos perceber que esta raiz possui infinitas casas decimais, isso faz com que o computador não possa representá-la de forma precisa o que torna inviável para a função poli(x[i]) retornar um zero absoluto, o que também resulta em um loop infinito. 

2. Como podemos corrigir o código para que ele consiga encontrar aproximadamente uma raiz no intervalo [a,b]?
Resposta: Podemos corrigir o programa modificando o código para que ele monitore quando a função poli(x[i]) muda seu sinal (indicando que o poli(x[i]) passou pelo zero). Neste caso podemos escolher retornar x[i] ou x[i -1] como raiz na função raiz(). Segue o código abaixo com as modificações:"""





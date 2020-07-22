# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 12:48:43 2020

@author: Victoria Monteiro
"""


i=1
while True:
      i=i+1
      epsilon=1/(2**i)
      if 1+epsilon==1:
            break
      print('i=',i,' 1 +',epsilon,' = ',1+epsilon)

print('Olha que horror: 1 +',epsilon,' = ',1+epsilon,'!')

"""Para variáveis cujos os valores atribuídos a elas são decimais, 
o tipo utilizado é o float por ser mais preciso. Entretanto, essa 
precisão também é limitada, alguns números são representados de forma 
aproximada e não de forma exata. Esse tipo de representação faz com que 
certas operações com esses valores tenham comportamentos inesperados. 
Nesse caso, ao compararmos a expressão "epsilon + 1" com "1" (epsilon == 1),
 o computador entende como uma afirmação verdadeira, devido a essas 
 pequenas imprecisões. Como a representação do número "epsilon" + 1 é 
 imprecisa, o computador utiliza a notação mais próxima desse valor, no caso, 1."""

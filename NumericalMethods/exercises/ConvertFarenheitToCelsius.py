# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:37:41 2020

@author: Victoria Monteiro Pontes
"""

"""Atividade 1: Faca upload de um arquivo com o código Python para converter 
  graus Farenheit para centígrados   
"""

def convert (TF):
    ratio = 5/9
    
    constante = 32
    
    TC = ratio * (TF - constante)
    
    TC = round(TC, 2)
    
    return TC

print (convert(1))

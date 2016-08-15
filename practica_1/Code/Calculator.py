# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 22:24:51 2016

@author: francisco
"""
class Calculator(object):
    
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0
        
    def suma(self):
        self.resultado = self.valor1 + self.valor2
    
    def resta(self):
        self.resultado = self.valor1 - self.valor2
    
    def pasaValor1(self,a):
        self.valor1 = a
    
    def pasaValor2(self,b):
        self.valor2 = b
    
    def imprimeResult(self):
        print(self.resultado)
        
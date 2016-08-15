# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 23:17:05 2016

@author: francisco
"""
import Calculator

class ScientificCalculator(Calculator.Calculator):

    def multi(self):
        self.resultado = self.valor1 * self.valor2
        
    def divi(self):
        self.resultado = float(self.valor1) / float(self.valor2)
    
    def modulo(self):
        self.resultado = self.valor1 % self.valor2
    
    def potencia(self):
        self.resultado = self.valor1 ** self.valor2
        
    def limpia(self):
        self.resultado = 0
        self.valor1 = 0
        self.valor2 = 0
    
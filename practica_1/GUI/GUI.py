# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 23:44:00 2016

@author: francisco
"""

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
import  Code.ScientificCalculator as calc
import  Code.Acceso as acc

class GUI(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.inicializaGUI()
        
    def inicializaGUI(self):
        self.operador = ""
        self.calcu = calc.ScientificCalculator() 
        self.line = QtGui.QLineEdit(self)
        self.line.move(5,5)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.resize(200,25)
        cero = QtGui.QPushButton("0",self)
        cero.move(10,200)
        uno = QtGui.QPushButton("1",self)
        uno.move(10,50)
        dos = QtGui.QPushButton("2",self)
        dos.move(60,50)
        tres = QtGui.QPushButton("3",self)
        tres.move(110,50)
        cuatro = QtGui.QPushButton("4",self)
        cuatro.move(10,100)
        cinco = QtGui.QPushButton("5",self)
        cinco.move(60,100)
        seis = QtGui.QPushButton("6",self)
        seis.move(110,100)
        siete = QtGui.QPushButton("7",self)
        siete.move(10,150)
        ocho = QtGui.QPushButton("8",self)
        ocho.move(60,150)
        nueve = QtGui.QPushButton("9",self)
        nueve.move(110,150)
        listabotones = [cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve]
        nuevo_usuario = QtGui.QPushButton("Registrar Usuario",self) 
        nuevo_usuario.move(10,250)
        nuevo_usuario.resize(nuevo_usuario.sizeHint())
        nuevo_usuario.clicked.connect(self.showDialog)
        for i in listabotones:
            i.resize(35,30)
            i.clicked.connect(self.escribeNumeros)
            
        suma = QtGui.QPushButton("+",self)
        suma.move(160,100)
        resta = QtGui.QPushButton("-",self)
        resta.move(210,100)
        mult = QtGui.QPushButton("*",self)
        mult.move(160,150)
        div = QtGui.QPushButton("/",self)
        div.move(210,150)
        mod = QtGui.QPushButton("MOD",self)
        mod.move(210,200)
        pot = QtGui.QPushButton("^",self)
        pot.move(160,200)
        igual = QtGui.QPushButton("=",self)
        igual.move(110,200)
        igual.resize(35,30)
        igual.clicked.connect(self.obtenResultado)
        borrar = QtGui.QPushButton("CE",self)
        borrar.move(210,50)
        borrar.resize(35,30)
        borrar.clicked.connect(self.borraTodo)
        neg = QtGui.QPushButton("(-)",self)
        neg.move(160,50)
        neg.resize(35,30)
        neg.clicked.connect(self.vuelveNegativo)
        punto = QtGui.QPushButton(".",self)
        punto.move(60,200)        
        punto.resize(35,30)
        punto.clicked.connect(self.puntoDecimal)
        listaops = [suma,resta,mult,div,mod,pot]
        for i in listaops:
            #i.move(10,180)
            i.resize(35,30)
            i.clicked.connect(self.escogeOperacion)
        self.setGeometry(300,300,210,220)
        self.setFixedSize(250,300)
        self.setWindowTitle("Calculadora")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()
        
        
    
        
    def showDialog(self):
        
        usuario, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Usuario:')
        contrasena, ok_2 = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Contrasena:')
            
        if ok_2:
            registrarUsuario(str(usuario),str(contrasena))            
        
           
    
        
        
    def escribeNumeros(self):
        sender = self.sender()
        n1 = int(sender.text())
        ntexto = str(n1)
        #if self.operador == "":
        self.line.setText(self.line.text() + ntexto)
        #else:
         #   self.line.setText(ntexto)

    def vuelveNegativo(self):
        global value        
        try:
            value = int(self.line.text())
        except:
            value = float(self.line.text())
        value = value * -1
        self.line.setText(str(value))
        
    def borraTodo(self):
        self.calcu.limpia()
        self.line.setText("")
        self.operador == ""
        
    def puntoDecimal(self):
        if "." not in self.line.text():
            self.line.setText(self.line.text() + ".")
        
    def escogeOperacion(self):
        try:
            self.calcu.valor1 = int(self.line.text())
        except:
            self.calcu.valor1 = float(self.line.text())
        sender = self.sender()
 
        self.operador = sender.text()
        self.line.setText("")        

        
    def obtenResultado(self):
        try:
            self.calcu.valor2 = int(self.line.text())
        except:
            self.calcu.valor2 = float(self.line.text())

        if self.operador == "+":
            self.calcu.suma()
 
        elif self.operador == "-":
            self.calcu.resta()
 
        elif self.operador == "/":
            self.calcu.divi()
 
        elif self.operador == "*":
            self.calcu.multi()
            
        elif self.operador == "MOD":
            self.calcu.modulo()
            
        elif self.operador == "^":
            self.calcu.potencia()
        self.line.setText(str(self.calcu.resultado))
        self.operador == ""


def registrarUsuario(usuario, contrasena):
        contrasena = acc.suma_cinco(contrasena)
        f = open('Code\input.txt','a')
        f.write('\n'+usuario+","+contrasena) 
        f.close()   
        
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    main= GUI()
    main.show()
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
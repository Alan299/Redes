# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 21:32:40 2016

@author: Alan
"""

from PyQt4 import QtGui
from Code import Acceso
from GUI import GUI 


class Login(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle('Inicio de Sesion')
        self.textName = QtGui.QLineEdit(self)
        self.textPass = QtGui.QLineEdit(self)
        
        self.buttonLogin = QtGui.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.ManejaLogin)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def ManejaLogin(self):
        if (Acceso.ingresar(self.textName.text() ,self.textPass.text())):
            self.accept()
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Usuario o contraseña invalido')
    






class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
      
      

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtGui.QDialog.Accepted:
        g = GUI.GUI()
        g.show()
        sys.exit(app.exec_())
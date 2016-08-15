import sys
from PyQt4 import QtCore, QtGui
from GUI import Login as log
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex =log.Login()
    ex.show()
    sys.exit(app.exec_())
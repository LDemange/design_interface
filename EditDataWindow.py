#! /usr/bin/python
#*coding: utf8 *

import sys
from PyQt5 import QtCore, QtWidgets
from EditDataWindow_ui import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar



class CEditDataWindow(QtWidgets.QMainWindow):
    
    def __init__(self, MW=None, parent=None):
        super(CEditDataWindow, self).__init__(parent=parent) #  nouvelle notation depuis python 3 : super().__init__(parent=parent)
        self._ui = Ui_CEditDataWindow() # On peut remplacer ces deux dernieres lignes par :
        self._ui.setupUi(self)        # self.setupUi(self)
        self._MW = MW
        self.update_DW(self._MW)
        
    def update_DW(self, MW):
        self._ui.CurveChoice.addItem('Toto')
        #mm = MW._figure.gca()
        #line = mm.lines[0]
        ##mm.lines[0].remove()
        #print(line.get_xydata())
        

        
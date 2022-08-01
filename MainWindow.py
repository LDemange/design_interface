#! /usr/bin/python
#*coding: utf8 *

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.pyplot import close, figure
from MainWindow_ui import *
import numpy as np

import weakref

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class CMainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(CMainWindow, self).__init__(parent=parent) #  nouvelle notation depuis python 3 : super().__init__(parent=parent)
        ui = Ui_CMainWindow() # On peut remplacer ces deux dernieres lignes par :
        ui.setupUi(self)        # self.setupUi(self)
        ui.actionCreer.triggered.connect(lambda : self.CreerMenuFonction())
        #ui.actionGraph_en_temporel.triggered.connect(lambda : self.CreerGraphTemp())
        self._mdiArea = QtWidgets.QMdiArea(self)
        self._mdiArea.show()
        self._mdiArea.setEnabled(True)
        self._mdiArea.setGeometry(QtCore.QRect(80, 50, 1750, 951)) 
        self._mdiArea.setMinimumSize(QtCore.QSize(1750, 950))
        self._mdiArea.setObjectName("_mdiArea")
        CMainWindow._MWinstance = self
        self._liste_curve=[]

    def CreerMenuFonction(self):
        import MenuFonction
        self._MF = MenuFonction.CMenuFonction(self)
        self._MF.show()
        self._MF._ui.ValidateButton.pressed.connect(lambda : self.CreerGraphTemp())

    def CreerGraphTemp(self):
    
        from math import cos, sin, exp, sqrt, erf, cosh, sinh
        import matplotlib
        from numpy import fft, complex, pi, arange, random, zeros, log10, floor
        from matplotlib import pyplot as plt
    
        self._liste_curve.append([self._MF._x, self._MF._y])

        try:
            self._figure
        except:
            print('fig does not exist')
            self._GraphWindow =  QtWidgets.QMdiSubWindow(self) # Creation GraphWindow
            self._mdiArea.addSubWindow(self._GraphWindow) #Placement dans la GraphWindow dans la MdiArea  
            self._figure = Figure() # a figure instance to plot on
            
            # this is the Canvas Widget that displays the `figure`
            # it takes the `figure` instance as a parameter to __init__
            self._canvas = FigureCanvas(self._figure)

            # this is the Navigation widget
            # it takes the Canvas widget and a parent
            self._toolbar = NavigationToolbar(self._canvas, self)
        
            self._GraphWindow.layout().addWidget(self._canvas) #AJout du Canvas à la GraphWindow`
            self._GraphWindow.layout().addWidget(self._toolbar) #AJout de toolbar à la GraphWindow`

        self._figure.clear()
        ax = self._figure.add_subplot(111, position=[0.06, 0.06, 0.9, 0.9]) #Creation du ou des graphs et definition [X0, Y0, LX, LY]
        ax.set_title('Title', fontsize=18)
        ax.set_xlabel('x', fontsize=16)
        ax.set_ylabel('y', fontsize=16)
        for curve in self._liste_curve:
            print(curve[0])
            #plt.plot(curve[0], curve[1]) #ne fonctionne pas
            line = ax.plot(curve[0], curve[1]) #Creation liste de courbe line

        
        #line.append(ax.plot(self._MF._x, self._MF._y)) # ou line = ax.plot(t, 0*u), ajouter une courbe
 
        self._GraphWindow.show()
        
   
   
      
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w=0
    w = CMainWindow()
    w.show()
    sys.exit(app.exec_())
    

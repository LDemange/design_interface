#! /usr/bin/python
#*coding: utf8 *

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.pyplot import close, figure

from MainWindow_ui import *

import weakref

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class CMainWindow(QtWidgets.QMainWindow):
    
    _MWinstance = 0
    
    def __init__(self, parent=None):
        super(CMainWindow, self).__init__(parent=parent) #  nouvelle notation depuis python 3 : super().__init__(parent=parent)
        ui = Ui_CMainWindow() # On peut remplacer ces deux dernieres lignes par :
        ui.setupUi(self)        # self.setupUi(self)
        ui.actionCreer.triggered.connect(lambda : CreerMenuFonction(self))
        ui.actionGraph_en_temporel.triggered.connect(lambda : CreerGraphTemp(self))
        self._mdiArea = QtWidgets.QMdiArea(self)
        self._mdiArea.show()
        self._mdiArea.setEnabled(True)
        self._mdiArea.setGeometry(QtCore.QRect(80, 50, 1750, 951)) 
        self._mdiArea.setMinimumSize(QtCore.QSize(1750, 950))
        self._mdiArea.setObjectName("_mdiArea")
        CMainWindow._MWinstance = self
        #print('MW _MWinstance=',self._MWinstance) #test variable statique

def CreerMenuFonction(self):
    import MenuFonction
    w = MenuFonction.CMenuFonction(self)
    w.show()
    
def CreerGraphTemp(self):
    
        from math import cos, sin, exp, sqrt, erf, cosh, sinh
        import numpy
        import matplotlib
        from numpy import fft, complex, pi, arange, random, zeros, log10, floor
        from matplotlib import pyplot as plt
    
        taille_legende=9

        N=1000
        T=5
        f0=5
        t=numpy.linspace(0,T,N)
    
        u=numpy.zeros(N)
        for i in range (0,N):
            u[i]=cos(2*pi*f0*t[i])
        
        self.GraphWindow =  QtWidgets.QMdiSubWindow(self) # Creation GraphWindow
        self._mdiArea.addSubWindow(self.GraphWindow) #Placement dans la GraphWindow dans la MdiArea  
        self._figure = Figure() # a figure instance to plot on
        
        

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self._canvas = FigureCanvas(self._figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self._canvas, self)
        
        self.GraphWindow.layout().addWidget(self._canvas) #AJout du Canvas à la GraphWindow`
        self.GraphWindow.layout().addWidget(self.toolbar) #AJout de toolbar à la GraphWindow`
        
        ax = self._figure.add_subplot(111, position=[0.06, 0.06, 0.9, 0.9]) #Creation du ou des graphs et definition [X0, Y0, LX, LY]
        
        line = ax.plot(t, u) #Creation liste de courbe line
        ax.set_title('A single plot', fontsize=18)
        ax.set_xlabel('t en s', fontsize=16)
        ax.set_ylabel('|u|', fontsize=16)
        
        line.append(ax.plot(t, 0*u)) # ou line = ax.plot(t, 0*u), ajouter une courbe
        
        #print(wl := weakref.ref(line[0])) #reference a l objet devant etre supprime
        #line.pop(0).remove()              #pop(0) enleve la courbe de la liste (indispensable) et remove, supprime la courbe
        #print(wl)                         #reference a lobjet supprime
 
        self.GraphWindow.show()
        
   
   
      
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w=0
    w = CMainWindow()
    w.show()
    sys.exit(app.exec_())
    
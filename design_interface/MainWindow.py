#! /usr/bin/python
#*coding: utf8 *

import sys
from PyQt5 import QtCore, QtWidgets
from MainWindow_ui import *

from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np

class CMainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(CMainWindow, self).__init__(parent=parent) #  nouvelle notation depuis python 3 : super().__init__(parent=parent)
        self._ui = Ui_CMainWindow() # On peut remplacer ces deux dernieres lignes par :
        self._ui.setupUi(self)        # self.setupUi(self)
        self._ui.actionCreer.triggered.connect(lambda : self.CreerMenuFonction())
        self._ui.actionDonnees.triggered.connect(lambda : self.CreerDataWindow())
        self._ui.pushButton.pressed.connect(lambda : self.refresh())
        self._ui.AutoZoomButton.pressed.connect(lambda : self. AutoZoom())
        self.CreerGraph()
    
    def AutoZoom(self):
        mm = self._figure.gca()
        x=[]
        y=[]
        for curve in mm.lines[:]:
            print('type(curve)=',type(curve))
            print('type(curve.get_xdata())=',type(curve.get_xdata()))
            print('type(x)=',type(x))
            x.append(curve.get_xdata())
            y.append(curve.get_ydata())
        min_x = np.min(x)
        max_x = np.max(x)
        min_y = np.min(y)
        max_y = np.max(y)
        delta_x = 0.025*(max_x - min_x)
        delta_x = 0.025*(max_x - min_x)
        delta_y = 0.025*(max_y - min_y)
        delta_y = 0.025*(max_y - min_y)
        self._ax.set_xlim(min_x - delta_x, max_x + delta_x)
        self._ax.set_ylim(min_y - delta_y, max_y + delta_y)
        self._figure.canvas.draw()
        
    def refresh(self):
        self._ax.legend(loc = 1, prop={'size': 10})
        self._figure.canvas.draw()
        
        
    def CreerMenuFonction(self):
        import MenuFonction
        self._MF = MenuFonction.CMenuFonction(self)
        self._MF.show()
        
    def CreerDataWindow(self):
        import EditDataWindow
        self._DW = EditDataWindow.CEditDataWindow(self)
        self._DW.show()

    def CreerGraph(self):

        from matplotlib import pyplot as plt

        try:
            self._MF.calcul()
        except:
            pass

        try:
            self._figure
        except:
            self._GraphWindow =  QtWidgets.QMdiSubWindow(self) # Creation GraphWindow

            #self._GraphWindow.resize(3000,2100)
            
            self._ui._mdiArea.addSubWindow(self._GraphWindow) #Placement dans la GraphWindow dans la MdiArea  
            self._GraphWindow.setWindowState(QtCore.Qt.WindowMaximized)

            self._GraphWindow.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
            self._figure = plt.figure()  # a figure instance to plot on
            
            # this is the Canvas Widget that displays the `figure`
            # it takes the `figure` instance as a parameter to __init__
            self._canvas = FigureCanvas(self._figure)

            # this is the Navigation widget
            # it takes the Canvas widget and a parent
            self._toolbar = NavigationToolbar(self._canvas, self)
        
            self._GraphWindow.layout().addWidget(self._canvas) #AJout du Canvas à la GraphWindow`
            self._GraphWindow.layout().addWidget(self._toolbar) #AJout de toolbar à la GraphWindow`
            
            self._ax = self._figure.add_subplot(111, position=[0.06, 0.06, 0.9, 0.9]) #Creation du ou des graphs et definition [X0, Y0, LX, LY]
            self._ax.set_title('Title', fontsize=18)
            self._ax.set_xlabel('x', fontsize=16)
            self._ax.set_ylabel('y', fontsize=16)
            

        try:
            self._ax.plot(self._MF._x, self._MF._y,label=self._MF._name)
            self._ax.legend(loc = 1, prop={'size': 10})
        except:
            pass
        
        self._figure.canvas.draw()
        
        try:
            self._DW.update_DW(self)
        except:
            pass
 
        self._GraphWindow.show()
      
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w=0
    w = CMainWindow()
    w.show()
    sys.exit(app.exec_())
#! /usr/bin/python
#*coding: utf8 *

import sys
from PyQt5 import QtCore, QtWidgets
from MainWindow_ui import *

from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class CMainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(CMainWindow, self).__init__(parent=parent) #  nouvelle notation depuis python 3 : super().__init__(parent=parent)
        ui = Ui_CMainWindow() # On peut remplacer ces deux dernieres lignes par :
        ui.setupUi(self)        # self.setupUi(self)
        ui.actionCreer.triggered.connect(lambda : self.CreerMenuFonction())
        ui.actionDonnees.triggered.connect(lambda : self.CreerDataWindow())
        ui.pushButton.pressed.connect(lambda : self.refresh())
        self._mdiArea = QtWidgets.QMdiArea(self)
        self._mdiArea.show()
        self._mdiArea.setEnabled(True)
        self._mdiArea.setGeometry(QtCore.QRect(80, 50, 1750, 951)) 
        self._mdiArea.setMinimumSize(QtCore.QSize(1750, 950))
        self._mdiArea.setObjectName("_mdiArea")
        self.CreerGraph()
        
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
            
            #self._mdiArea.addSubWindow(self._GraphWindow) #Placement dans la GraphWindow dans la MdiArea  
            self._GraphWindow.setWindowState(QtCore.Qt.WindowMaximized)
            self._GraphWindow.setGeometry(70, 32, 1770, 970)
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
    

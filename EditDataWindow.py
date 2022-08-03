#! /usr/bin/python
#*coding: utf8 *

import sys
from PyQt5 import QtCore, QtWidgets
from EditDataWindow_ui import *
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class CEditDataWindow(QtWidgets.QMainWindow):
    
    def __init__(self, MW=None, parent=None):
        super(CEditDataWindow, self).__init__(parent=parent) #  nouvelle notation depuis python 3 : super().__init__(parent=parent)
        self._ui = Ui_CEditDataWindow() # On peut remplacer ces deux dernieres lignes par :
        self._ui.setupUi(self)        # self.setupUi(self)
        self._MW = MW
        self.update_DW(self._MW)
        self.refresh_DW(self._MW)
        self._ui.CloseButton.pressed.connect(lambda : self.close())
        self._ui.CurveChoice.currentTextChanged.connect(lambda : self.refresh_DW(self._MW))
        
    def refresh_DW(self, MW):

        mm = MW._figure.gca()        
        print('mm.lines[:]=',mm.lines[:])
        print('self._ui.CurveChoice.currentText()=',self._ui.CurveChoice.currentText())
        ind_curve = self.get_ind_curve(mm.lines[:],self._ui.CurveChoice.currentText())
        print('indC=',ind_curve)
        x=mm.lines[ind_curve].get_xdata()
        y=mm.lines[ind_curve].get_ydata()
        self._ui.Xmin.setText(str(format(np.min(x),'.4E')))
        self._ui.Xmax.setText(str(format(np.max(x),'.4E')))
        self._ui.Ymin.setText(str(format(np.min(y),'.4E')))
        self._ui.Ymax.setText(str(format(np.max(y),'.4E')))
        self._ui.NbPoint.setText(str(len(x)))
        #mm = MW._figure.gca()
        #line = mm.lines[0]
        ##mm.lines[0].remove()
        #print(line.get_xydata())
    
    def update_DW(self, MW):
        self._ui.CurveChoice.clear()   
        mm = MW._figure.gca()
        for curve in mm.lines[:]:
            self._ui.CurveChoice.addItem(curve.get_label())     
        
        
    def get_ind_curve(self,liste_curve,name):
        for i in range(0,len(liste_curve)):
            if(liste_curve[i].get_label() == name):
                return i
        return -1              
            
            
        

        
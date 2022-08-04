#! /usr/bin/python
#*coding: utf8 *

import sys
from PyQt5 import QtCore, QtWidgets
from EditDataWindow_ui import *
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

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
        self._ui.DeleteButton.pressed.connect(lambda : self.remove_curve(self._MW))
        self._ui.DataButton.pressed.connect(lambda : self.create_table(self._MW))
        
    def refresh_DW(self, MW): #Display data

        mm = MW._figure.gca()        
        ind_curve = self.get_ind_curve(mm.lines[:],self._ui.CurveChoice.currentText())
        if(ind_curve != -1):
            x=mm.lines[ind_curve].get_xdata()
            y=mm.lines[ind_curve].get_ydata()
            self._ui.Xmin.setText(str(format(np.min(x),'.4E')))
            self._ui.Xmax.setText(str(format(np.max(x),'.4E')))
            self._ui.Ymin.setText(str(format(np.min(y),'.4E')))
            self._ui.Ymax.setText(str(format(np.max(y),'.4E')))
            self._ui.NbPoint.setText(str(len(x)))
        else:
            self._ui.Xmin.setText(str(''))
            self._ui.Xmax.setText(str(''))
            self._ui.Ymin.setText(str(''))
            self._ui.Ymax.setText(str(''))
            self._ui.NbPoint.setText(str(''))
    
    def update_DW(self, MW): #add/remove curve
        self._ui.CurveChoice.clear()   
        mm = MW._figure.gca()
        for curve in mm.lines[:]:
            self._ui.CurveChoice.addItem(curve.get_label())     

    def get_ind_curve(self,liste_curve,name):
        for i in range(0,len(liste_curve)):
            if(liste_curve[i].get_label() == name):
                return i
        return -1   
    
    def remove_curve(self,MW):
        mm = MW._figure.gca()  
        ind_curve = self.get_ind_curve(mm.lines[:],self._ui.CurveChoice.currentText()) 
        mm.lines[ind_curve].remove()
        MW._figure.canvas.draw()
        self.update_DW(MW)
        self.refresh_DW(MW)
        
    def create_table(self,MW):
        WDataTable = QtWidgets.QMainWindow(self)
        Table = QtWidgets.QTableWidget()
        WDataTable.setCentralWidget(Table)
        
        mm = MW._figure.gca()
        ind_curve = self.get_ind_curve(mm.lines[:],self._ui.CurveChoice.currentText())
        x = mm.lines[ind_curve].get_xdata()
        y = mm.lines[ind_curve].get_ydata()
        
        #Row count
        Table.setRowCount(len(x)) 
  
        #Column count
        Table.setColumnCount(2)
        
        for i in range(0,len(x)):
            Table.setItem(i,0, QTableWidgetItem(str(x[i])))
            Table.setItem(i,1, QTableWidgetItem(str(y[i])))
        
        WDataTable.show()
        
        
        '''
        data = {'col1':['1','2','3','4'],
        'col2':['1','2','1','3'],
        'col3':['1','1','2','1']}
        
        table = TableView(data, 4, 3)
        table.show()
        print('Triggered !!!!!!!!!!!!!!!!!!!!!!1')
        '''
class TableView(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
 
    def setData(self): 
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)         
        

        
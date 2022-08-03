#! /usr/bin/python
#*coding: utf8 *

import sys

from matplotlib.pyplot import close

from MenuFonction_ui import *
from MainWindow import *
import numpy as np
        
def convert_format(fct):
    fct = fct.replace('x','self._x')
    fct = fct.replace('sin','np.sin')
    fct = fct.replace('cos','np.cos')
    fct = fct.replace('tan','np.tan')
    fct = fct.replace('arctan','np.arctan')
    fct = fct.replace('arcsin','np.arcsin')
    fct = fct.replace('arccos','np.arccos')
    fct = fct.replace('sqrt','np.sqrt')
    fct = fct.replace('floor','np.floor')
    return fct

class CMenuFonction(QtWidgets.QMainWindow):
    

    def __init__(self, parent=None):
        #super(CMenuFonction, self).__init__(parent=parent) #  nouvelle notation depuis python 3 : super().__init__(parent=parent)
        super().__init__(parent=parent)
        self._ui = Ui_CMenuFonction() # On peut remplacer ces deux dernieres lignes par :
        self._ui.setupUi(self)        # self.setupUi(self)
        #self.connect(self.CancelButton,QtCore.SIGNAL("clicked()"),self.calcul) #exemple pour connecter

        #ui.CancelButton.pressed.connect(self.close)
        self._ui.CancelButton.pressed.connect(lambda : self.cancel())
        self._ui.ValidateButton.pressed.connect(lambda : self.calcul())

    def cancel(self):
        self.close()

    def calcul(self):
        self._name = self._ui.Editname.text()
        self._fonction = self._ui.Editfx.text()
        self._xmin = float(self._ui.Editxmin.text())
        self._xmax = float(self._ui.Editxmax.text())
        self._NbPoint = int(self._ui.EditNbPoint.text())
        self._fonction = convert_format(self._fonction)
        self._x=np.linspace(self._xmin,self._xmax,self._NbPoint)
        self._y=eval(self._fonction)
        return self._x, self._y



    

    
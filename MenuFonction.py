#! /usr/bin/python
#*coding: utf8 *

import sys

from matplotlib.pyplot import close

from MenuFonction_ui import *

import MainWindow

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
        pass
        #self.close()
        #self._name = self._ui.EditName
        #print(self._name)


    

    
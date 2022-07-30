#! /usr/bin/python
#*coding: utf8 *

import sys

from matplotlib.pyplot import close

from MenuFonction_ui import *

import MainWindow


class CMenuFonction(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CMenuFonction, self).__init__(parent=parent) #  nouvelle notation depuis python 3 : super().__init__(parent=parent)
        ui = Ui_CMenuFonction() # On peut remplacer ces deux dernieres lignes par :
        ui.setupUi(self)        # self.setupUi(self)
        #self.connect(self.CancelButton,QtCore.SIGNAL("clicked()"),self.calcul)

        #ui.CancelButton.pressed.connect(self.close)
        ui.CancelButton.pressed.connect(lambda : calcul(self))

        print('MF _MWinstance=',MainWindow.CMainWindow._MWinstance) #test variable statique
        #print('MF _MWinstance=',parent._mdiArea) Solution          #Solution
        

def calcul(self):
    self.close()
    

    
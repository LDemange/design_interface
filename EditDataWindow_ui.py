# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditDataWindow_copy.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CEditDataWindow(object):
    def setupUi(self, CEditDataWindow):
        CEditDataWindow.setObjectName("CEditDataWindow")
        CEditDataWindow.resize(800, 365)
        self.centralwidget = QtWidgets.QWidget(CEditDataWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 10, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 761, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 40, 311, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.CurveChoice = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.CurveChoice.setMinimumSize(QtCore.QSize(150, 0))
        self.CurveChoice.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.CurveChoice.setFont(font)
        self.CurveChoice.setCurrentText("")
        self.CurveChoice.setObjectName("CurveChoice")
        self.gridLayout.addWidget(self.CurveChoice, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.DeleteButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.DeleteButton.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setObjectName("DeleteButton")
        self.gridLayout.addWidget(self.DeleteButton, 1, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 310, 761, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.RefreshButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.RefreshButton.setFont(font)
        self.RefreshButton.setObjectName("RefreshButton")
        self.horizontalLayout.addWidget(self.RefreshButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.CloseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CloseButton.setFont(font)
        self.CloseButton.setObjectName("CloseButton")
        self.horizontalLayout.addWidget(self.CloseButton)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 190, 761, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 40, 755, 61))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelYmax = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelYmax.setFont(font)
        self.labelYmax.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYmax.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYmax.setObjectName("labelYmax")
        self.gridLayout_3.addWidget(self.labelYmax, 0, 4, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setFrameShape(QtWidgets.QFrame.Box)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 0, 1, 1, 1)
        self.Ymax = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Ymax.setFont(font)
        self.Ymax.setFrameShape(QtWidgets.QFrame.Box)
        self.Ymax.setAlignment(QtCore.Qt.AlignCenter)
        self.Ymax.setObjectName("Ymax")
        self.gridLayout_3.addWidget(self.Ymax, 1, 4, 1, 1)
        self.NbPoint = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.NbPoint.setFont(font)
        self.NbPoint.setFrameShape(QtWidgets.QFrame.Box)
        self.NbPoint.setAlignment(QtCore.Qt.AlignCenter)
        self.NbPoint.setObjectName("NbPoint")
        self.gridLayout_3.addWidget(self.NbPoint, 1, 5, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_24.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setFrameShape(QtWidgets.QFrame.Box)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 0, 5, 1, 1)
        self.Xmin = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Xmin.setFont(font)
        self.Xmin.setFrameShape(QtWidgets.QFrame.Box)
        self.Xmin.setAlignment(QtCore.Qt.AlignCenter)
        self.Xmin.setObjectName("Xmin")
        self.gridLayout_3.addWidget(self.Xmin, 1, 1, 1, 1)
        self.labelYmin = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelYmin.setFont(font)
        self.labelYmin.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYmin.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYmin.setObjectName("labelYmin")
        self.gridLayout_3.addWidget(self.labelYmin, 0, 3, 1, 1)
        self.Xmax = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Xmax.setFont(font)
        self.Xmax.setFrameShape(QtWidgets.QFrame.Box)
        self.Xmax.setAlignment(QtCore.Qt.AlignCenter)
        self.Xmax.setObjectName("Xmax")
        self.gridLayout_3.addWidget(self.Xmax, 1, 2, 1, 1)
        self.Ymin = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Ymin.setFont(font)
        self.Ymin.setFrameShape(QtWidgets.QFrame.Box)
        self.Ymin.setAlignment(QtCore.Qt.AlignCenter)
        self.Ymin.setObjectName("Ymin")
        self.gridLayout_3.addWidget(self.Ymin, 1, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setFrameShape(QtWidgets.QFrame.Box)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.DataButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.DataButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.DataButton.setFont(font)
        self.DataButton.setObjectName("DataButton")
        self.gridLayout_3.addWidget(self.DataButton, 1, 0, 1, 1)
        CEditDataWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CEditDataWindow)
        self.statusbar.setObjectName("statusbar")
        CEditDataWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CEditDataWindow)
        QtCore.QMetaObject.connectSlotsByName(CEditDataWindow)

    def retranslateUi(self, CEditDataWindow):
        _translate = QtCore.QCoreApplication.translate
        CEditDataWindow.setWindowTitle(_translate("CEditDataWindow", "MainWindow"))
        self.label.setText(_translate("CEditDataWindow", "Data"))
        self.groupBox.setTitle(_translate("CEditDataWindow", "Data selection"))
        self.label_10.setText(_translate("CEditDataWindow", "Action"))
        self.label_2.setText(_translate("CEditDataWindow", "Curve"))
        self.DeleteButton.setText(_translate("CEditDataWindow", "Delete"))
        self.RefreshButton.setText(_translate("CEditDataWindow", "Refresh"))
        self.CloseButton.setText(_translate("CEditDataWindow", "Close"))
        self.groupBox_3.setTitle(_translate("CEditDataWindow", "Curve statistic"))
        self.labelYmax.setText(_translate("CEditDataWindow", "Ymax"))
        self.label_27.setText(_translate("CEditDataWindow", "Xmin"))
        self.Ymax.setText(_translate("CEditDataWindow", "10"))
        self.NbPoint.setText(_translate("CEditDataWindow", "0"))
        self.label_24.setText(_translate("CEditDataWindow", "Nb points"))
        self.Xmin.setText(_translate("CEditDataWindow", "-10"))
        self.labelYmin.setText(_translate("CEditDataWindow", "Ymin"))
        self.Xmax.setText(_translate("CEditDataWindow", "10"))
        self.Ymin.setText(_translate("CEditDataWindow", "-10"))
        self.label_17.setText(_translate("CEditDataWindow", "Xmax"))
        self.label_3.setText(_translate("CEditDataWindow", "Data"))
        self.DataButton.setText(_translate("CEditDataWindow", "Table"))

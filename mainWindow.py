# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Wed Jun 17 12:56:33 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(281, 355)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/app-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.lblHost = QtGui.QLabel(mainWindow)
        self.lblHost.setGeometry(QtCore.QRect(20, 10, 66, 17))
        self.lblHost.setObjectName("lblHost")
        self.lblPortBegin = QtGui.QLabel(mainWindow)
        self.lblPortBegin.setGeometry(QtCore.QRect(20, 50, 91, 16))
        self.lblPortBegin.setObjectName("lblPortBegin")
        self.txtHost = QtGui.QLineEdit(mainWindow)
        self.txtHost.setGeometry(QtCore.QRect(80, 10, 191, 27))
        self.txtHost.setObjectName("txtHost")
        self.txtBeginPort = QtGui.QLineEdit(mainWindow)
        self.txtBeginPort.setGeometry(QtCore.QRect(160, 50, 113, 27))
        self.txtBeginPort.setObjectName("txtBeginPort")
        self.txtLog = QtGui.QTextEdit(mainWindow)
        self.txtLog.setGeometry(QtCore.QRect(10, 130, 261, 161))
        self.txtLog.setObjectName("txtLog")
        self.lblPortEnd = QtGui.QLabel(mainWindow)
        self.lblPortEnd.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.lblPortEnd.setObjectName("lblPortEnd")
        self.txtEndPort = QtGui.QLineEdit(mainWindow)
        self.txtEndPort.setGeometry(QtCore.QRect(160, 80, 113, 27))
        self.txtEndPort.setObjectName("txtEndPort")
        self.btnScan = QtGui.QPushButton(mainWindow)
        self.btnScan.setGeometry(QtCore.QRect(207, 300, 61, 41))
        self.btnScan.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/button-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnScan.setIcon(icon1)
        self.btnScan.setIconSize(QtCore.QSize(48, 48))
        self.btnScan.setObjectName("btnScan")

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "sPS - Shadow Port Scanner", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHost.setText(QtGui.QApplication.translate("mainWindow", "Host/IP", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPortBegin.setText(QtGui.QApplication.translate("mainWindow", "Begin Port", None, QtGui.QApplication.UnicodeUTF8))
        self.txtHost.setText(QtGui.QApplication.translate("mainWindow", "Enter Host", None, QtGui.QApplication.UnicodeUTF8))
        self.txtBeginPort.setText(QtGui.QApplication.translate("mainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPortEnd.setText(QtGui.QApplication.translate("mainWindow", "Ending Port", None, QtGui.QApplication.UnicodeUTF8))
        self.txtEndPort.setText(QtGui.QApplication.translate("mainWindow", "1024", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc

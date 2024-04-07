# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cam.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_cam = QtWidgets.QFrame(self.centralwidget)
        self.frame_cam.setGeometry(QtCore.QRect(260, 90, 241, 331))
        self.frame_cam.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cam.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cam.setObjectName("frame_cam")
        self.cam = QtWidgets.QLabel(self.frame_cam)
        self.cam.setGeometry(QtCore.QRect(90, 90, 101, 111))
        self.cam.setObjectName("cam")
        self.cam.se
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cam.setText(_translate("MainWindow", "TextLabel"))


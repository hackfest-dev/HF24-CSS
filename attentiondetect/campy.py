# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cam.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Start the camera capture
        self.cap = cv2.VideoCapture(0)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update frame every 30 milliseconds

    def update_frame(self):
        ret, frame = self.cap.read()  # Read frame from the camera

        if ret:
            # Convert frame to RGB format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Create QImage from the frame
            image = QImage(frame_rgb, frame_rgb.shape[1], frame_rgb.shape[0], QImage.Format_RGB888)

            # Create QPixmap from the QImage
            pixmap = QPixmap.fromImage(image)

            # Scale the pixmap to fit the size of Frame_cam
            pixmap = pixmap.scaled(self.ui.Frame_cam.width(), self.ui.Frame_cam.height(), QtCore.Qt.KeepAspectRatio)

            # Set the pixmap on a QLabel widget within Frame_cam
            self.ui.cam.setPixmap(pixmap)

    def closeEvent(self, event):
        # Stop the camera capture and release the camera
        self.timer.stop()
        self.cap.release()
        super(MainWindow, self).closeEvent(event)



    def button_clicked(self):
        print("Button clicked")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Frame_web = QtWidgets.QFrame(self.centralwidget)
        self.Frame_web.setGeometry(QtCore.QRect(20, 80, 331, 391))
        self.Frame_web.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_web.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_web.setObjectName("Frame_web")
        self.pushButton = QtWidgets.QPushButton(self.Frame_web)
        self.pushButton.setGeometry(QtCore.QRect(110, 120, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.Frame_cam = QtWidgets.QFrame(self.centralwidget)
        self.Frame_cam.setGeometry(QtCore.QRect(400, 70, 321, 411))
        self.Frame_cam.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_cam.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_cam.setObjectName("Frame_cam")
        self.cam = QtWidgets.QLabel(self.Frame_cam)
        
        self.cam.setGeometry(QtCore.QRect(90, 90, 321, 411))
        self.cam.setObjectName("cam")
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
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
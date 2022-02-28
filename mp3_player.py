# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mp3_player.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(50, 350, 75, 23))
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(125, 350, 75, 23))
        self.removeButton.setObjectName("removeButton")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(200, 350, 75, 23))
        self.playButton.setObjectName("playButton")
        self.playlist = QtWidgets.QListWidget(self.centralwidget)
        self.playlist.setGeometry(QtCore.QRect(50, 50, 300, 300))
        self.playlist.setObjectName("playlist")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(275, 350, 75, 23))
        self.pauseButton.setObjectName("pauseButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionClear_Playlist = QtWidgets.QAction(MainWindow)
        self.actionClear_Playlist.setToolTip("Clear Playlist")
        self.actionClear_Playlist.setObjectName("actionClear_Playlist")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.actionClear_Playlist.setText(_translate("MainWindow", "Clear Playlist"))
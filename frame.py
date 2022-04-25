# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import youtube
from PyQt5 import QtCore, QtGui, QtWidgets
from mhyt import yt_download


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 392)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_download = QtWidgets.QPushButton(self.centralwidget)
        self.bt_download.setGeometry(QtCore.QRect(330, 250, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bt_download.setFont(font)
        self.bt_download.setObjectName("bt_download")
        self.link = QtWidgets.QLabel(self.centralwidget)
        self.link.setGeometry(QtCore.QRect(30, 150, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.link.setFont(font)
        self.link.setObjectName("link")
        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(20, 200, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Titulo.setFont(font)
        self.Titulo.setObjectName("Titulo")
        self.txt_link = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_link.setGeometry(QtCore.QRect(70, 150, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_link.setFont(font)
        self.txt_link.setText("")
        self.txt_link.setObjectName("txt_link")
        self.txt_titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_titulo.setGeometry(QtCore.QRect(70, 200, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_titulo.setFont(font)
        self.txt_titulo.setObjectName("txt_titulo")
        self.Downloader = QtWidgets.QLabel(self.centralwidget)
        self.Downloader.setGeometry(QtCore.QRect(240, 50, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Seagram tfb")
        font.setPointSize(24)
        self.Downloader.setFont(font)
        self.Downloader.setObjectName("Downloader")
        self.img_yt = QtWidgets.QLabel(self.centralwidget)
        self.img_yt.setGeometry(QtCore.QRect(80, 0, 161, 141))
        self.img_yt.setObjectName("img_yt")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 241, 57, 54))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_mp3 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_mp3.setFont(font)
        self.rb_mp3.setChecked(True)
        self.rb_mp3.setObjectName("rb_mp3")
        self.verticalLayout.addWidget(self.rb_mp3)
        self.rb_mp4 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_mp4.setFont(font)
        self.rb_mp4.setObjectName("rb_mp4")
        self.verticalLayout.addWidget(self.rb_mp4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Função do Botaão de download

        self.bt_download.clicked.connect(self.download)

    def download(self):

        # Download do arquivo em Mp4
        if self.rb_mp4.isCheckable() == True:
            url = self.txt_link.text()
            titulo = self.txt_titulo.text()
            titulo_mp4 = titulo+'.mp4'
            yt_download(url, titulo_mp4)

        # Download do arquivo em Mp3
        elif self.rb_mp3.isCheckable() == True:
            url = self.txt_link.text()
            titulo = self.txt_titulo.text()
            titulo_mp3 = titulo+'.mp3'
            yt_download(url, titulo_mp3, ismusic=True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_download.setText(_translate("MainWindow", "Download"))
        self.link.setText(_translate("MainWindow", "Link:"))
        self.Titulo.setText(_translate("MainWindow", "Titulo:"))
        self.Downloader.setText(_translate("MainWindow", "Downloader"))
        self.img_yt.setText(_translate(
            "MainWindow", "<html><head/><body><p><img src=\":/youtube/YouTube.png\"/></p></body></html>"))
        self.rb_mp3.setText(_translate("MainWindow", "mp3"))
        self.rb_mp4.setText(_translate("MainWindow", "mp4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crayui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_crayui(object):
    def setupUi(self, crayui):
        crayui.setObjectName("crayui")
        crayui.resize(542, 546)
        self.centralwidget = QtWidgets.QWidget(crayui)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 541, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("x.gif"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 131, 41))
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:#bfff33;\n"
"font-size:22px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 480, 111, 61))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:#bfff33;\n"
"font-size:25px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 500, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 500, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"background-color: rgb(170, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        crayui.setCentralWidget(self.centralwidget)

        self.retranslateUi(crayui)
        QtCore.QMetaObject.connectSlotsByName(crayui)

    def retranslateUi(self, crayui):
        _translate = QtCore.QCoreApplication.translate
        crayui.setWindowTitle(_translate("crayui", "MainWindow"))
        self.pushButton.setText(_translate("crayui", "Run"))
        self.pushButton_2.setText(_translate("crayui", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    crayui = QtWidgets.QMainWindow()
    ui = Ui_crayui()
    ui.setupUi(crayui)
    crayui.show()
    sys.exit(app.exec_())

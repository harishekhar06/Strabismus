# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logpage1.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(450, 550)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(49, 29, 370, 480))
        self.widget.setStyleSheet(u"QPushButton#pushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255,255,255210);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"}\n"
"QPushButton#pushButton_2{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color: rgb(204, 204, 204);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
""
                        "	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"}\n"
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 300, 420))
        self.label.setStyleSheet(u"border-radius:20px;\n"
"background-image: url(:/icons/bgl2.png);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 50, 90, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:rgba(255,255,255,210);")
        self.username = QLineEdit(self.widget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(70, 170, 200, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.username.setFont(font1)
        self.username.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;\n"
"")
        self.password = QLineEdit(self.widget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(70, 220, 200, 40))
        self.password.setFont(font1)
        self.password.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;\n"
"")
        self.password.setEchoMode(QLineEdit.Password)
        self.loginBtn = QPushButton(self.widget)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(70, 280, 200, 40))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.loginBtn.setFont(font2)
        self.loginBtn.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255,255,255,210);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 320, 131, 31))
        font3 = QFont()
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.signupBtn = QPushButton(self.widget)
        self.signupBtn.setObjectName(u"signupBtn")
        self.signupBtn.setGeometry(QRect(70, 350, 201, 41))
        self.signupBtn.setFont(font2)
        self.signupBtn.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255,255,255,210);")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 90, 101, 81))
        font4 = QFont()
        font4.setPointSize(48)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(204, 204, 204);\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"LOGIN", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Dialog", u"USER NAME", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Dialog", u"PASSWORD", None))
        self.loginBtn.setText(QCoreApplication.translate("Dialog", u"LOG IN", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"New User?", None))
        self.signupBtn.setText(QCoreApplication.translate("Dialog", u"SIGN UP", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\ue77b", None))
    # retranslateUi


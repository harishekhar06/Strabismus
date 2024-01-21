# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regis.ui'
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


class Ui_Dia(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(450, 516)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(49, 29, 370, 480))
        self.widget.setStyleSheet(u"QPushButton#pushButton,#pushButton_6{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color: rgb(204, 204, 204);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover, #pushBitton_6:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton:pressed,  #pushBitton_6:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 300, 420))
        self.label.setStyleSheet(u"background-image: url(:/icons/bgl2.png);\n"
"border-radius:20px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 70, 121, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:rgba(255,255,255,210);")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 250, 200, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 290, 200, 40))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 350, 200, 40))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(80, 200, 200, 40))
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(80, 150, 91, 31))
        self.lineEdit_4.setFont(font1)
        self.lineEdit_4.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(190, 150, 91, 31))
        self.lineEdit_5.setFont(font1)
        self.lineEdit_5.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"REGISTER", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"PASSWORD", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"CONFIRM PASSWORD", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"REGISTER", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"E-MAIL ADDRESS", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Dialog", u"FIRST NAME", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Dialog", u"LAST NAME", None))
    # retranslateUi


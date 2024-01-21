# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginpgvudNHR.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QToolButton, QWidget)
import iconic_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #1f232a;\n"
"color:rgba(255,255,255,210);\n"
"QPushButton#pushButton{\n"
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
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, "
                        "118, 132, 226));\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius:20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton#pushButton{\n"
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
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 10, 241, 20))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.toolButton = QToolButton(self.frame_2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(210, 0, 101, 41))
        self.toolButton.setStyleSheet(u"background:transparent;")
        icon = QIcon()
        icon.addFile(u":/icon/feather (1)/Strab-ist_bgrem.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(50, 50))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 70, 71, 81))
        font1 = QFont()
        font1.setPointSize(48)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(204, 204, 204);\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 150, 90, 40))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color:rgba(255,255,255,210);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.username = QLineEdit(self.frame_2)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(170, 230, 451, 31))
        font3 = QFont()
        font3.setPointSize(10)
        self.username.setFont(font3)
        self.username.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;\n"
"")
        self.passWord = QLineEdit(self.frame_2)
        self.passWord.setObjectName(u"passWord")
        self.passWord.setGeometry(QRect(170, 290, 451, 31))
        self.passWord.setFont(font3)
        self.passWord.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;\n"
"")
        self.passWord.setEchoMode(QLineEdit.Password)
        self.logg = QPushButton(self.frame_2)
        self.logg.setObjectName(u"logg")
        self.logg.setGeometry(QRect(280, 350, 200, 40))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.logg.setFont(font4)
        self.logg.setStyleSheet(u"QPushButton#logg{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color: rgb(204, 204, 204);\n"
"border-radius:20px;;\n"
"}\n"
"QPushButton#logg:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#logg:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"}\n"
"")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 400, 131, 31))
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.signin = QPushButton(self.frame_2)
        self.signin.setObjectName(u"signin")
        self.signin.setGeometry(QRect(280, 440, 201, 41))
        self.signin.setFont(font4)
        self.signin.setStyleSheet(u"QPushButton#signin{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color: rgb(204, 204, 204);\n"
"border-radius:20px;;\n"
"}\n"
"QPushButton#signin:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#signin:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"}\n"
"")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(540, 280, 75, 24))
        self.pushButton.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setIconSize(QSize(24, 24))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)

        self.horizontalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"STRABIS-T", None))
        self.toolButton.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ue77b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-MAIL ADDRESS", None))
        self.passWord.setText("")
        self.passWord.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        self.logg.setText(QCoreApplication.translate("MainWindow", u"LOG IN", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"New User?", None))
        self.signin.setText(QCoreApplication.translate("MainWindow", u"SIGN UP", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Show", None))
    # retranslateUi


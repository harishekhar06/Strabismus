# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImagecollectzDJZnx.ui'
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
import resources_1_rc

class Ui_ImageWindow(object):
    def setupUi(self, ImageWindow):
        if not ImageWindow.objectName():
            ImageWindow.setObjectName(u"ImageWindow")
        ImageWindow.resize(870, 563)
        self.centralwidget = QWidget(ImageWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #1f232a;\n"
"color:rgba(255,255,255,210);\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius:20px;\n"
"QPushButton#pushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 290, 491, 81))
        self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
"	background-color: transparent;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icon/feather (1)/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(230, 390, 301, 41))
        self.pushButton_2.setStyleSheet(u"QPushButton#pushButton_2{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color: rgb(204, 204, 204);\n"
"border-radius:20px;;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"}\n"
"")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 230, 491, 31))
        self.lineEdit.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(130, 150, 491, 31))
        self.lineEdit_2.setAcceptDrops(True)
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.lineEdit_2.setEchoMode(QLineEdit.Normal)
        self.lineEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_2.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(29, 10, 741, 51))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 10, 241, 20))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.toolButton = QToolButton(self.frame_2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(200, 0, 101, 41))
        self.toolButton.setStyleSheet(u"background:transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/icon/feather (1)/Strab-ist_bgrem.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QSize(50, 50))
        self.backBtn = QPushButton(self.frame_2)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(20, 10, 75, 24))
        font1 = QFont()
        font1.setBold(True)
        self.backBtn.setFont(font1)
        self.backBtn.setStyleSheet(u"QPushButton#backBtn{\n"
"background:transparent;\n"
"border-radius:20px;;\n"
"}\n"
"QPushButton#backBtn:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#backBtn:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"}\n"
"")
        self.backBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.frame)

        ImageWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ImageWindow)

        QMetaObject.connectSlotsByName(ImageWindow)
    # setupUi

    def retranslateUi(self, ImageWindow):
        ImageWindow.setWindowTitle(QCoreApplication.translate("ImageWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("ImageWindow", u"SELECT IMAGE", None))
        self.pushButton_2.setText(QCoreApplication.translate("ImageWindow", u"ANALYZE", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ImageWindow", u"AGE", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("ImageWindow", u"NAME OF THE PATIENT", None))
        self.label.setText(QCoreApplication.translate("ImageWindow", u"STRABIS-T", None))
        self.toolButton.setText("")
        self.backBtn.setText(QCoreApplication.translate("ImageWindow", u"\ue72b", None))
    # retranslateUi


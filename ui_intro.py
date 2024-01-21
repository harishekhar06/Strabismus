# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'introJFVDVQ.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import iconic_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(800, 600)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0,0,0);\n"
"	color: rgb(220, 220, 220);\n"
"   border-radius:10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadow = QFrame(self.centralwidget)
        self.dropShadow.setObjectName(u"dropShadow")
        self.dropShadow.setStyleSheet(u"")
        self.dropShadow.setFrameShape(QFrame.StyledPanel)
        self.dropShadow.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.dropShadow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(8, 200, 761, 71))
        font = QFont()
        font.setPointSize(30)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.dropShadow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 260, 771, 31))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(197, 255, 8);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadow)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(70, 360, 651, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(98, 114, 164); 	\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align:center;\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius:10px;\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:0.977273, y2:0.579545, stop:0 rgba(83, 162, 18, 255), stop:1 rgba(190, 255, 10, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_3 = QLabel(self.dropShadow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 400, 771, 31))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(201, 255, 23);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.dropShadow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 110, 311, 91))
        self.pushButton.setStyleSheet(u"color: rgb(35, 0, 104);\n"
"border:transparent;\n"
"background:transparent;\n"
"")
        icon = QIcon()
        icon.addFile(u"Strabist.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(200, 200))

        self.verticalLayout.addWidget(self.dropShadow)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SplashScreen", u"<strong>STRABIS-T</strong>", None))
        self.label_2.setText(QCoreApplication.translate("SplashScreen", u"COOL AS <strong>EYES</strong>", None))
        self.label_3.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p>loading...</p><p><br/></p></body></html>", None))
        self.pushButton.setText("")
    # retranslateUi


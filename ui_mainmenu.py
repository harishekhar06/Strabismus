# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainmenuuEpcbN.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)
import iconic_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 600)
        MainWindow.setStyleSheet(u"*{\n"
"border: none;\n"
"background-color: transaprent;\n"
"background: transparent;\n"
"padding: 0;\n"
"margin:0;\n"
"color:#fff;\n"
"}\n"
"#centrawidget{\n"
"background-color: #1f232a;\n"
"}\n"
"leftMenuSubContainer{\n"
"background-color: #16191d;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"text-allign: left;\n"
"padding: 5px 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer{\n"
"background-color: #2c313c;\n"
"}\n"
"#frame_4{\n"
"background-color: #16191d;\n"
"border-radius: 10px;\n"
"}\n"
"#headerContainer{\n"
"background-color: #16191d;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, -1)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.menuBtn = QPushButton(self.leftMenuSubContainer)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setStyleSheet(u"QPushButton#menuBtn{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color: rgb(204, 204, 204);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#menuBtn:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#menuBtn:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icon/feather (1)/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.menuBtn)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.homeBtn = QPushButton(self.leftMenuSubContainer)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setStyleSheet(u"QPushButton#homeBtn{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color: rgb(204, 204, 204);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#homeBtn:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#homeBtn:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/feather (1)/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.homeBtn)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.fileBtn = QPushButton(self.frame_2)
        self.fileBtn.setObjectName(u"fileBtn")
        self.fileBtn.setStyleSheet(u"QPushButton#fileBtn{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color: rgb(204, 204, 204);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#fileBtn:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#fileBtn:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fileBtn.setIcon(icon2)
        self.fileBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.fileBtn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.camBtn = QPushButton(self.leftMenuSubContainer)
        self.camBtn.setObjectName(u"camBtn")
        self.camBtn.setStyleSheet(u"QPushButton#camBtn{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color: rgb(204, 204, 204);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#camBtn:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#camBtn:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105,118,132,200);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.camBtn.setIcon(icon3)
        self.camBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.camBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QWidget(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.verticalLayout_6 = QVBoxLayout(self.headerContainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, -1, 0)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/icon/feather (1)/Strab-ist_bgrem.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.toolButton_3 = QToolButton(self.frame_7)
        self.toolButton_3.setObjectName(u"toolButton_3")
        icon4 = QIcon()
        icon4.addFile(u":/icon/feather (1)/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_3.setIcon(icon4)
        self.toolButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.toolButton_3)

        self.toolButton_2 = QToolButton(self.frame_7)
        self.toolButton_2.setObjectName(u"toolButton_2")
        icon5 = QIcon()
        icon5.addFile(u":/icon/feather (1)/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon5)
        self.toolButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.toolButton_2)

        self.toolButton = QToolButton(self.frame_7)
        self.toolButton.setObjectName(u"toolButton")
        icon6 = QIcon()
        icon6.addFile(u":/icon/feather (1)/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon6)
        self.toolButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.toolButton)


        self.verticalLayout_6.addWidget(self.frame_7)


        self.verticalLayout_9.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.mainBodyContent.setStyleSheet(u"background-color: #1f232a;")

        self.verticalLayout_9.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
#if QT_CONFIG(tooltip)
        self.fileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Access Image", None))
#endif // QT_CONFIG(tooltip)
        self.fileBtn.setText(QCoreApplication.translate("MainWindow", u"Access Images", None))
#if QT_CONFIG(tooltip)
        self.camBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Open Camera", None))
#endif // QT_CONFIG(tooltip)
        self.camBtn.setText(QCoreApplication.translate("MainWindow", u" Open Camera", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"STRABIS-T", None))
        self.toolButton_3.setText("")
        self.toolButton_2.setText("")
        self.toolButton.setText("")
    # retranslateUi


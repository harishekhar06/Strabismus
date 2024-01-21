from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)
import iconic_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(907, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bg = QFrame(self.centralwidget)
        self.bg.setObjectName(u"bg")
        self.bg.setStyleSheet(u"#bg{\n"
"background-color:rgb(19, 19, 19);\n"
"}")
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.bg)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.bg)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 28))
        self.header.setStyleSheet(u"*{\n"
"color: rgb(255,255,255);\n"
"background: black;\n"
"border:none;\n"
"}\n"
"#QPushButton{\n"
"color: rgb(255,255,255);\n"
"background: transparent;\n"
"border:none;\n"
"}\n"
"#QPushButton-hover{\n"
"background: white;\n"
"border:none;\n"
"}\n"
"")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 2, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icon/feather (1)/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/icon/feather (1)/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/icon/feather (1)/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.main = QFrame(self.bg)
        self.main.setObjectName(u"main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy1)
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.main)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 0, 150, 531))
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setStyleSheet(u"background-color:rgb(10,10,10);\n"
"color:rgb(255, 255, 255);\n"
"border:none;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.toolButton = QToolButton(self.frame_4)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(5, 5, 100, 27))
        icon3 = QIcon()
        icon3.addFile(u":/icon/feather (1)/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon3)
        self.toolButton.setIconSize(QSize(24, 24))
        self.toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_2 = QToolButton(self.frame_4)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(0, 90, 141, 27))
        icon4 = QIcon()
        icon4.addFile(u":/icon/feather (1)/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon4)
        self.toolButton_2.setIconSize(QSize(24, 24))
        self.toolButton_2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_3 = QToolButton(self.frame_4)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setGeometry(QRect(0, 140, 150, 27))
        icon5 = QIcon()
        icon5.addFile(u":/icon/feather (1)/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_3.setIcon(icon5)
        self.toolButton_3.setIconSize(QSize(24, 24))
        self.toolButton_3.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_4 = QToolButton(self.frame_4)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setGeometry(QRect(0, 190, 141, 27))
        icon6 = QIcon()
        icon6.addFile(u":/icon/feather (1)/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon6)
        self.toolButton_4.setIconSize(QSize(24, 24))
        self.toolButton_4.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_5 = QToolButton(self.frame_4)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setGeometry(QRect(0, 240, 141, 27))
        icon7 = QIcon()
        icon7.addFile(u":/icon/feather (1)/eye.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_5.setIcon(icon7)
        self.toolButton_5.setIconSize(QSize(24, 24))
        self.toolButton_5.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_6 = QToolButton(self.frame_4)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setGeometry(QRect(0, 290, 151, 27))
        icon8 = QIcon()
        icon8.addFile(u":/icon/feather (1)/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_6.setIcon(icon8)
        self.toolButton_6.setIconSize(QSize(24, 24))
        self.toolButton_6.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.frame_5 = QFrame(self.main)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(50, 0, 741, 541))
        self.frame_5.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 190, 281, 41))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_5.raise_()
        self.frame_4.raise_()

        self.verticalLayout.addWidget(self.main)

        self.footer = QFrame(self.bg)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 25))
        self.footer.setMaximumSize(QSize(16777215, 25))
        self.footer.setStyleSheet(u"background-color:rgb(0, 0, 0);")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.bg)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Squin-T", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"    PROFILE", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"   INPUT IMAGE", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"   CAPTURE", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"   CHECK", None))
        self.toolButton_6.setText(QCoreApplication.translate("MainWindow", u"   REPORT", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"COOL AS EYES", None))
    # retranslateUi


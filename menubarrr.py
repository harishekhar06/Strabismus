from PyQt5 import QtWidgets, uic, QtCore,QtGui
import sys


class Main_UI(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("menubar_1.ui", self)

        QtCore.QResource.registerResource("C:/Users/alhar/Desktop/Project/strabismus/Strabismus-Detection-Mediapipe-main/iconic.qrc")
        icon = QtGui.QIcon()
        icon.addFile(u":/icon/feather (1)/printer.svg")

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton_3.clicked.connect(lambda: MainApp.exit())
        self.pushButton.clicked.connect(lambda: self.showMinimized())
        self.pushButton_2.clicked.connect(lambda: self.showMaximized())
        self.Side_Menu_Num = 0
        self.toolButton.clicked.connect(lambda: self.Side_Menu_Def_0())
        self.frame_5.mousePressEvent = self.Side_Menu_Def_1
        self.show()
    def Side_Menu_Def_0(self):
        if self.Side_Menu_Num == 0:
            self.animation1 = QtCore.QPropertyAnimation(self.frame_4, b"maximimumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(40)
            self.animation1.setEndValue(150)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()

            self.animation2 = QtCore.QPropertyAnimation(self.frame_4, b"minimumWidth")
            self.animation2.setDuration(500)
            self.animation2.setStartValue(40)
            self.animation2.setEndValue(150)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()
            self.Side_Menu_Num = 1
        else:
            self.animation1 = QtCore.QPropertyAnimation(self.frame_4, b"maximimumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(150)
            self.animation1.setEndValue(40)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()

            self.animation2 = QtCore.QPropertyAnimation(self.frame_4, b"minimumWidth")
            self.animation2.setDuration(500)
            self.animation2.setStartValue(150)
            self.animation2.setEndValue(40)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()
            self.Side_Menu_Num = 0

    def Side_Menu_Def_1(self, Event):
        if Event.button() == QtCore.Qt.LeftButton:
            if self.Side_Menu_Num == 1:
                self.animation1 = QtCore.QPropertyAnimation(self.frame_4, b"maximimumWidth")
                self.animation1.setDuration(500)
                self.animation1.setStartValue(150)
                self.animation1.setEndValue(40)
                self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.animation1.start()

                self.animation2 = QtCore.QPropertyAnimation(self.frame_4, b"minimumWidth")
                self.animation2.setDuration(500)
                self.animation2.setStartValue(150)
                self.animation2.setEndValue(40)
                self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.animation2.start()
                self.Side_Menu_Num = 0
            else:
                pass
        self.frame_2.mouseMoveEvent = self.MoveWindow

    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
if __name__ == "__main__":
    MainApp = QtWidgets.QApplication(sys.argv)
    window = Main_UI()
    sys.exit(MainApp.exec())
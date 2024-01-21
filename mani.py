import sys

from PySide6.QtGui import QColor, QPixmap, QImage
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow, QProgressBar, QPushButton, QSizePolicy,
                               QWidget, QGraphicsDropShadowEffect, QFileDialog)
from logpage import Ui_Dialog
from ui_menubar_1 import Ui_MainWindow
from regis import Ui_Dia
from activities import on_camera

class LoginScreen(QMainWindow) :
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        image = QImage("bgl2.png")
        image_resized = image.scaled (self.ui.label.width (), self.ui.label.height ())
        pixmap = QPixmap.fromImage (image_resized)
        self.ui.label.setPixmap (pixmap)
        self.show ()

        self.ui.loginBtn.clicked.connect(self.on_login)
        self.ui.signupBtn.clicked.connect(self.on_signup)


    def on_login(self):
        self.login = MainScreen()
        self.login.show()
        self.close()

    def on_signup(self) :
        self.signup = SignupScreen()
        self.signup.show()
        self.close()
class SignupScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Dia()
        self.ui.setupUi(self)
        image = QImage ("bgl2.png")
        image_resized = image.scaled (self.ui.label.width (), self.ui.label.height ())
        pixmap = QPixmap.fromImage (image_resized)
        self.ui.label.setPixmap (pixmap)
        self.ui.pushButton.clicked.connect(self.on_register)

    def on_register(self) :
        self.register = LoginScreen()
        self.register.show()
        self.close()
class MainScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def camaccess(self):
        on_camera()

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp *jpeg)", options=options)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginScreen()
    sys.exit(app.exec())

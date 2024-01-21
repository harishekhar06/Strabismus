import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt, QTimer
app = QApplication(sys.argv)
lbl = QLabel('<font color=Black size=12> <b> Strab-is? </b> </font>')
lbl.setWindowFlags(Qt.Splashscreen | Qt.FramelessWindowHint)
lbl.show()
QTimer.singleShot(000, app.quit)
sys.exit(app.exec_())
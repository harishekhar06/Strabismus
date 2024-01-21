#import sys

#from PyQt5.QtWidgets import QMainWindow, QApplication,QTextEdit,QFileDialog
#from PyQt5 import uic
#from PyQt5.QtGui import QPixmap
#class UI(QMainWindow):
 #   def __init__(self):
  #      super(UI,self).__init__()

#        uic.loadUi("patient_report.ui",self)
 #       self.show()
   # def imge(self):
    #    fname= QFileDialog.getOpenFileName(self,"C:/Users/alhar/Desktop/Project/strabismus/Strabismus-Detection-Mediapipe-main/Images")
     #   self.pixmap = QPixmap(fname[0])
      #  self.label.setPixmap(self.pixmap)
#app = QApplication(sys.argv)
#UIWindow = UI()
#app.exec_()

from PyQt5 import QtWidgets, QtPrintSupport
from PyQt5 import uic
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QBuffer
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('my_ui_file.ui', self)

app = QtWidgets.QApplication([])
form = uic.loadUi('patient_report.ui')

printer = QtPrintSupport.QPrinter()
painter = QPainter()
painter.begin(printer)

buffer = QBuffer()
buffer.open(QBuffer.ReadWrite)
form.render(painter)
form.render(buffer)
painter.end()

pdf_canvas = canvas.Canvas('output.pdf', pagesize=letter)
pdf_canvas.drawImage(ImageReader(buffer.data()), 0, 0)
pdf_canvas.save()

buffer.close()
app.quit()


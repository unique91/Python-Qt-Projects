import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(300, 300, 400, 600)
        self.setWindowTitle('Basic math Calculator')
        self.initUI()
    
    def initUI(self):        
        self.label = QtWidgets.QLabel(self)
        self.label.setText("This is a label")
        self.label.move(50, 50)
        
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Click me")
        self.btn.clicked.connect(self.clicked)
    
    def clicked(self):
        self.label.setText("I pressed the button annsdfo sdfod")
        self.update()
    
    def update(self):
        self.label.adjustSize()
        

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
    
window()
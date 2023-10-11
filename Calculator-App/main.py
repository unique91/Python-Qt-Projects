from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(300, 300, 400, 600)
    win.setWindowTitle('Basic math Calculator')
    
    label = QtWidgets.QLabel(win)
    label.setText('This is a lable!')
    label.move(50, 50)
    
    win.show()
    sys.exit(app.exec_())
    

window()
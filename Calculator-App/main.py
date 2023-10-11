from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

num1 = int(input('Input 1st number: '))
num2 = int(input('Input 2st number: '))
operator = input('Input an operator (+, -, *, /): ')

res = 0
if operator == '+':
    res = num1 + num2
elif operator == '-':
    res = num1 - num2
elif operator == '*':
    res = num1 * num2
elif operator == '/':
    res = num1 / num2
else:
    print(f"{operator} is not a valid operator!")

print('(%d %s %d) = %d' % (num1, operator, num2, res))

'''def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(300, 300, 400, 600)
    win.setWindowTitle('Basic math Calculator')
    q
    label = QtWidgets.QLabel(win)
    label.setText('This is a lable!')
    label.move(50, 50)
    win.show()
    sys.exit(app.exec_())
    

window()'''

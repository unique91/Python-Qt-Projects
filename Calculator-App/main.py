'''
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
'''
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import win32api

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        MainWindow.setStyleSheet("background-color:rgb(229, 229, 229)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_number0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_number0.sizePolicy().hasHeightForWidth())
        self.btn_number0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_number0.setFont(font)
        self.btn_number0.setObjectName("btn_number0")
        self.gridLayout.addWidget(self.btn_number0, 5, 1, 1, 1)
        self.btn_number5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_number5.sizePolicy().hasHeightForWidth())
        self.btn_number5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_number5.setFont(font)
        self.btn_number5.setObjectName("btn_number5")
        self.gridLayout.addWidget(self.btn_number5, 3, 1, 1, 1)
        self.btn_number1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_number1.sizePolicy().hasHeightForWidth())
        self.btn_number1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_number1.setFont(font)
        self.btn_number1.setObjectName("btn_number1")
        self.gridLayout.addWidget(self.btn_number1, 4, 0, 1, 1)
        self.btn_multiplication = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_multiplication.sizePolicy().hasHeightForWidth())
        self.btn_multiplication.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_multiplication.setFont(font)
        self.btn_multiplication.setObjectName("btn_multiplication")
        self.gridLayout.addWidget(self.btn_multiplication, 2, 3, 1, 1)
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet(
"QPushButton:hover {\n"
"    background-color:rgb(50, 110, 255);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(85, 170, 255);\n"
"}")
        self.btn_equal.setObjectName("btn_equal")
        self.gridLayout.addWidget(self.btn_equal, 5, 3, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout.addWidget(self.btn_plus, 4, 3, 1, 1)
        self.btn_neg_pos = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_neg_pos.sizePolicy().hasHeightForWidth())
        self.btn_neg_pos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_neg_pos.setFont(font)
        self.btn_neg_pos.setObjectName("btn_neg_pos")
        self.gridLayout.addWidget(self.btn_neg_pos, 5, 0, 1, 1)
        self.lb_output = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.lb_output.sizePolicy().hasHeightForWidth())
        self.lb_output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(42)
        font.setBold(False)
        self.lb_output.setFont(font)
        self.lb_output.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_output.setWordWrap(False)
        self.lb_output.setObjectName("lb_output")
        self.gridLayout.addWidget(self.lb_output, 0, 0, 1, 4)
        self.btn_number9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_number9.sizePolicy().hasHeightForWidth())
        self.btn_number9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_number9.setFont(font)
        self.btn_number9.setObjectName("btn_number9")
        self.gridLayout.addWidget(self.btn_number9, 2, 2, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_minus.setFont(font)
        self.btn_minus.setObjectName("btn_minus")
        self.gridLayout.addWidget(self.btn_minus, 3, 3, 1, 1)
        self.btn_number7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_number7.sizePolicy().hasHeightForWidth())
        self.btn_number7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_number7.setFont(font)
        self.btn_number7.setObjectName("btn_number7")
        self.gridLayout.addWidget(self.btn_number7, 2, 0, 1, 1)
        self.btn_number8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_number8.sizePolicy().hasHeightForWidth())
        self.btn_number8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_number8.setFont(font)
        self.btn_number8.setObjectName("btn_number8")
        self.gridLayout.addWidget(self.btn_number8, 2, 1, 1, 1)
        self.btn_number4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_number4.sizePolicy().hasHeightForWidth())
        self.btn_number4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_number4.setFont(font)
        self.btn_number4.setObjectName("btn_number4")
        self.gridLayout.addWidget(self.btn_number4, 3, 0, 1, 1)
        self.btn_number6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_number6.sizePolicy().hasHeightForWidth())
        self.btn_number6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_number6.setFont(font)
        self.btn_number6.setObjectName("btn_number6")
        self.gridLayout.addWidget(self.btn_number6, 3, 2, 1, 1)
        self.btn_number2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_number2.sizePolicy().hasHeightForWidth())
        self.btn_number2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_number2.setFont(font)
        self.btn_number2.setObjectName("btn_number2")
        self.gridLayout.addWidget(self.btn_number2, 4, 1, 1, 1)
        self.btn_number3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_number3.sizePolicy().hasHeightForWidth())
        self.btn_number3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_number3.setFont(font)
        self.btn_number3.setObjectName("btn_number3")
        self.gridLayout.addWidget(self.btn_number3, 4, 2, 1, 1)
        self.btn_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_point.setFont(font)
        self.btn_point.setObjectName("btn_point")
        self.gridLayout.addWidget(self.btn_point, 5, 2, 1, 1)
        self.btn_modular = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_modular.sizePolicy().hasHeightForWidth())
        self.btn_modular.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_modular.setFont(font)
        self.btn_modular.setObjectName("btn_modular")
        self.gridLayout.addWidget(self.btn_modular, 1, 0, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout.addWidget(self.btn_cancel, 1, 1, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 1, 2, 1, 1)
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btn_divide.sizePolicy().hasHeightForWidth())
        self.btn_divide.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        self.btn_divide.setFont(font)
        self.btn_divide.setObjectName("btn_divide")
        self.gridLayout.addWidget(self.btn_divide, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        a = win32api.GetKeyState(0x01)
        if a < 0:
            print('left button pressed')
            
        self.btn_number0.clicked.connect(self.number0_output)
        self.btn_number1.clicked.connect(self.number1_output)
        self.btn_number2.clicked.connect(self.number2_output)
        self.btn_number3.clicked.connect(self.number3_output)
        self.btn_number4.clicked.connect(self.number4_output)
        self.btn_number5.clicked.connect(self.number5_output)
        self.btn_number6.clicked.connect(self.number6_output)
        self.btn_number7.clicked.connect(self.number7_output)
        self.btn_number8.clicked.connect(self.number8_output)
        self.btn_number9.clicked.connect(self.number9_output)
        self.btn_clear.clicked.connect(self.clear_output)
        self.btn_cancel.clicked.connect(self.cancel_output)
        self.btn_plus.clicked.connect(self.add_output)
        self.btn_minus.clicked.connect(self.sub_output)
        self.btn_multiplication.clicked.connect(self.mult_output)
        self.btn_divide.clicked.connect(self.div_output)
        self.btn_equal.clicked.connect(self.result_output)
        
    def number0_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt + "0")
    
    def number1_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt + "1")
    
    def number2_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt + "2")
    
    def number3_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt + "3")
    
    def number4_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt + "4")
    
    def number5_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt + "5")
    
    def number6_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt + "6")
    
    def number7_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt + "7")
    
    def number8_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt + "8")
    
    def number9_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt + "9")
    
    def clear_output(self):
        self.lb_output.setText("")
        
    def cancel_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt[:len(txt) - 1])
    
    def add_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt + '+')
    
    def sub_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt + '-')
    
    def mult_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt + '*')
    
    def div_output(self):
        txt = self.lb_output.text()
        self.lb_output.setText(txt + '/')
        
    def result_output(self):
        txt = self.lb_output.text()
        try:
            ans = eval(txt)
            self.lb_output.setText(str(ans))
        except:
            self.lb_output.setStyleSheet("color:rgb(255, 0, 0)")
            self.lb_output.setText('False Input!')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_number0.setText(_translate("MainWindow", "0"))
        self.btn_number5.setText(_translate("MainWindow", "5"))
        self.btn_number1.setText(_translate("MainWindow", "1"))
        self.btn_multiplication.setText(_translate("MainWindow", "x"))
        self.btn_multiplication.setShortcut(_translate("MainWindow", "*"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_plus.setShortcut(_translate("MainWindow", "+"))
        self.btn_neg_pos.setText(_translate("MainWindow", "+/-"))
        self.lb_output.setText(_translate("MainWindow", "0"))
        self.btn_number9.setText(_translate("MainWindow", "9"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_minus.setShortcut(_translate("MainWindow", "-"))
        self.btn_number7.setText(_translate("MainWindow", "7"))
        self.btn_number8.setText(_translate("MainWindow", "8"))
        self.btn_number4.setText(_translate("MainWindow", "4"))
        self.btn_number6.setText(_translate("MainWindow", "6"))
        self.btn_number2.setText(_translate("MainWindow", "2"))
        self.btn_number3.setText(_translate("MainWindow", "3"))
        self.btn_point.setText(_translate("MainWindow", ","))
        self.btn_modular.setText(_translate("MainWindow", "%"))
        self.btn_cancel.setText(_translate("MainWindow", "CE"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_divide.setText(_translate("MainWindow", "/"))
        self.btn_divide.setShortcut(_translate("MainWindow", "/"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


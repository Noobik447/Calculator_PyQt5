from PyQt5 import QtWidgets
import math
import random

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(400, 200)
        self.setWindowTitle("Калькулятор")
        self.lb = QtWidgets.QLabel("0")
        self.le = QtWidgets.QLineEdit()
        self.le2 = QtWidgets.QLineEdit()
        self.btn = QtWidgets.QPushButton("+")
        self.btn2 = QtWidgets.QPushButton("-")
        self.btn3 = QtWidgets.QPushButton("*")
        self.btn4 = QtWidgets.QPushButton("/")
        self.btn5 = QtWidgets.QPushButton("Степень")
        self.btn6 = QtWidgets.QPushButton("Корень")
        self.btn7 = QtWidgets.QPushButton("n!")
        self.btn8 = QtWidgets.QPushButton("C")
        self.btn9 = QtWidgets.QPushButton("Рандомное число")

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addWidget(self.le)
        vbox.addWidget(self.le2)

        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.btn, 3, 0)
        grid.addWidget(self.btn2, 3, 1)
        grid.addWidget(self.btn3, 4, 0)
        grid.addWidget(self.btn4, 4, 1)
        grid.addWidget(self.btn5, 5, 0)
        grid.addWidget(self.btn6, 5, 1)
        grid.addWidget(self.btn7, 6, 0)
        grid.addWidget(self.btn8, 6, 1)
        vbox.addLayout(grid)
        
        vbox.addWidget(self.btn9)
        self.setLayout(vbox)

        self.btn.clicked.connect(self.plus)
        self.btn2.clicked.connect(self.min)
        self.btn3.clicked.connect(self.mul)
        self.btn4.clicked.connect(self.div)
        self.btn5.clicked.connect(self.pow)
        self.btn6.clicked.connect(self.sqrt)
        self.btn7.clicked.connect(self.fact)
        self.btn8.clicked.connect(self.clear)
        self.btn9.clicked.connect(self.rand)

    def plus(self):
        res = float(self.le.text()) + float(self.le2.text())
        self.lb.setText(str(res))
        print(res)

    def min(self):
        res = float(self.le.text()) - float(self.le2.text())
        self.lb.setText(str(res))
        print(res)

    def mul(self):
        res = float(self.le.text()) * float(self.le2.text())
        self.lb.setText(str(res))
        print(res)

    def div(self):
        res = float(self.le.text()) / float(self.le2.text())
        self.lb.setText(str(res))
        print(res)

    def pow(self):
        res = math.pow(float(self.le.text()), float(self.le2.text()))
        self.lb.setText(str(res))
        print(res)

    def sqrt(self):
        res = math.sqrt(float(self.le.text()))
        self.lb.setText(str(res))
        print(res)

    def fact(self):
        res = math.factorial(int(self.le.text()))
        self.lb.setText(str(res))
        print(res)
    
    def rand(self):
        res = random.randint(int(self.le.text()), int(self.le2.text()))
        self.lb.setText(str(res))
        print(res)

    def clear(self):
        self.lb.setText("0")
        print("Cleared")

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

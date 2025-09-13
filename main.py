import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import math

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("./logo.png"))
        self.setGeometry(700, 250, 500, 700)
        self.setFixedSize(500, 700) # To prevent the window resize
        self.input = QLineEdit(self)
        self.nine = QPushButton("9", self)
        self.eight = QPushButton("8", self)
        self.seven = QPushButton("7", self)
        self.plus = QPushButton("+", self)
        self.six = QPushButton("6", self)
        self.five = QPushButton("5", self)
        self.four = QPushButton("4", self)
        self.minus = QPushButton("-", self)
        self.tree = QPushButton("3", self)
        self.two = QPushButton("2", self)
        self.one = QPushButton("1",self)
        self.multi = QPushButton("*", self)
        self.zero = QPushButton("0", self)
        self.point = QPushButton(".", self)
        self.clear = QPushButton("C", self)
        self.div = QPushButton("/", self)
        self.initUI()
    def initUI(self):
        # Setting the buttons and the layout of the application
        box = QGridLayout()
        box.addWidget(self.input, 0, 0)
        box.addWidget(self.nine, 1, 0)
        box.addWidget(self.eight, 1, 1)
        box.addWidget(self.seven, 1, 2)
        box.addWidget(self.plus, 1, 3)
        box.addWidget(self.six, 2, 0)
        box.addWidget(self.five, 2, 1)
        box.addWidget(self.four, 2, 2)
        box.addWidget(self.minus, 2, 3)
        box.addWidget(self.tree, 3, 0)
        box.addWidget(self.two, 3, 1)
        box.addWidget(self.one, 3, 2)
        box.addWidget(self.multi, 3, 3)
        box.addWidget(self.zero, 4, 0)
        box.addWidget(self.point, 4, 1)
        box.addWidget(self.clear, 4, 2)
        box.addWidget(self.div, 4, 3)
        self.setLayout(box)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
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
        pass

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
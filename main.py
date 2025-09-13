import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import math

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("./logo.png"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
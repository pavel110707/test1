import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("test")
        self.setGeometry(400, 400, 500, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window1 = MainWindow1()
    window1.show()

    app.exec()

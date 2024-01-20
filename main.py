import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import main1


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        self.setGeometry(400, 400, 500, 200)
        self.setCentralWidget(self.button)
        self.button.clicked.connect(self.clic)
        self.n = 0

    def clic(self):
        self.n += 1
        self.button.setText(f'{self.n}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
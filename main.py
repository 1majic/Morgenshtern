import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw = False
        self.pushButton.clicked.connect(self.check)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(Qt.yellow, 12, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        if self.draw:
            for i in range(random.randint(2, 20)):
                h = random.randint(10, 50)
                x = random.randint(10, 400)
                y = random.randint(10, 300)
                painter.drawEllipse(x, y, h, h)
            self.draw = False

    def check(self):
        self.draw = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
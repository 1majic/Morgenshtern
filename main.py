import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def draw(self):
        qp = QPainter(self)
        qp.setPen(QPen(Qt.yellow, 3, Qt.SolidLine))
        qp.setBrush(QColor(60, 10, 100))

        for i in range(random.randint(2, 20)):
            h = random.randint(10, 50)
            x = random.randint(10, 400)
            y = random.randint(10, 300)
            qp.drawEllipse(x, y, h, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
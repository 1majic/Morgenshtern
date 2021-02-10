from random import randint
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 120, 131, 28))
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.frame.setMinimumSize(QtCore.QSize(401, 301))
        self.frame.setMaximumSize(QtCore.QSize(401, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Очуметь"))


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.draw = False
        self.pushButton.clicked.connect(self.check)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        if self.draw:
            for i in range(randint(2, 20)):
                color = QColor((randint(0, 255)), (randint(0, 255)), (randint(0, 255)))
                painter.setPen(QPen(color, 12, Qt.SolidLine))
                painter.setBrush(color)
                h = randint(10, 50)
                x = randint(10, 400)
                y = randint(10, 300)
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
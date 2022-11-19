from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import random


def draw_cyrcle(painter: QtGui.QPainter, pos: QtCore.QPoint, radius: int):
    painter.drawEllipse(pos, radius, radius)


class Program(QtWidgets.QWidget):
    def __init__(self):
        super(Program, self).__init__()
        self.btn = QtWidgets.QPushButton('Push me', self)
        self.painter = QtGui.QPainter()
        self.was_pushed = False

        self.initUI()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        super(Program, self).paintEvent(a0)
        self.painter.begin(self)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        self.painter.setBrush(brush)
        if self.was_pushed:
            draw_cyrcle(self.painter,
                        QtCore.QPoint(random.randint(0, self.width()), random.randint(0, self.height())),
                        random.randint(10, 50))
        self.painter.end()

    def initUI(self):
        self.setWindowTitle('Круги (под глазами)')
        self.btn.move(self.width() // 2, self.height() // 2)
        self.btn.clicked.connect(self.draw)

    def draw(self):
        self.was_pushed = True
        self.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    program = Program()
    program.show()
    sys.exit(app.exec())

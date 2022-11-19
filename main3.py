from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import sqlite3


class Program(QtWidgets.QWidget):
    def __init__(self):
        super(Program, self).__init__()
        self.table = QtWidgets.QTableWidget(self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.initUI()

    def initUI(self):
        self.setMinimumSize(680, 300)
        self.table.setMinimumSize(680, 300)
        self.update_result()

    def update_result(self):
        cursor = self.con.cursor()
        result = cursor.execute('SELECT * FROM coffee').fetchall()
        self.table.setRowCount(len(result))
        if not result:
            return
        self.table.setColumnCount(len(result[0]))
        titles = [i[0] for i in cursor.description]
        self.table.setHorizontalHeaderLabels(titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    program = Program()
    program.show()
    sys.exit(app.exec())

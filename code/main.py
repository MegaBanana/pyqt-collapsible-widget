__author__ = 'Caroline Beyne'

from PyQt4 import QtGui, QtCore
import sys
from FrameLayout import FrameLayout

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)

    win = QtGui.QMainWindow()
    w = QtGui.QWidget()
    w.setMinimumWidth(350)
    win.setCentralWidget(w)
    l = QtGui.QVBoxLayout()
    l.setSpacing(0)
    l.setAlignment(QtCore.Qt.AlignTop)
    w.setLayout(l)

    t = FrameLayout(title="Buttons")
    t.addWidget(QtGui.QPushButton('a'))
    t.addWidget(QtGui.QPushButton('b'))
    t.addWidget(QtGui.QPushButton('c'))

    f = FrameLayout(title="TableWidget")
    rows, cols = (6, 3)
    data = {'col1': ['1', '2', '3', '4', '5', '6'],
            'col2': ['7', '8', '9', '10', '11', '12'],
            'col3': ['13', '14', '15', '16', '17', '18']}
    table = QtGui.QTableWidget(rows, cols)
    headers = []
    for n, key in enumerate(sorted(data.keys())):
        headers.append(key)
        for m, item in enumerate(data[key]):
            newitem = QtGui.QTableWidgetItem(item)
            table.setItem(m, n, newitem)
    table.setHorizontalHeaderLabels(headers)
    f.addWidget(table)

    l.addWidget(t)
    l.addWidget(f)

    win.show()
    win.raise_()
    print "Finish"
    sys.exit(app.exec_())


import os
import sys

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import uic

from qrangeslider import QRangeSlider

app = QtGui.QApplication(sys.argv)




rs1 = QRangeSlider()
rs1.show()
rs1.setWindowTitle('example 1')
rs1.setRange(15, 35)
rs1.setBackgroundStyle('background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #222, stop:1 #333);')
rs1.setSpanStyle('background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #282, stop:1 #393);')


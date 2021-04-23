import os
import sys

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import uic

from qrangeslider import QRangeSlider

app = QtGui.QApplication(sys.argv)

rs2 = QRangeSlider()
rs2.show()
rs2.setWindowTitle('example 2')
rs2.setFixedWidth(400)
rs2.setFixedHeight(36)
rs2.setMin(0)
rs2.setMax(100)
rs2.setRange(30, 80)
rs2.setDrawValues(False)
rs2.setStyleSheet("""
QRangeSlider * {
    border: 0px;
    padding: 0px;
}
QRangeSlider #Head {
    background: url(data/filmstrip.png) repeat-x;
}
QRangeSlider #Span {
    background: url(data/clip.png) repeat-x;
}
QRangeSlider #Tail {
    background: url(data/filmstrip.png) repeat-x;
}
QRangeSlider > QSplitter::handle {
    background: #fff;
}
QRangeSlider > QSplitter::handle:vertical {
    height: 2px;
}
QRangeSlider > QSplitter::handle:pressed {
    background: #ca5;
}
""")

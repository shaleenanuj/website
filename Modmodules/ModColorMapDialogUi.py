

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(455, 316)
        
        
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        
        
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(160, 40, 171, 24))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 180, 59, 14))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(220, 170, 71, 24))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 170, 71, 24))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        
        self.radioButton = QtGui.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(60, 100, 201, 21))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 120, 191, 31))
        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Choose Colour map", None))
        self.label.setText(_translate("Dialog", "Colour map :", None))
        self.comboBox.setItemText(0, _translate("Dialog", "viridis", None))
        self.comboBox.setItemText(1, _translate("Dialog", "magma", None))
        self.comboBox.setItemText(2, _translate("Dialog", "jet", None))
        self.comboBox.setItemText(3, _translate("Dialog", "inferno", None))
        self.comboBox.setItemText(4, _translate("Dialog", "plasma", None))
        self.comboBox.setItemText(5, _translate("Dialog", "hot", None))
        self.comboBox.setItemText(6, _translate("Dialog", "cool", None))
        self.comboBox.setItemText(7, _translate("Dialog", "rainbow", None))
        self.comboBox.setItemText(8, _translate("Dialog", "binary", None))
        self.comboBox.setItemText(9, _translate("Dialog", "gray", None))
        self.label_2.setText(_translate("Dialog", "Range :", None))
        self.lineEdit.setToolTip(_translate("Dialog", "Min", None))
        self.lineEdit_2.setToolTip(_translate("Dialog", "Max", None))
        self.radioButton.setText(_translate("Dialog", "Set color resolution range :", None))
        self.label_3.setText(_translate("Dialog", "( Note that all the alpha\n"
" function points will reset  )", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


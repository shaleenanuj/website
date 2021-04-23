# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoadStack.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_LoadDialog(QtGui.QDialog):
	
	
	def setupUi(self, Dialog):
	
	
	        Dialog.setObjectName(_fromUtf8("Dialog"))
	        Dialog.resize(447, 531)
	        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
	        self.buttonBox.setGeometry(QtCore.QRect(90, 460, 341, 32))
	        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
	        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
	        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        
        
	        self.path_label = QtGui.QLabel(Dialog)
	        self.path_label.setGeometry(QtCore.QRect(40, 40, 59, 14))
	        self.path_label.setObjectName(_fromUtf8("label"))
	        
	        self.path_lineEdit = QtGui.QLineEdit(Dialog)
	        self.path_lineEdit.setGeometry(QtCore.QRect(170, 30, 181, 24))
	        self.path_lineEdit.setObjectName(_fromUtf8("lineEdit"))
	        
	        self.browse_button= QtGui.QPushButton(Dialog)
	        self.browse_button.setGeometry(QtCore.QRect(370, 30, 71, 27))
	        self.browse_button.setObjectName(_fromUtf8("browse"))#object name..??
	        
	        self.image_prefix_label = QtGui.QLabel(Dialog)
	        self.image_prefix_label.setGeometry(QtCore.QRect(40, 100, 100, 16))
        	self.image_prefix_label.setObjectName(_fromUtf8("label_2"))
        	
        	self.image_prefix_lineEdit = QtGui.QLineEdit(Dialog)
        	self.image_prefix_lineEdit.setGeometry(QtCore.QRect(170, 100, 113, 24))
        	self.image_prefix_lineEdit.setObjectName(_fromUtf8("lineEdit_2"))
        	
        	self.offset_label = QtGui.QLabel(Dialog)
        	self.offset_label.setGeometry(QtCore.QRect(40, 180, 59, 14))
        	self.offset_label.setObjectName(_fromUtf8("label_3"))
        	
        	self.starting_index_label = QtGui.QLabel(Dialog)
        	self.starting_index_label.setGeometry(QtCore.QRect(40, 200, 110, 16))
        	self.starting_index_label.setObjectName(_fromUtf8("label_4"))
        	
        	self.offset_lineEdit = QtGui.QLineEdit(Dialog)
        	self.offset_lineEdit.setGeometry(QtCore.QRect(170, 180, 113, 24))
        	self.offset_lineEdit.setObjectName(_fromUtf8("lineEdit_3"))
        	
        	self.num_of_image_label = QtGui.QLabel(Dialog)
        	self.num_of_image_label.setGeometry(QtCore.QRect(40, 260, 125, 16))
        	self.num_of_image_label.setObjectName(_fromUtf8("label_5"))
        	
        	self.num_of_image_lineEdit = QtGui.QLineEdit(Dialog)
        	self.num_of_image_lineEdit.setGeometry(QtCore.QRect(170, 260, 113, 24))
        	self.num_of_image_lineEdit.setObjectName(_fromUtf8("lineEdit_4"))
        
        	self.data_spacing_label = QtGui.QLabel(Dialog)
        	self.data_spacing_label.setGeometry(QtCore.QRect(40, 320, 91, 16))
        	self.data_spacing_label.setObjectName(_fromUtf8("label_6"))
        
        	self.x_label = QtGui.QLabel(Dialog)
        	self.x_label.setGeometry(QtCore.QRect(150, 320, 59, 14))
        	self.x_label.setObjectName(_fromUtf8("label_7"))
        
        	self.y_label = QtGui.QLabel(Dialog)
        	self.y_label.setGeometry(QtCore.QRect(150, 350, 59, 14))
        	self.y_label.setObjectName(_fromUtf8("label_8"))
        	
        	self.z_label = QtGui.QLabel(Dialog)
        	self.z_label.setGeometry(QtCore.QRect(150, 380, 59, 14))
        	self.z_label.setObjectName(_fromUtf8("label_9"))
        
        	self.x_lineEdit = QtGui.QLineEdit(Dialog)
        	self.x_lineEdit.setGeometry(QtCore.QRect(200, 320, 51, 21))
        	self.x_lineEdit.setObjectName(_fromUtf8("lineEdit_5"))
        	
        	self.y_lineEdit = QtGui.QLineEdit(Dialog)
        	self.y_lineEdit.setGeometry(QtCore.QRect(200, 350, 51, 21))
        	self.y_lineEdit.setObjectName(_fromUtf8("lineEdit_6"))
        	
        	self.z_lineEdit = QtGui.QLineEdit(Dialog)
        	self.z_lineEdit.setGeometry(QtCore.QRect(200, 380, 51, 21))
        	self.z_lineEdit.setObjectName(_fromUtf8("lineEdit_7"))
        	
        	# self.list=QtGui.QList(Dialog)
        	#self.list.setGeometry(QtCore.Qrect(100,100,465.500))
        	#self.list.setObjectName(-formUtf8("Files"))
        	#this component is made so that later on we could stored the files from the selected directory into this list
        	

        	self.retranslateUi(Dialog)
        	
        	#QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        	#check the signal constant once again 
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        	QtCore.QMetaObject.connectSlotsByName(Dialog)
	
		#self.showDialog()
		
	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
		self.path_label.setText(_translate("Dialog", "Path :", None))
		self.browse_button.setText(_translate("Dialog", "Browse", None))
		self.image_prefix_label.setText(_translate("Dialog", "Image Prefix :", None))
		self.offset_label.setText(_translate("Dialog", "Offset :", None))
		self.starting_index_label.setText(_translate("Dialog", "(Starting index)", None))
		self.num_of_image_label.setText(_translate("Dialog", "Number of Images :", None))
		self.x_label.setText(_translate("Dialog", "x :", None))
		self.y_label.setText(_translate("Dialog", "y :", None))
		self.z_label.setText(_translate("Dialog", "z :", None))
        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_LoadDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


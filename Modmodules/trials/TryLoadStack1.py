import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
#from QtGui import QDialog
import os


class LoadStackModule(QWidget):
	def __init__(self):
		#super().__init__()
		#elf.buttonBox=QDialogButtonBox(self)
		#self.buttonBox.setGeometry(QtCore.QtRect(90,460,341,32))
		#self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		#self.buttonbox.setStandardbuttons(QDialogButtonBox.Cancel | QDialogButtonBox.ok)
		#self.buttonBox.setObjectName("Buton Box")
		self.initUi()
	
	def initUi(self):
		
		self.buttonBox=QDialogButtonBox(self)
		self.buttonBox.setGeometry(QtCore.QtRect(90,460,341,32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonbox.setStandardbuttons(QDialogButtonBox.Cancel | QDialogButtonBox.ok)
		self.buttonBox.setObjectName("Buton Box")
	
if __name__=="__main__":
		
	#app=LoadStackModule(sys.argv)
	app=QApplication(sys.argv)
	ex=LoadStackModule()
	sys.exit(app.exec_())
		
		

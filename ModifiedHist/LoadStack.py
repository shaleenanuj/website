"""
This class takes the input from the user ,i.e, details about the image stack to loaded.
It provides all this info to the Renderer.
"""

import vtk
import sys
from PyQt4 import QtGui,QtCore
from LoadStackDialogUi import Ui_LoadDialog
import os

class LoadStack(object):

	def __init__(self,driver):
		# initialize the dialog with the UI designed in PLoadStackDialogUi
		self.driver = driver
		
	def showDialog(self):
		self.Dialog = QtGui.QDialog()
		self.ui_l = Ui_LoadDialog()
		self.ui_l.setupUi(self.Dialog)
		self.Dialog.show()
		self.ui_l.lineEdit_5.setText('1')
		self.ui_l.lineEdit_6.setText('1')
		self.ui_l.lineEdit_7.setText('0.5')
		self.ui_l.pushButton.clicked.connect(self.setDirPath)
		self.ui_l.buttonBox.accepted.connect(self.accept)

	def setDirPath(self):
		# opens a File Dialog box to browse and locate the path of directory
		self.ui_l.lineEdit.setText(str(QtGui.QFileDialog.getExistingDirectory(self.ui_l,"Select Directory",os.getenv('HOME')))+"/")

	def accept(self):
		# this method is called when "Ok" is clicked 
		# it assigns the values entered by the user in the text box to the class variables
		# it also calls the renderV() of driver in order to start the rendering of the input image stack
		self.dirPath = self.ui_l.lineEdit.text()
		self.filePrefix = self.ui_l.lineEdit_2.text()
		self.offset = int(self.ui_l.lineEdit_3.text())
		self.imageNo = int(self.ui_l.lineEdit_4.text())
		self.xSpace = float(self.ui_l.lineEdit_5.text())
		self.ySpace = float(self.ui_l.lineEdit_6.text())
		self.zSpace = float(self.ui_l.lineEdit_7.text())
		self.driver.pRenderer.readImgStack(self)
		self.driver.renderV()
		QtGui.QDialog.accept(self.Dialog)

	# these are some getters written below helps the PRenderer to get the specific parameters of loaded image stack


	def getExtent(self):
		# this method reads the first image and returns a tuple having info about the extents of the image
		reader2 = vtk.vtkTIFFReader()
		reader2.SetFileName(str(self.dirPath+self.filePrefix+self.ui_l.lineEdit_3.text()+".tif"))
		reader2.Update()
		return reader2.GetDataExtent()

	def getDigits(self):
		""" there was a problem if the image stack have a perticular number of digits in file name 
		(like some may have 3 digits Img_000, Img_001.. or some may be normal like Img_0,Img_1,..)
		now its a normal human tendency that one will follow this pattern while giving the offset 
		(means if image name has the digit pattern as Img_000,Img_001 so one will write the offset as "000").
		Assuming this we return the length of this offset as the number of digits in file name.
		This helps the SetFilePattern() in the PRenderer to read the files having such specific digit pattern in the file name.		 
		""" 
		return len(self.ui_l.lineEdit_3.text())



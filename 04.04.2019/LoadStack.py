"""
This class takes the input from the user ,i.e, details about the image stack to loaded.
It provides all this info to the Renderer.
"""

import vtk
import sys
from PyQt4 import QtGui,QtCore
from LoadStackDialogUi import Ui_LoadDialog
import os
import glob
import json
from RenderConfiguration import RenderConfiguration
from LoggingFile import Logger



class LoadStack(object):

	def __init__(self,driver):
		# initialize the dialog with the UI designed in PLoadStackDialogUi
		self.driver = driver
		
	def showDialog(self):
		self.Dialog = QtGui.QDialog()
		self.ui_l = Ui_LoadDialog()
		self.ui_l.setupUi(self.Dialog)
		self.Dialog.show()
		self.ui_l.x_lineEdit.setText('1')
		self.ui_l.y_lineEdit.setText('1')
		self.ui_l.z_lineEdit.setText('0.5')
		self.ui_l.browse_button.clicked.connect(self.setDirPath)
		self.ui_l.buttonBox.accepted.connect(self.loadValueFromLoadStackUi)

	def setDirPath(self, driver):
		# opens a File Dialog box to browse and locate the path of directory
		#self.ui_l.lineEdit.setText(str(QtGui.QFileDialog.getExistingDirectory(self.ui_l,"Select Directory",os.getenv('HOME')))+"/")
		dir_path = str(QtGui.QFileDialog.getExistingDirectory(self.ui_l,"Select Directory",os.getenv('HOME')))+"/"
		#dir_name = str(dir_path)
		self.ui_l.path_lineEdit.setText(dir_path)
		self.setFileImages(dir_path,driver)
	
	def setFileImages(self , dir_path,driver):
	#check whi i have passed driver object here
		#print dir_path
		file_list = glob.glob(dir_path + "*.tif")
		image_prefix = " " 
		offset_list = []
		#print (file_list)
		#print(len(file_list))
		for index in range(len(file_list)):
			filename = os.path.basename(file_list[index])
			offset = ''
			image_prefix = ''
			#print (filename)
			#print(len(filename))
			for character in range(len(filename)):
				if filename[character].isdigit():
					offset = offset + filename[character]
				else:
					image_prefix = image_prefix + filename[character]
					
			offset_list.append(offset)
		#print (offset_list)
		#sys.exit()
		#assert check_something(), "Incorrect data"
		offset_list.sort(key = int)
		limit = image_prefix.find('.')
		image_prefix = image_prefix[0 : limit]
		#print (offset_list[1])
		#print (image_prefix)
		self.ui_l.image_prefix_lineEdit.setText(image_prefix)
		offset_final=offset_list[0]
		#print a
     		self.ui_l.offset_lineEdit.setText(offset_final)
     		no_of_images=len(file_list)
     		self.ui_l.num_of_image_lineEdit.setText(str(no_of_images))
		#self.driver.saveLoadStackvalue()
		
		
		
		
		

		

	
	def loadValueFromLoadStackUi(self):
		# this method is called when "Ok" is clicked 
		# it assigns the values entered by the user in the text box to the class variables
		# it also calls the renderV() of driver in order to start the rendering of the input image stack
		self.dirPath = self.ui_l.path_lineEdit.text()
		self.filePrefix = self.ui_l.image_prefix_lineEdit.text()
		self.offset =int(self.ui_l.offset_lineEdit.text())
		self.imageNo=int(self.ui_l.num_of_image_lineEdit.text())
		self.xSpace =float(self.ui_l.x_lineEdit.text())
		self.ySpace =float(self.ui_l.y_lineEdit.text())
		self.zSpace =float(self.ui_l.z_lineEdit.text())
		self.accept(self.dirPath,self.filePrefix,self.offset,self.imageNo,self.xSpace,self.ySpace,self.zSpace)
		
		
	#why are we using two different functions as fromui function will always call the accept function..?
	#we are splitting the function into two so as to increase the usability as we wont require the fromui part while we will be using loadui feature as there we will have to pass the following values to the renderer hence thi function will be set as the call back function of the loadDataImage
	
	
	def accept(self,dirPath,filePrefix,offset,imageNo,xSpace,ySpace,zSpace):
		rc=RenderConfiguration()
		rc.dirPath =self.dirPath
		rc.filePrefix =self.filePrefix
		rc.offset =self.offset
		rc.imageNo=self.imageNo
		rc.xSpace =self.xSpace
		rc.ySpace =self.ySpace
		rc.zSpace =self.zSpace
		rc.digits=self.getDigits()
		extent=self.getExtent()
		#print(extent[1])
		rc.extent_1 = extent[1]
		rc.extent_3 = extent[3]
		
		
		self.driver.pRenderer.readImgStack(rc)
		self.driver.renderV()
		QtGui.QDialog.accept(self.Dialog)
		
		lg=Logger()
		lg.log("Image Loaded")
	
	

	
	# these are some getters written below helps the PRenderer to get the specific parameters of loaded image stack

	def getExtent(self):
		# this method reads the first image and returns a tuple having info about the extents of the image
		reader2 = vtk.vtkTIFFReader()
		reader2.SetFileName(str(self.dirPath+self.filePrefix+self.ui_l.offset_lineEdit.text()+".tif"))
		#reader2.SetFileName(str(self.dirPath+self.filePrefix+self.offset)+".tif")
		reader2.Update()
		extent = reader2.GetDataExtent()
		#print extent
		#print(type(extent))
		return extent
	def getDigits(self):
		""" there was a problem if the image stack have a perticular number of digits in file name 
		(like some may have 3 digits Img_000, Img_001.. or some may be normal like Img_0,Img_1,..)
		now its a normal human tendency that one will follow this pattern while giving the offset 
		(means if image name has the digit pattern as Img_000,Img_001 so one will write the offset as "000").
		Assuming this we return the length of this offset as the number of digits in file name.
		This helps the SetFilePattern() in the PRenderer to read the files having such specific digit pattern in the file name.		 
		""" 
		
		digits =len(self.ui_l.offset_lineEdit.text())
		return digits
		













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
	
		self.showDialog()
		
    	def retranslateUi(self, Dialog):
        	Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        	self.path_label.setText(_translate("Dialog", "Path :", None))
        	self.browse_button.setText(_translate("Dialog", "Browse", None))
        	self.image_prefix_label.setText(_translate("Dialog", "Image Prefix :", None))
        	self.offset_label.setText(_translate("Dialog", "Offset :", None))
        	self.starting_index_label.setText(_translate("Dialog", "(Starting index)", None))
        	self.num_of_image_label.setText(_translate("Dialog", "Number of Images :", None))
        	self.data_spacing_label.setText(_translate("Dialog", "Data Spacing:", None))
        	self.x_label.setText(_translate("Dialog", "x :", None))
        	self.y_label.setText(_translate("Dialog", "y :", None))
        	self.z_label.setText(_translate("Dialog", "z :", None))
        



	def showDialog(self):
	
		 
		self.x_lineEdit.setText('1')
		self.y_lineEdit.setText('1')
		self.z_lineEdit.setText('0.5')
		self.browse_button.clicked.connect(self.setDirPath)#connected to the browse button
		self.buttonBox.accepted.connect(self.accept)
	
		
	def setDirPath(self):
	
		# opens a File Dialog box to browse and locate the path of directory
		dir_path =QtGui.QFileDialog.getExistingDirectory(self,"Select Directory",os.getenv('HOME'))
 		#self.lineEdit.setText(str(QtGui.QFileDialog.getExistingDirectory(self,"Select Directory",os.getenv('HOME')))+"/")
 		
 		#print(dir_path)
 		
 		dir_name = str(dir_path)
 		self.path_lineEdit.setText(dir_name + "/")
		self.setFileImages(dir_name)
		#self.lineEdit_2.setText(image_prefix)
		
		#return setFileImages(self,dir_name)

	
	def setFileImages(self,dir_name):
		#i=1
		#while()
		#file_name=QtGui.QFileDialog.ExistingFile
		
     		#QStringList fileNames
     		
     		#file_path = QtGui.QFileDialog.getExistingDirectory(self,"Select Files",dir_name)
     		#file_name=str(file_path)

		file_name = QtGui.QFileDialog.getOpenFileName(self, "Select File",dir_name,"Images (*.tif)")		
		
		#print file_name
		#print(len(file_name))
		
		#print(len("abc"))
		
		#no need to reverse the string could use the method [lastindexOf()]
		res_file_name=' '
		
		for i in file_name:
		
			res_file_name = i + res_file_name
			
		#print res_file_name
		
		
		
		#print res_file_name.find('/')
		#QString.section function could also be used
		limit=res_file_name.indexOf('/')
		trunc_string = res_file_name.mid(0 ,limit)
		
		file_name=" "
		
		for i in trunc_string:
		
			file_name= i + file_name	
			
			
		#print file_name
		# snippet will be optimized
		
		limit1 = file_name.indexOf('.')
		file_name=file_name.mid(0,limit1)
		
		file_name_utf8=file_name.toUtf8()
		
		image_prefix=''
		offset=''
		
		
		
							
		for c in file_name_utf8:
		
		    if c.isdigit():
		    	offset=offset + c
		    	
		    	
		    else:
		    
		    	image_prefix= image_prefix + c
		
		
		#command_string = '  ls ' + dir_name +  ' | wc -l' 
		#print command_string
		
		dir_name = dir_name + '/'
		
		#file_count=subprocess.check_output(['ls ' + dir_name + '| wc -l'])
		#print file_count.stdout
		#file_count=command_string
		
		filename_list=glob.glob(dir_name  + '*.tif')
		file_count=(len(filename_list))
		
		offset_int=int(offset)	
		image_no= file_count - offset_int
		image_no=str(image_no)
			
		#add an if else statement considering the situation where the index of the file starts with the zeroth pos
		#check why a new icon of application is bein g shown when this module is being opened
		#check why the app is able to accept the image number value even if it exceeds the actual number of images
		'''
     		digit_pattern = re.compile(r'\D')
     		alpha_pattern = re.compile(r'\d')
     		offset = digit_pattern.split(file_name)
     		image_prefix = alpha_pattern.split(file_name)
     		'''
     		
     		#offset = digit_pattern.split(file_name)
     		#image_prefix = alpha_pattern.split(file_name)
     		
     		#print offset
     		#print image_prefix
     		
     		self.image_prefix_lineEdit.setText(image_prefix)
     		self.offset_lineEdit.setText(offset)
     		self.num_of_image_lineEdit.setText(image_no)
     		
     		#fileNames = QtGui.QFileDialog.getOpenFileNames(self, "Select File",dir_name,"Images (*.tif)")
     		#QtGui.QFileDialog.selectFile()
     		#QtCore.QBject.connect(self,QtCore.SIGNAL())
     		
     	
	def accept(self):
		# this method is called when "Ok" is clicked 
		# it assigns the values entered by the user in the text box to the class variables
		# it also calls the renderV() of driver in order to start the rendering of the input image stack
		self.dirPath = self.ui_l.lineEdit.text()
		self.filePrefix = self.ui_l.lineEdit_2.text()
		self.offset = int(self.ui_l.lineEdit_3.text())
		self.imageNo = int(self.ui_l.lineEdit_4.text())

		#ask the purpose of this fucntion via mail
		self.xSpace = float(self.ui_l.lineEdit_5.text())
		self.ySpace = float(self.ui_l.lineEdit_6.text())
		self.zSpace = float(self.ui_l.lineEdit_7.text())



if __name__ == "__main__":
    import sys
    import os
    import re
    import subprocess
    import glob
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_LoadDialog()
    ui.setupUi(Dialog)
    Dialog.show()
   # ui.showDialog()
    
    sys.exit(app.exec_())



'''
		self.ui_l.lineEdit_5.setText('1')
		self.ui_l.lineEdit_6.setText('1')
		self.ui_l.lineEdit_7.setText('0.5')
		self.ui_l.pushButton.clicked.connect(self.setDirPath)#connected to the browse button
		self.ui_l.buttonBox.accepted.connect(self.accept)


	#using the file Mode enum of class QfileDialog we could access the constant Existing Files
	#this constant will return the names of all the files that are present there
	
		
		
		
		
	def setDirPath(self):
		# opens a File Dialog box to browse and locate the path of directory
		self.ui_l.lineEdit.setText(str(QtGui.QFileDialog.getExistingDirectory(self.ui_l,"Select Directory",os.getenv('HOME')))+"/")
		self.setFileImages()
		self.u_il.lineEdit_2.setText(image_prefix)
		self.u_il.lineEdit_3.setText(offset)
	
	def setFileImages(self):
		#i=1
		#while()
		file_name=QtGui.QfileDialog.ExistingFile
		digit_pattern = re.compile(r'\D')
     		alpha_pattern = re.compile(r'\d')
     		offset = filter(None, digit_pattern.split(file_name))
     		image_prefix = filter(None, alpha_pattern.split(file_name))
     		

	def accept(self):
		# this method is called when "Ok" is clicked 
		# it assigns the values entered by the user in the text box to the class variables
		# it also calls the renderV() of driver in order to start the rendering of the input image stack
		self.dirPath = self.ui_l.lineEdit.text()
		self.filePrefix = self.ui_l.lineEdit_2.text()
		self.offset = int(self.ui_l.lineEdit_3.text())
		self.imageNo = int(self.ui_l.lineEdit_4.text())

		#ask the purpose of this fucntion via mail
		self.xSpace = float(self.ui_l.lineEdit_5.text())
		self.ySpace = float(self.ui_l.lineEdit_6.text())
		self.zSpace = float(self.ui_l.lineEdit_7.text())


'''

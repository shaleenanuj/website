"""
This class manages calls to different class functions (/utilities) as and when required and serves as a central module.
This class should be called in order to run the entire software.
It takes the UI from MainWindowUi class.
"""


from PyQt4 import QtCore,QtGui
import LoadStack, MainWindowUi, Renderer, CutObj, HistogramWidget
from RecDialogUi import Ui_Dialog
from LoadStackDialogUi import Ui_LoadDialog
import sys
import os
from vtk.util.numpy_support import vtk_to_numpy
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np		
from matplotlib.colors import Normalize
import time
import threading
import pickle
import json
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
from RenderConfiguration import RenderConfiguration
#from qrangeslider1 import QRangeSlider


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

class Driver:

	flag_stackRendered = False

	
	def __init__(self):
		# We create a MainWindow object and initialise with the UI from PMainWindowUi
		self.app = QtGui.QApplication(sys.argv)
		self.MainWindow = QtGui.QMainWindow()
		self.ui_m = MainWindowUi.Ui_MainWindow()
		self.ui_m.setupUi(self.MainWindow)

		self.Dialog = QtGui.QDialog()
		self.ui_l = Ui_LoadDialog()
		self.ui_l.setupUi(self.Dialog)
		
		
		

		# We connect all the buttons to their respective callback functions, called when the 'clicked' event is generated 
		self.ui_m.setRange.clicked.connect(self.colorMask)
		self.ui_m.pushButton.clicked.connect(self.openLoadStackDialog)
		self.ui_m.pushButton_2.clicked.connect(self.cutObj)
		self.ui_m.pushButton_3.clicked.connect(self.setSliceResolution)
		self.ui_m.pushButton_4.clicked.connect(self.changeColorMap)
		self.ui_m.pushButton_5.clicked.connect(self.takeSnapshot)
		#self.ui_m.pushButton_6.clicked.connect(self.saveAsVTKObj)
		self.ui_m.pushButton_7.clicked.connect(self.record)
		self.ui_m.pushButton_8.clicked.connect(self.removePoint)
		self.ui_m.pushButton_9.clicked.connect(self.getIntensityOpacityFromUi)#call getIntensityOpacityFromUi function here
		self.ui_m.pushButton_10.clicked.connect(self.renderV)
		#self.ui_m.pushButton_11.clicked.connect(self.openVTKObj)
		self.ui_m.pushButton_12.clicked.connect(self.changeBGColor)
		self.ui_m.pushButton_13.clicked.connect(self.resetCamera)
		self.ui_m.pushButton_11.clicked.connect(self.alignPlaneToX)
		self.ui_m.pushButton_14.clicked.connect(self.alignPlaneToZ)
		self.ui_m.pushButton_15.clicked.connect(self.alignPlaneToY)
		self.ui_m.saveImage_pushButton.clicked.connect(self. saveVtkConfiguration)
		self.ui_m.loadImage_pushButton.clicked.connect(self.openVTKObj)

		# Below are the toggle buttons
		self.ui_m.radioButton_hist.toggled.connect(self.toggleColorMasking)
		self.ui_m.radioButton.toggled.connect(self.toggleOutline)
		self.ui_m.radioButton_2.toggled.connect(self.togglePlane)
		self.ui_m.radioButton_3.toggled.connect(self.toggleClippingBox)
		self.ui_m.radioButton_4.toggled.connect(self.toggleVolume)
		self.ui_m.radioButton_5.toggled.connect(self.toggleSlice)
		self.ui_m.radioButton_6.toggled.connect(self.toggleAlignedPlane)
		
		self.ui_m.horizontalSlider.valueChanged.connect(self.valueChangeSlider)
		#these are colorMasking widgets which are initially set as disabled
		self.ui_m.min.setEnabled(False)
		self.ui_m.max.setEnabled(False)
		self.ui_m.setRange.setEnabled(False)
		
		# These are the 'Clip' and 'Set' (set slice resolution) buttons which are initially disabled, enabled only when the Plane Widget is active
		self.ui_m.pushButton_2.setEnabled(False)
		self.ui_m.pushButton_3.setEnabled(False)
		self.ui_m.pushButton_10.setEnabled(False)
		self.ui_m.pushButton_11.setEnabled(False)
		self.ui_m.pushButton_14.setEnabled(False)
		self.ui_m.pushButton_15.setEnabled(False)
		self.ui_m.horizontalSlider.setEnabled(False)
		self.Dialog = QtGui.QDialog()
		self.ui_l = Ui_Dialog()
		self.ui_l.setupUi(self.Dialog)



		self.pRenderer = Renderer.Renderer()
		self.pRenderer.renderBlank(self.ui_m.qvtkWidget)
		self.MainWindow.show()
		
		self.pCutObj = CutObj.CutObj()
		self.histWidg = HistogramWidget.HistogramWidget()

		self.loadStack = LoadStack.LoadStack(self)
		
		#self.rc=RenderConfiguration()

		sys.exit(self.app.exec_())



	def openLoadStackDialog(self):

		self.ui_m.radioButton_2.setChecked(False)
		self.loadStack.showDialog()
		self.ui_m.pushButton_10.setEnabled(True)


	"""def openVTKObj(self):
		fname = str(QtGui.QFileDialog.getOpenFileName(self.MainWindow, "Open File",os.getenv('HOME'),"vtkObj (*.vtk)"))
		self.pRenderer.readVtkObj(fname)
		
		self.renderV()"""
	
	
	
	
	
	'''
	def openVTKObj(self):
		fname = str(QtGui.QFileDialog.getOpenFileName(self.MainWindow, "Open File",os.getenv('HOME'),"*.cfg"))
		#self.pRenderer.readVtkObj(fname)
		rc = RenderConfiguration()
		
		with open(fname) as json_file:  
			data = json.load(json_file)
			for index in data['LoadStack']:
			
				
        			rc.dirPath =index['path']
				rc.filePrefix =index['image_prefix']
				rc.offset =index['offset']
				rc.imageNo=index['imageNo']
				rc.xSpace =index['xSpace']
				rc.ySpace =index['ySpace']
				rc.zSpace =index['zSpace']
				
				rc.extent=self.loadStack.getExtent()
				rc.digits=self.loadStack.getDigits()
				
				
			self.pRenderer.readImgStack(rc)
			self.renderV()
	'''

	def renderV(self):
		# calls the Renderer volume which actually visualize the object (/renders the object)
		# the call to this method is made from the LoadStack class, so that as soon as the "OK" button of dialog is pressed, the volume should render
		
		
		if self.flag_stackRendered:
			self.cMin = self.pRenderer.cMin
			self.cMax = self.pRenderer.cMax
			self.pRenderer.planeWidget.Off()   # otherwise gives segmentation fault
			self.pRenderer.boxWidget.Off()
			self.pRenderer.widgetAxes.Off()
			self.pRenderer.alignedPlaneWidget.Off()
			self.ui_m.figure.clear()
		#self.pRenderer.renderVolume(self.ui_m.getVtkWidget(),self.ui_m.qvtkWidget_2)
		self.pRenderer.renderVolume(self.ui_m.qvtkWidget)
		# default value for color resolution used in histogram and alpha function plot
		self.cMin = self.pRenderer.cMin
		self.cMax = self.pRenderer.cMax	
		self.ui_m.radioButton.setChecked(True)
		self.ui_m.radioButton_2.setChecked(False)
		self.ui_m.radioButton_3.setChecked(False)
		self.ui_m.radioButton_4.setChecked(True)
		self.ui_m.radioButton_5.setChecked(False)
		self.ui_m.radioButton_6.setChecked(False)
		self.flag_stackRendered = True
		self.alignPlaneToZ()
		# setting default values for table
		self.alphaFuncPoints = {self.cMin:0.0, self.cMax:1.0}
		self.createTable()
		self.plot()
		self.pRenderer.widgetAxes.SetEnabled( 1 )
		self.pRenderer.widgetAxes.InteractiveOff()

	def cutObj(self):
		if self.flag_stackRendered:
			self.ui_m.radioButton_2.setChecked(False)
			self.pCutObj.cut(self.pRenderer)

	def toggleOutline(self):
		if self.flag_stackRendered:
			if self.ui_m.radioButton.isChecked() :
				self.pRenderer.outlineActor.VisibilityOn()
			else:
				self.pRenderer.outlineActor.VisibilityOff()
			self.pRenderer.renderWin.Render()


	def togglePlane(self):
		if self.flag_stackRendered:
			if self.ui_m.radioButton_2.isChecked() :
				self.pRenderer.planeWidget.On()
				self.ui_m.radioButton_5.setChecked(True)
				self.ui_m.pushButton_2.setEnabled(True)
				
			else:
				self.pRenderer.planeWidget.Off()
				self.ui_m.pushButton_2.setEnabled(False)
				self.ui_m.pushButton_3.setEnabled(False)	
			self.pRenderer.renderWin.Render()

	def toggleClippingBox(self):
		if self.flag_stackRendered:
			if self.ui_m.radioButton_3.isChecked() :
				self.pRenderer.boxWidget.On()
				
			else:
				self.pRenderer.boxWidget.Off()
			self.pRenderer.renderWin.Render()


	def toggleVolume(self):
		if self.flag_stackRendered:
			if self.ui_m.radioButton_4.isChecked() :
				self.pRenderer.volume.VisibilityOn()
			else:
				self.pRenderer.volume.VisibilityOff()
			self.pRenderer.renderWin.Render()

	def toggleSlice(self):
		if self.flag_stackRendered:
			if self.ui_m.radioButton_5.isChecked() :
				self.pRenderer.contourActor.VisibilityOn()
				self.ui_m.pushButton_3.setEnabled(True)
			else:
				self.pRenderer.contourActor.VisibilityOff()
				self.ui_m.pushButton_3.setEnabled(False)
				self.pRenderer.planeWidget.Off()
				self.ui_m.pushButton_2.setEnabled(False)
				self.ui_m.radioButton_2.setChecked(False)
			self.pRenderer.renderWin.Render()

	def toggleAlignedPlane(self):			# On / Off the ImagePlaneWidget widget. 
							#By default  plane is aligned to  Z axis and sets the state of buttons and slider accordingly.
		if self.flag_stackRendered:
			if self.ui_m.radioButton_6.isChecked() :
				self.pRenderer.alignedPlaneWidget.On()
				self.ui_m.pushButton_11.setEnabled(True)
				self.ui_m.pushButton_14.setEnabled(True)
				self.ui_m.pushButton_15.setEnabled(True)
				self.ui_m.horizontalSlider.setEnabled(True)
				
			else:
				self.pRenderer.alignedPlaneWidget.Off()
				self.ui_m.pushButton_11.setEnabled(False)
				self.ui_m.pushButton_14.setEnabled(False)
				self.ui_m.pushButton_15.setEnabled(False)
				self.ui_m.horizontalSlider.setEnabled(False)
			self.pRenderer.renderWin.Render()
			
	def alignPlaneToX(self):
		if self.flag_stackRendered:
			self.pRenderer.alignedPlaneWidget.SetPlaneOrientationToXAxes()
			ex = self.pRenderer.reader.GetDataExtent()		# gets the data extent of the volume from the reader
			self.ui_m.horizontalSlider.setMinimum(ex[0])		# set the sliders min and max as per the data extent
			self.ui_m.horizontalSlider.setMaximum(ex[1])
			center = int((ex[1]-ex[0])/2)
			self.ui_m.horizontalSlider.setValue(center)		# place plane at the center
			self.pRenderer.alignedPlaneWidget.SetSliceIndex(center)
			self.pRenderer.renderWin.Render()

	def alignPlaneToY(self):
		if self.flag_stackRendered:
			self.pRenderer.alignedPlaneWidget.SetPlaneOrientationToYAxes()
			ex = self.pRenderer.reader.GetDataExtent()		# gets the data extent of the volume from the resder
			self.ui_m.horizontalSlider.setMinimum(ex[2])		# set the sliders min and max as per the data extent
			self.ui_m.horizontalSlider.setMaximum(ex[3])
			center = int((ex[3]-ex[2])/2)
			self.ui_m.horizontalSlider.setValue(center)		# place plane at the center
			self.pRenderer.alignedPlaneWidget.SetSliceIndex(center)
			self.pRenderer.renderWin.Render()
			
	def alignPlaneToZ(self):
		if self.flag_stackRendered:
			self.pRenderer.alignedPlaneWidget.SetPlaneOrientationToZAxes()
			ex = self.pRenderer.reader.GetDataExtent()		# gets the data extent of the volume from the resder
			self.ui_m.horizontalSlider.setMinimum(ex[4])		# set the sliders min and max as per the data extent
			self.ui_m.horizontalSlider.setMaximum(ex[5])
			center = int((ex[5]-ex[4])/2)
			self.ui_m.horizontalSlider.setValue(center)		# place plane at the center
			self.pRenderer.alignedPlaneWidget.SetSliceIndex(center)
			self.pRenderer.renderWin.Render()


	def valueChangeSlider(self):
			newPos = int(self.ui_m.horizontalSlider.value())
			self.pRenderer.alignedPlaneWidget.SetSliceIndex(newPos)
			self.pRenderer.renderWin.Render()
	
	
	def toggleColorMasking(self):
	
			if self.flag_stackRendered:
				if self.ui_m.radioButton_hist.isChecked():
					#self.pRenderer.alignedPlaneWidget.On()
					
					self.ui_m.min.setEnabled(True)
					self.ui_m.max.setEnabled(True)
					self.ui_m.setRange.setEnabled(True)
					self.ui_m.tableWidget.setEnabled(False)	
					
				else:
					#self.pRenderer.alignedPlaneWidget.Off()
					
					self.ui_m.min.setEnabled(False)
					self.ui_m.max.setEnabled(False)
					self.ui_m.setRange.setEnabled(False)
					self.ui_m.tableWidget.setEnabled(True)
				self.pRenderer.renderWin.Render()
			
	
	def colorMask(self):
		if self.flag_stackRendered:
			
			rc=RenderConfiguration()
			allRows = self.ui_m.tableWidget.rowCount()
            rc.allrows=int(allRows)
    			for row in xrange(0,allRows):
    				intensity= self.ui_m.tableWidget.item(row,0)
    				print(type(intensity))
    				#opacity= self.ui_m.tableWidget.item(row,1)
    				intensity =intensity.text()
				intensity=str(intensity)
				self.addPoint(intensity , 0)
			
			#self.removePoint()
			intensity_min =int(self.ui_m.min.text())
			intensity_max = int(self.ui_m.max.text())
			#self.addPoint(0,0.0)
			self.addPoint(intensity_min,0.0)
			self.addPoint(intensity_min+1,0.6)
			self.addPoint(intensity_max-1,0.6)
			self.addPoint(intensity_max,0.0)
			#self.addPoint(255,0.0)	
			#self.addPoint(256,0.0)			  
			

	def changeColorMap(self):
		if self.flag_stackRendered:
			self.histWidg.showDialogBox(self)
			self.pRenderer.volume.Update()
			self.histWidg.plotAlphaFunc(self.pRenderer.alphaChannelFunc,self.ax2,self.ui_m.canvas,self.pRenderer.cMin,self.pRenderer.cMax)

	def takeSnapshot(self):
		if self.flag_stackRendered:
			fname = str(QtGui.QFileDialog.getSaveFileName(self.MainWindow, "Save File",os.getenv('HOME'),"Images (*.png)"))
			self.pRenderer.snapshot(fname)


	def plot(self):
		mpl.rcParams['agg.path.chunksize'] = 10000

		self.data = vtk_to_numpy(self.pRenderer.reader.GetOutput().GetPointData().GetScalars())		# we convert the vtk scalars from the vtkTIFFReader to the numpy array so matplotlib can process it

		# create an axis for plotting histogram
		self.ax = self.ui_m.figure.add_subplot(111)
		
		#self.ax2 = self.ui_m.figure.add_subplot(111)
		# create an axis for plotting the alpha function
		self.ax2 = self.ax.twinx()


		# plot the graphs
		self.histWidg.plotHist(self,'viridis',self.cMin,self.cMax)				# plots the histogram 
		self.histWidg.plotAlphaFunc(self.pRenderer.alphaChannelFunc,self.ax2,self.ui_m.canvas,self.pRenderer.cMin,self.pRenderer.cMax)	#plots the alpha function
		
		#plt.scatter(ix, iy, color = "Blue",s=50, alpha=1)
		
		# refresh canvas
		self.ui_m.canvas.draw()


	

	def setSliceResolution(self):
		if self.flag_stackRendered:
			self.pRenderer.planeWidget.SetResolution(int(self.ui_m.lineEdit.text()))
			self.pRenderer.renderWin.Render()




	def addPoint(self , intensity ,opacity):
		if self.flag_stackRendered:
			#intensity = int(self.ui_m.lineEdit_2.text())
			#opacity = float(self.ui_m.lineEdit_3.text())
			if self.ui_m.radioButton_hist.isChecked():
			
				self.pRenderer.alphaChannelFunc.AddPoint(float(intensity),float(opacity))
				self.pRenderer.renderWin.Render()
				self.histWidg.plotAlphaFunc(self.pRenderer.alphaChannelFunc,self.ax2,self.ui_m.canvas,self.pRenderer.cMin,self.pRenderer.cMax)
				self.alphaFuncPoints[intensity]=opacity #key value pair for table of intensity and opacity
				#self.createTable()
				self.ui_m.lineEdit_2.setText("")
				self.ui_m.lineEdit_3.setText("")
			else:
			
				self.pRenderer.alphaChannelFunc.AddPoint(float(intensity),float(opacity))
				self.pRenderer.renderWin.Render()
				self.histWidg.plotAlphaFunc(self.pRenderer.alphaChannelFunc,self.ax2,self.ui_m.canvas,self.pRenderer.cMin,self.pRenderer.cMax)
				self.alphaFuncPoints[intensity]=opacity #key value pair for table of intensity and opacity
				self.createTable()
				self.ui_m.lineEdit_2.setText("")
				self.ui_m.lineEdit_3.setText("")
	def removePoint(self):
		if self.flag_stackRendered:
			row = int(self.ui_m.tableWidget.currentRow())
			intensity = int(self.ui_m.tableWidget.item(row,0).text())
			self.alphaFuncPoints.pop(intensity)
			self.pRenderer.alphaChannelFunc.RemovePoint(intensity)
			self.pRenderer.renderWin.Render()
			self.histWidg.plotAlphaFunc(self.pRenderer.alphaChannelFunc,self.ax2,self.ui_m.canvas,self.pRenderer.cMin,self.pRenderer.cMax)
			self.createTable()

	# function to take an input from the user
	
	def getIntensityOpacityFromUi(self):
		if self.flag_stackRendered:
			intensity = int(self.ui_m.lineEdit_2.text())
			opacity = float(self.ui_m.lineEdit_3.text())
			self.addPoint(intensity,opacity)
	
	
	def createTable(self):
		if self.flag_stackRendered:
			self.ui_m.tableWidget.clear()
			self.ui_m.tableWidget.setHorizontalHeaderItem(0,QtGui.QTableWidgetItem("Intensity"))
			self.ui_m.tableWidget.setHorizontalHeaderItem(1,QtGui.QTableWidgetItem("Opacity"))
			self.ui_m.tableWidget.setRowCount(0)
			for key in sorted(self.alphaFuncPoints):
				self.ui_m.tableWidget.insertRow(self.ui_m.tableWidget.rowCount())
				self.ui_m.tableWidget.setItem(self.ui_m.tableWidget.rowCount()-1,0.0,QtGui.QTableWidgetItem(str(key)))
				self.ui_m.tableWidget.setItem(self.ui_m.tableWidget.rowCount()-1,1.0,QtGui.QTableWidgetItem(str(self.alphaFuncPoints[key])))	

	#onclick function for interactive histogram
	
	def onclick(self,event):#change the name indicating this is for histogram
		if self.flag_stackRendered:
			#global ix, iy
			ix, iy = event.xdata, event.ydata
			#print 'x = %d, y = %d'%(ix, iy)
			ix=int(ix)
			iy=round(iy,2)
			self.addPoint(ix,iy)
			#plt.scatter(ix, iy, color = "Blue",s=50, alpha=1)
			#return (ix ,iy)
			
			#data=rc.intensityOpacity()
			self.scatterPlot(ix,iy)
	
	
	def scatterPlot(self,ix,iy):
	
		if self.flag_stackRendered:
		
			ix=round(ix)
			iy=round(iy)
			colors = (0,0,0)
			fig,ax=plt.subplots()
			print ix
			coll = ax.scatter(ix, iy, c = colors ,s=10000, alpha=0.5)
			fig.canvas.draw()
			
	

	
			
	'''		
	def saveAsVTKObj(self):
		if self.flag_stackRendered:
		
		
			
			fname = str(QtGui.QFileDialog.getSaveFileName(self.MainWindow, "Save File",os.getenv('HOME'),"vtkVolumeObj"))+".vtk"
			#self.pRenderer.writeImageData(fname)
			with open(fname,'wb') as file:
				pickle.dump(self.pRenderer.reader.GetOutput(),file,-1)
	
	'''
	
	def openVTKObj(self):			
		fname = str(QtGui.QFileDialog.getOpenFileName(self.MainWindow, "Open File",os.getenv('HOME'),"*.cfg"))
		#self.pRenderer.readVtkObj(fname)
		rc = RenderConfiguration()
		
		with open(fname) as json_file:  
			data = json.load(json_file)
			for index in data['LoadStack']:
			
			
        			rc.dirPath =index['path']
				rc.filePrefix =index['image_prefix']
				rc.offset =index['offset']
				imageNo=index['imageNo']
				
				
				
				xSpace =index['xSpace']
				ySpace =index['ySpace']
				zSpace =index['zSpace']
				
				rc.xSpace =float(xSpace)
				rc.ySpace =float(ySpace)
				rc.zSpace =float(zSpace)
				 
				rc.extent_1=index['extent_1']
				imageNo= imageNo.split()[0]
				rc.imageNo =imageNo
				rc.extent_3=index['extent_3']
				rc.digits=index['digits']
				#imageNo=imageNo.encode('ascii','ignore')
				#print(imageNo)
				#extent = unicode(extent,"Utf-8")
				#extent = extent.encode("utf-8")
				#extent = Encoding.UTF8.GetString(Encoding.Default.GetBytes(extent))
				#extent=ord(extent)
				#extent= extent.split(',')
				#####rc.extent_1=extent[1]
				#rc.extent_3=extent[3]
				
			for index in data['intensityOpacity']:
			
			
				intensity = index['intensity']
				intensity=intensity.split(",")
				opacity = index['opacity']
				opacity=opacity.split(",")
				#print(intensity)
				#print(opacity)
				
				#self.flag_stackRendered =True
                opacity=[t.replace("[","") for t in opacity]
		opacity=[t.replace("]","") for t in opacity]
		opacity=[t.replace("'","") for t in opacity]
		intensity=[s.replace("[","") for  s in intensity]   #[s.replace('8', '') for s in lst]
		intensity=[s.replace("]","") for  s in intensity]  
		intensity=[s.replace("'","") for  s in intensity]          
		print(intensity)
		print(opacity)
		#print(type(intensity[1]))
		
		self.pRenderer.readImgStack(rc)
		self.renderV()
		for count in range(1,len(intensity)):
                         
                         
                        intensity[count],opacity[count]=str(intensity[count]),str(opacity[count])
                        #intensity[count],opacity[count]=float(intensity[count]),float(opacity[count])
			self.addPoint(intensity[count],opacity[count])
	
	
	def saveVtkConfiguration(self , loadedDataInfo):
		if self.flag_stackRendered:
		
				rc=RenderConfiguration()
				intensity_list = []
				opacity_list = []
                                allRows = self.ui_m.tableWidget.rowCount()
                                rc.allrows=int(allRows)
    				for row in xrange(0,allRows):
    					intensity= self.ui_m.tableWidget.item(row,0)
    					opacity= self.ui_m.tableWidget.item(row,1)
    					#twi1 = self.ui_m.tableWidget.cellWidget(row,1)
    					#twi2 = self.ui_m.tableWidget.cellWidget(row,2)
    					#print (intensity.text() + " " +opacity.text()) 
					#print(type(intensity.text()))
					
					intensity =intensity.text()
					intensity=str(intensity)
					opacity = opacity.text()
					opacity = str(opacity)
					
				#intensity = intensity.split(",")
					intensity_list.append(intensity)
		   			opacity_list.append(opacity)
		   		
		   		
		   		#print(opacity_list)
				#print(intensity_list)
				#print(type(intensity_list))
				#opacity = opacity.text()
				rc.intensity =intensity_list
				rc.opacity = opacity_list
		
				
				
				
				self.fname = str(QtGui.QFileDialog.getSaveFileName(self.MainWindow, "Save File",os.getenv('HOME'),"Config"))+".cfg"		
				
				#file = open(fname,'w')
				#self.ls = LoadStack()
				
				data=rc.loadStackData()
				data=rc.intensityOpacity()
				print(data)
				with open(self.fname, 'w') as outfile:  
    					json.dump(data, outfile)
                               
                                
					
					
					
					
				
	def changeBGColor(self):
		if self.flag_stackRendered:
			color = QtGui.QColorDialog.getColor()
			self.pRenderer.renderWin.Render()
		
	
	def record(self):
		if self.flag_stackRendered:
			
			fname = str(QtGui.QFileDialog.getSaveFileName(self.MainWindow, "Save File",os.getenv('HOME'),"Images (*.png)"))
			fRate = int(self.ui_m.lineEdit_5.text())
			recTime = int(self.ui_m.lineEdit_4.text())
			nImg = fRate * recTime
			sTime = 1.0/fRate
			t1 = threading.Thread(target=self.task1, args=(fname,nImg,sTime))
			#t2 = threading.Thread(target=self.incPBar, args=(recTime,))
			t1.start()
			#t2.start()
			#timer = QtCore.QTimer()
			#self.ui_m.progressBar.connect(timer,SIGNAL("timeout()"),self.ui_m.progressBar,SLOT("incPBar()"))
			#timer.start(100) 
	"""@pyqtSlot()		
	def incPBar(self, recTime):
		currentTime = 0
		self.ui_m.progressBar.setRange(0, recTime)
		while	currentTime <= recTime:
			self.ui_m.progressBar.setValue(currentTime)
			time.sleep(0.5)
			currentTime += 0.5"""	
	
	def task1(self,fname,nImg,sTime):
		for i in range(0,nImg):
			#self.pRenderer.recorder.Write()
			self.pRenderer.snapshot(fname+str(i))
			time.sleep(sTime)
		print 'Done'

	def resetCamera(self):
		self.pRenderer.renderer.ResetCamera()
		self.pRenderer.renderer.GetActiveCamera().SetViewUp(0.0, 1.0, 0.0)
		self.pRenderer.renderWin.Render()



if __name__ == "__main__":

	Driver()

"""
This class takes care of the histogram widget. 
It provides function to apply color maps to the rendererd volume and also the histogram.
It also plots the alpha function over the histogram. 
"""


import sys
from PyQt4 import QtGui,QtCore
from ColorMapDialogUi import Ui_Dialog
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

class HistogramWidget(object):


	def showDialogBox(self, driver):
		# initialize the dialog with the UI designed in PColourMapDialogUi
		self.Dialog = QtGui.QDialog()
		self.ui_l = Ui_Dialog()
		self.ui_l.setupUi(self.Dialog)
		self.ui_l.lineEdit.setText(str(driver.cMin))
		self.ui_l.lineEdit_2.setText(str(driver.cMax))
		self.ui_l.lineEdit.setEnabled(False)
		self.ui_l.lineEdit_2.setEnabled(False)
		self.Dialog.show()
		self.d = driver
		self.ui_l.buttonBox.accepted.connect(self.accept)
		self.ui_l.radioButton.toggled.connect(self.enableSettingRange)
		
	def accept(self):
		self.d.cMin = int(self.ui_l.lineEdit.text())
		self.d.cMax = int(self.ui_l.lineEdit_2.text())
		colorMap = str(self.ui_l.comboBox.currentText())
		self.setColorMap(self.d.pRenderer.colorFunc, colorMap, self.d.cMin, self.d.cMax)
		self.plotHist(self.d, colorMap, self.d.cMin, self.d.cMax)
		
		# if the user sets the color resolution range, then the alpha function will reset or else only the color map will change (retaining the old aplha points)
		if self.ui_l.radioButton.isChecked() :
			# Now we add these cMin and cMax to the alpha function as we want that all the points other than this range should be transparent
			self.d.pRenderer.alphaChannelFunc.RemoveAllPoints()
			self.d.pRenderer.alphaChannelFunc.AddPoint(0, 0)
			if self.d.cMin != 0:
				self.d.pRenderer.alphaChannelFunc.AddPoint(self.d.cMin, 0)
			self.d.pRenderer.alphaChannelFunc.AddPoint(self.d.pRenderer.cMax, 1)
			if self.d.cMax != self.d.pRenderer.cMax:
				self.d.pRenderer.alphaChannelFunc.AddPoint(self.d.cMax, 1)
				self.d.pRenderer.alphaChannelFunc.AddPoint(self.d.cMax+1, 0)
				self.d.pRenderer.alphaChannelFunc.AddPoint(self.d.pRenderer.cMax, 0)
			# plot new alpha function on histogram
			self.d.histWidg.plotAlphaFunc(self.d.pRenderer.alphaChannelFunc,self.d.ax2,self.d.ui_m.canvas,self.d.pRenderer.cMin,self.d.pRenderer.cMax)	
			# We also want the values in table to change accordingly so we update the table too 
			self.d.alphaFuncPoints = {self.d.cMin:0.0, self.d.cMax:1.0}
			self.d.createTable()
		
		
		QtGui.QDialog.accept(self.Dialog)

	def enableSettingRange(self):
		if self.ui_l.radioButton.isChecked() :
			self.ui_l.lineEdit.setEnabled(True)
			self.ui_l.lineEdit_2.setEnabled(True)
		else:
			self.ui_l.radioButton.setChecked(True)
		

	def plotHist(self, driver, cName, cMin, cMax):
		driver.ax.clear()
		driver.ax.set_ylabel('Frequency')
		N, bins, patches = driver.ax.hist(driver.data, bins=np.linspace(cMin, cMax, 120),log = True, label = 'Gray values')
		# N is the count in each bin, bins is the lower-limit of the bin
		norm = colors.Normalize(bins.min(), bins.max())
		# set a color for every bar (patch) according 
		# to bin value from normalized min-max interval
		cm = plt.get_cmap(cName)
		
		for bin1, patch in zip(bins, patches):
		    color = cm(norm(bin1))
		    patch.set_facecolor(color)	
		driver.ui_m.canvas.draw()
		#to create a connection
		cid= driver.ui_m.canvas.mpl_connect('button_press_event',driver.onclick)
		 


	
	def plotAlphaFunc(self, func, ax, canvas, cMin, cMax):		# not working according to cMin-cMax of the color map 
		ax.clear()
		ax.set_ylabel('Opacity')
		data = np.empty((cMax+1,))
		for i in range(0,cMax+1):
			np.put(data,i,func.GetValue(i))
		ax.plot(data,color='red',linewidth=2.0)
		canvas.draw()



	def setColorMap(self, cFunc, cName, cMin, cMax):	# color map of volume 			
		cFunc.RemoveAllPoints()			# this resets the color function and removes old points, otherwise the old and new colormaps were getting overlapped
		cm = plt.get_cmap(cName)
		divs = np.linspace(cMin,cMax,256)
		norm1 = colors.Normalize(divs.min(), divs.max())
		for div in divs:		
			cc = cm(norm1(div))
			cFunc.AddRGBPoint(div,cc[0],cc[1],cc[2])
		





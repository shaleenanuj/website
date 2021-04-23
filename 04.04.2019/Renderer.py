""" 
This class will take the information of the image stack(such as it's path, number of images,etc.) from the LoadStack object or the vtkObj (pickle) and pass it to the VTK pipeline.
Volume default properties and functions(color and alpha) are defined here.
Volume will be mapped, rendered and the output will be given to the render window of vtkWidget.
All the other widgets like plane for clipping and slicing, clipping box and snapshot are defined here. 
"""

import pickle
import vtk
from HistogramWidget import HistogramWidget   # for applying color map

class Renderer:

		

	def readImgStack(self, loadedDataInfo):
	#def readVolume(self):
		# This function fetches the info of the image stack from PLoadStack object and reads it using the TiffReader
		self.reader = vtk.vtkTIFFReader()
		self.reader.SetFilePrefix(str(loadedDataInfo.dirPath+loadedDataInfo.filePrefix ))
		self.reader.SetFilePattern("%s%0"+str(loadedDataInfo.digits)+"d.tif")
		self.reader.SetFileNameSliceOffset(int(loadedDataInfo.offset))
		#ex = loadedDataInfo.extent
		#print(type(loadedDataInfo.imageNo-1))
		#print(loadedDataInfo.imageNo-1)
		self.reader.SetDataExtent(0,int(loadedDataInfo.extent_1),0,int(loadedDataInfo.extent_3),0,int(loadedDataInfo.imageNo))
		#self.reader.SetDataExtent(0,ex[1],0,1,0,loadedDataInfo.imageNo-1))
		self.reader.SetDataSpacing(loadedDataInfo.xSpace, loadedDataInfo.ySpace, loadedDataInfo.zSpace)
		self.reader.Update()
		# cMin,cMax default value for color resolution used in histogram and alpha function plot
		self.cMin = 0
		if self.reader.GetOutput().GetScalarRange()[1] > 255:
			self.cMax = 65535
		else:
			self.cMax = 255

		"""self.reader.SetFilePrefix("/home/pssarkar/Pranav/Small Data/reconstructed/img_Image")		# for default sample images # testing
		self.reader.SetFilePattern("%s%d.tif")
		self.reader.SetFileNameSliceOffset(13)
		self.reader.SetDataExtent(0,727,0,727,0,200)
		self.reader.SetDataSpacing(1,1,0.5)
		self.reader.Update()"""
	'''	

	def readVtkObj(self, fname):
	
		# This function fetches the info of the image stack from which has been already read and saved as vtkImageData
		"""self.reader = vtk.vtkImageReader()
		self.reader.SetFileName(fname)
		#ex = loadedDataInfo.getExtent()
		self.reader.SetDataExtent(0,727,0,727,0,100)
		self.reader.SetDataSpacing(1,1,0.5)
		self.reader.Update()"""
		with open(fname,'rb') as file:
			self.reader = pickle.load(fname)
		# cMin,cMax default value for color resolution used in histogram and alpha function plot
		self.cMin = 0
		if self.reader.GetOutput().GetScalarRange()[1] > 255:
			self.cMax = 65535
		else:
			self.cMax = 255
	'''

	def renderVolume(self, vtkWidget):
	#def renderVolume(self,vtkWidget,vtkWidgetXY):		
		
		#self.readVolume(loadedDataInfo)
		

		# The following class is used to store transparencyv-values for later retrival. In our case, we want the value 0 to be
		# completly opaque whereas the three different cubes are given different transperancy-values to show how it works.
		self.alphaChannelFunc = vtk.vtkPiecewiseFunction()
		self.alphaChannelFunc.AddPoint(self.cMin, 0)
		self.alphaChannelFunc.AddPoint(self.cMax, 1)

		# This class stores color data and can create color tables from a few color points. 
		self.colorFunc = vtk.vtkColorTransferFunction()

		self.histWidg = HistogramWidget()
		self.histWidg.setColorMap(self.colorFunc,'viridis',self.cMin,self.cMax)		# This function set the vslues for color function


		# The preavius two classes stored properties. Because we want to apply these properties to the volume we want to render,
		# we have to store them in a class that stores volume prpoperties.
		self.volumeProperty = vtk.vtkVolumeProperty()
		self.volumeProperty.SetColor(self.colorFunc)
		self.volumeProperty.SetScalarOpacity(self.alphaChannelFunc)

		# This class describes how the volume is rendered (through ray tracing).
		self.compositeFunction = vtk.vtkVolumeRayCastCompositeFunction()
		# We can finally create our volume. We also have to specify the data for it, as well as how the data will be rendered.
		self.volumeMapper = vtk.vtkVolumeRayCastMapper()
		self.volumeMapper.SetVolumeRayCastFunction(self.compositeFunction)
		self.volumeMapper.SetInput(self.reader.GetOutput())

		
		# The class vtkVolume is used to pair the preaviusly declared volume as well as the properties to be used when rendering that volume.
		self.volume = vtk.vtkVolume()
		self.volume.SetMapper(self.volumeMapper)
		self.volume.SetProperty(self.volumeProperty)


		# With almost everything else ready, its time to initialize the renderer and window, as well as creating a method for exiting the application
		self.renderer = vtk.vtkRenderer()

		self.renderWin = vtkWidget.GetRenderWindow()
		self.renderWin.AddRenderer(self.renderer)
		self.renderInteractor = vtkWidget.GetRenderWindow().GetInteractor()
		self.renderInteractor.SetRenderWindow(self.renderWin)


		# We add the volume to the renderer ...
		self.renderer.AddVolume(self.volume)
		
		# ... set background color to gray ...
		self.renderer.SetBackground(0.321, 0.349, 0.435)

		# ... and set window size.
		#self.renderWin.SetSize(800,800)      # in the UI of PMainWindow we have set "auto fill background" property of QVTKWidget to true, so no need to set the size


		# Setting up the Plane Widget which will be used for viewing the slice as well as a clipping plane
		self.planeWidget = vtk.vtkPlaneWidget()
		self.planeWidget.SetInteractor(self.renderInteractor)
		self.planeWidget.SetResolution(300)		# this can be changed by the user from the Ui
		self.planeWidget.SetPlaceFactor(1.15)
		self.planeWidget.SetInput(self.reader.GetOutput())
		self.planeWidget.PlaceWidget()


		# Code for slicing and clipping the volume

		self.plane = vtk.vtkPlane()		# vtkPlane is used to add the current plane as a clipping plane in vtkVolumeMapper
		self.planeWidget.GetPlane(self.plane)	# we get the current vtkPlane from the plane widget

		self.plane2 = vtk.vtkPolyData()		# vtkPolyData is used to get the slice and show it on the actor, tried this using the above vtkPlane, but didn't worked
		self.planeWidget.GetPolyData(self.plane2)
		self.planeWidget.SetRepresentationToOutline()

		# probe filter computes point attributes (e.g., scalars, vectors, etc.) at specified point positions. If not added, renders just a white plane
		self.probe = vtk.vtkProbeFilter()
		self.probe.SetInput(self.plane2)
		self.probe.SetSource(self.reader.GetOutput())

		self.contourMapper = vtk.vtkPolyDataMapper()
		self.contourMapper.SetInputConnection(self.probe.GetOutputPort())
		self.contourMapper.SetScalarRange(self.reader.GetOutput().GetScalarRange())
		self.contourMapper.SetLookupTable(self.colorFunc)	# this is like setting up the color map for the slice, we can directly pass the vtkColorFunction as a Lookup Table
		self.contourActor = vtk.vtkActor()
		self.contourActor.SetMapper(self.contourMapper)
		self.contourActor.VisibilityOff()		

		self.renderer.AddActor(self.contourActor)

		# Actually generate contour lines.
		def BeginInteraction(obj, event):
			obj.GetPolyData(self.plane2)
			self.contourActor.VisibilityOn()

		def ProbeData(obj, event):
			obj.GetPolyData(self.plane2)


		# Associate the widget with the interactor
		self.planeWidget.SetInteractor(self.renderInteractor)

		# Handle the events.
		self.planeWidget.AddObserver("EnableEvent", BeginInteraction)
		self.planeWidget.AddObserver("StartInteractionEvent", BeginInteraction)
		self.planeWidget.AddObserver("InteractionEvent", ProbeData)
		self.planeWidget.SetNormalToXAxis(True)
		


		# For getting the outline(3D box) around the object 
		outline = vtk.vtkOutlineFilter()
		outline.SetInput(self.reader.GetOutput())

		outlineMapper = vtk.vtkPolyDataMapper()
		outlineMapper.SetInputConnection(outline.GetOutputPort())

		self.outlineActor = vtk.vtkActor()
		self.outlineActor.SetMapper(outlineMapper)


		# We add outline actor to the renderer
		self.renderer.AddActor(self.outlineActor)


		# The Box widget
		# The SetInteractor method is how 3D widgets are associated with the
		# render window interactor. Internally, SetInteractor sets up a bunch
		# of callbacks using the Command/Observer mechanism (AddObserver()).
		self.boxWidget = vtk.vtkBoxWidget()
		self.boxWidget.SetInteractor(self.renderInteractor)
		self.boxWidget.SetPlaceFactor(1.0)

		# When interaction starts, the requested frame rate is increased.
		def StartInteraction(obj, event):
		    self.renderWin.SetDesiredUpdateRate(10)

		# When interaction ends, the requested frame rate is decreased to
		# normal levels. This causes a full resolution render to occur.
		def EndInteraction(obj, event):
		    self.renderWin.SetDesiredUpdateRate(0.001)

		# The implicit function vtkPlanes is used in conjunction with the
		# volume ray cast mapper to limit which portion of the volume is
		# volume rendered.
		self.planes = vtk.vtkPlanes()
		def ClipVolumeRender(obj, event):
		    obj.GetPlanes(self.planes)
		    self.volumeMapper.SetClippingPlanes(self.planes)


		# Place the interactor initially. The output of the reader is used to
		# place the box widget.
		self.boxWidget.SetInput(self.reader.GetOutput())
		self.boxWidget.PlaceWidget()
		self.boxWidget.InsideOutOn()
		self.boxWidget.AddObserver("StartInteractionEvent", StartInteraction)
		self.boxWidget.AddObserver("InteractionEvent", ClipVolumeRender)
		self.boxWidget.AddObserver("EndInteractionEvent", EndInteraction)

		self.outlineProperty = self.boxWidget.GetOutlineProperty()
		self.outlineProperty.SetRepresentationToWireframe()
		self.outlineProperty.SetAmbient(1.0)
		self.outlineProperty.SetAmbientColor(1, 1, 1)
		self.outlineProperty.SetLineWidth(3)

		self.selectedOutlineProperty = self.boxWidget.GetSelectedOutlineProperty()
		self.selectedOutlineProperty.SetRepresentationToWireframe()
		self.selectedOutlineProperty.SetAmbient(1.0)
		self.selectedOutlineProperty.SetAmbientColor(1, 0, 0)
		self.selectedOutlineProperty.SetLineWidth(3)


		# Add the actors to the renderer,		
		self.boxWidget.Off()

		# A simple function to be called when the user decides to quit the application.
		def exitCheck(obj, event):
			if obj.GetEventPending() != 0:
				obj.SetAbortRender(1)

		# Tell the application to use the function as an exit check.
		self.renderWin.AddObserver("AbortCheckEvent", exitCheck)


		self.alignedPlaneWidget = vtk.vtkImagePlaneWidget()
		self.alignedPlaneWidget.DisplayTextOn()
		self.alignedPlaneWidget.SetInput(self.reader.GetOutput())
		self.alignedPlaneWidget.SetPlaneOrientationToZAxes()
		self.alignedPlaneWidget.GetColorMap().SetLookupTable(self.colorFunc)
		self.prop3 = self.alignedPlaneWidget.GetPlaneProperty()
		self.prop3.SetColor(0, 0, 1)
		self.alignedPlaneWidget.SetInteractor(self.renderInteractor)
		#alignedPlaneWidget.On()


		axes = vtk.vtkAxesActor()

		self.widgetAxes = vtk.vtkOrientationMarkerWidget()
		#widget->SetOutlineColor( 0.9300, 0.5700, 0.1300 );
		self.widgetAxes.SetOrientationMarker( axes )
		self.widgetAxes.SetInteractor( self.renderInteractor )
		self.widgetAxes.SetViewport( 0.0, 0.0, 0.3, 0.3 )
		#self.widgetA.SetEnabled( 1 )
		#self.widgetA.InteractiveOff()
	
		
		# XY plot in another renderer window
		"""self.volumeMapperXY = vtk.vtkVolumeRayCastMapper()
		self.volumeMapperXY.SetVolumeRayCastFunction(self.compositeFunction)
		self.volumeMapperXY.SetInput(self.reader.GetOutput())

		self.volumeXY = vtk.vtkVolume()
		self.volumeXY.SetMapper(self.volumeMapper)
		self.volumeXY.SetProperty(self.volumeProperty)

		self.rendererXY = vtk.vtkRenderer()
		self.renderWinXY = vtkWidgetXY.GetRenderWindow()
		self.renderWinXY.AddRenderer(self.rendererXY)

		#self.rendererXY.AddVolume(self.volumeXY)
		self.rendererXY.SetBackground(0.321, 0.349, 0.435)
		self.renderWinXY.SetSize(724,724)
		
		self.xyActor = vtk.vtkActor2D()
		self.xyMapper = vtk.vtkPolyDataMapper2D()
		self.polyData = vtk.vtkPolyData()
		self.alignedPlaneWidget.GetPolyData(self.polyData)
		self.probe2 = vtk.vtkProbeFilter()
		self.probe2.SetInput(self.polyData)
		self.probe2.SetSource(self.reader.GetOutput())
		self.xyMapper.SetInputConnection(self.probe2.GetOutputPort())
		self.xyMapper.SetScalarRange(self.reader.GetOutput().GetScalarRange())
		self.xyMapper.SetLookupTable(self.colorFunc)
		self.xyActor.SetMapper(self.xyMapper)
		self.rendererXY.AddActor(self.xyActor)
		self.renderWinXY.Render()"""

		"""# create object of vtkFFMPEGWriter so as to record a avi of all the interactions done with visualized obj
		windowToImageFilter = vtk.vtkWindowToImageFilter()
		windowToImageFilter.SetInput(self.renderWin)
		windowToImageFilter.SetInputBufferTypeToRGBA()
		windowToImageFilter.ReadFrontBufferOff()
		windowToImageFilter.Update()
		self.recorder = vtk.vtkFFMPEGWriter()
		self.recorder.SetQuality(1)
		self.recorder.SetInput(windowToImageFilter.GetOutput())"""
		
		
		# Because nothing will be rendered without any input, we order the first render manually before control is handed over to the main-loop.
		self.renderInteractor.Initialize()
		self.renderWin.Render()
		self.renderer.ResetCamera()
		self.renderInteractor.Start()


	def renderBlank(self,vtkWidget):			# when initially the program loads this function is called, which just sets the background and renders no object
		self.renderer = vtk.vtkRenderer()
		self.renderWin = vtkWidget.GetRenderWindow()
		self.renderWin.AddRenderer(self.renderer)
		self.renderer.SetBackground(0.321, 0.349, 0.435)
		#self.renderWin.SetSize(800,800)
		self.renderWin.Render()


	def writeImageData(self,fname):
		writer = vtk.vtkImageWriter()
		writer.SetInput(self.reader.GetOutput())
		writer.SetFileName(fname)
		writer.SetFileDimensionality(3)
		writer.Write()


	def snapshot(self,fname):				# This funtion is used to take the snapshot of whatever is in the camera view of render window
		
		# WindowToImageFilter converts the render window view to an image writable format required for snapshot and recording
		w2if = vtk.vtkWindowToImageFilter()
		w2if.SetInput(self.renderWin)
		w2if.Update()

		writer = vtk.vtkPNGWriter()
		writer.SetFileName(fname)
		writer.SetInput(w2if.GetOutput())
		writer.Write()

	

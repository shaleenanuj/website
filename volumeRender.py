import vtk
import pickle
from numpy import *

# We begin by creating the data we want to render.
# For this tutorial, we create a 3D-image containing three overlaping cubes.
# This data can of course easily be replaced by data from a medical CT-scan or anything else three dimensional.
# The only limit is that the data must be reduced to unsigned 8 bit or 16 bit integers.
#data_matrix = zeros([75, 75, 75], dtype=uint8)
#data_matrix[0:35, 0:35, 0:35] = 50
#data_matrix[25:55, 25:55, 25:55] = 100
#data_matrix[45:74, 45:74, 45:74] = 150
try:
    
    with open('/home/nxpd/VTK/Image35.pickle','rb') as readData:
        I = pickle.load(readData)
    
except pickle.PickleError as pErr:
    print('Pickling error: '+ str(pErr))

data_matrix = I
print data_matrix
# For VTK to be able to use the data, it must be stored as a VTK-image. This can be done by the vtkImageImport-class which
# imports raw data and stores it.
dataImporter = vtk.vtkImageImport()
# The preaviusly created array is converted to a string of chars and imported.
data_string = data_matrix.tostring()
dataImporter.CopyImportVoidPointer(data_string, len(data_string))
# The type of the newly imported data is set to unsigned char (uint8)
dataImporter.SetDataScalarTypeToUnsignedChar()
# Because the data that is imported only contains an intensity value (it isnt RGB-coded or someting similar), the importer
# must be told this is the case.
dataImporter.SetNumberOfScalarComponents(1)
# The following two functions describe how the data is stored and the dimensions of the array it is stored in. For this
# simple case, all axes are of length 75 and begins with the first element. For other data, this is probably not the case.
# I have to admit however, that I honestly dont know the difference between SetDataExtent() and SetWholeExtent() although
# VTK complains if not both are used.
dataImporter.SetDataExtent(0, 727, 0,727,0,100)
dataImporter.SetWholeExtent(0, 727, 0,727,0,100)

dataImporter.Update()
print dataImporter.GetOutput().GetPointData().GetArray(0).GetRange()

# The following class is used to store transparencyv-values for later retrival. In our case, we want the value 0 to be
# completly opaque whereas the three different cubes are given different transperancy-values to show how it works.
alphaChannelFunc = vtk.vtkPiecewiseFunction()
alphaChannelFunc.AddPoint(0, 0.0)
#alphaChannelFunc.AddPoint(40000, 0.8)
#alphaChannelFunc.AddPoint(53000, 1.0)
#alphaChannelFunc.AddPoint(63001, 1.0)
#alphaChannelFunc.AddPoint(57000, 0.9)
#alphaChannelFunc.AddPoint(60000, 0.7)
#alphaChannelFunc.AddPoint(65553, 1.0)
alphaChannelFunc.AddPoint(225, 1.0)
alphaChannelFunc.AddPoint(255, 1.0)

# This class stores color data and can create color tables from a few color points. For this demo, we want the three cubes
# to be of the colors red green and blue.
colorFunc = vtk.vtkColorTransferFunction()
colorFunc.AddRGBPoint(0, 1.0, 1.0, 1.0)
#colorFunc.AddRGBPoint(40000, 0,0,0)
#colorFunc.AddRGBPoint(53000, 0,0,0)
#colorFunc.AddRGBPoint(53001, 1,1,1)
#colorFunc.AddRGBPoint(65553, 1.0, 1.0, 1.0)
colorFunc.AddRGBPoint(225, 1.0, 1.0, 1.0)
colorFunc.AddRGBPoint(255, 1.0, 1.0, 1.0)





# The preavius two classes stored properties. Because we want to apply these properties to the volume we want to render,
# we have to store them in a class that stores volume prpoperties.
volumeProperty = vtk.vtkVolumeProperty()
volumeProperty.SetColor(colorFunc)
volumeProperty.SetScalarOpacity(alphaChannelFunc)

# This class describes how the volume is rendered (through ray tracing).
compositeFunction = vtk.vtkVolumeRayCastCompositeFunction()
# We can finally create our volume. We also have to specify the data for it, as well as how the data will be rendered.
volumeMapper = vtk.vtkVolumeRayCastMapper()
volumeMapper.SetVolumeRayCastFunction(compositeFunction)
volumeMapper.SetInputConnection(dataImporter.GetOutputPort())

# The class vtkVolume is used to pair the preaviusly declared volume as well as the properties to be used when rendering that volume.
volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)


# With almost everything else ready, its time to initialize the renderer and window, as well as creating a method for exiting the application
renderer = vtk.vtkRenderer()

"""
contour=vtk.vtkContourFilter()
contour.SetInputConnection(dataImporter.GetOutputPort())
contour.SetNumberOfContours(1)
contour.SetValue(0,200)

mapper=vtk.vtkDataSetMapper()
mapper.SetInputConnection(contour.GetOutputPort())
actor=vtk.vtkActor()
actor.SetMapper(mapper)
renderer.AddActor(actor)
#renderer.Render()
renderer.ResetCamera()
"""

renderWin = vtk.vtkRenderWindow()
renderWin.AddRenderer(renderer)
renderInteractor = vtk.vtkRenderWindowInteractor()
renderInteractor.SetRenderWindow(renderWin)

# We add the volume to the renderer ...
#renderer.AddVolume(volume)

# ... set background color to white ...
renderer.SetBackground(0.5,0.5,0.7)
# ... and set window size.
renderWin.SetSize(800,800)

# A simple function to be called when the user decides to quit the application.
def exitCheck(obj, event):
    if obj.GetEventPending() != 0:
        obj.SetAbortRender(1)

# Tell the application to use the function as an exit check.
renderWin.AddObserver("AbortCheckEvent", exitCheck)

renderInteractor.Initialize()
# Because nothing will be rendered without any input, we order the first render manually before control is handed over to the main-loop.
renderWin.Render()

#print dataImporter.GetOutput().GetPointData().GetArray(0).GetRange()

renderInteractor.Start()


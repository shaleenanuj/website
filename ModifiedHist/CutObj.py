"""
This class will cut (/actually clip by adding a clipping plane) the rendered object based on the plane position of PlaneWidget.
Calling the  plane widget is necessary before calling the cut() method of this class.(which has been taken care of in the logic of Driver class)
"""

class CutObj:
 
	def cut(self,pRenderer):
		pRenderer.planeWidget.GetPlane(pRenderer.plane)
		pRenderer.volumeMapper.AddClippingPlane(pRenderer.plane)
		pRenderer.planeWidget.Off()
		pRenderer.renderWin.Render()



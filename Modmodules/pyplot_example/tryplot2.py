from matplotlib import pyplot as plt
import numpy as np
#import vtk


#np.random.seed(444)

class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)
        #self.rng=np.arrange(50)
       # self.rnd=np.random.randint(0,10,size=(3,rng.size))
        

    def __call__(self, event):
        print('click', event)
        if event.inaxes!=self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click to build line segments')
line, = ax.plot([0], [0])  # empty line
linebuilder = LineBuilder(line)

plt.show()


'''


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
		
		# refresh canvas
		self.ui_m.canvas.draw()


'''

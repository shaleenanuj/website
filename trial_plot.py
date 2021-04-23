
from matplotlib import pyplot as plt

class PointBuilder:
    def __init__(self, point):#initializing
        self.point = point
        self.xs = list(point.get_xdata())
        self.ys = list(point.get_ydata())
        self.cid = point.figure.canvas.mpl_connect('button_press_event', self)#connection id

    def __call__(self, event):
        print 'click', event
        if event.inaxes!=self.point.axes: return
       
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        
        #self.xs(event.xdata)
        #self.ys(event.ydata)
        print event.xdata
        print event.ydata
        
        self.point.set_data(self.xs, self.ys)
        self.point.figure.canvas.draw()
	
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click to build line segments')
point, = plt.scatter([5], [0])  # empty line
pointbuilder = PointBuilder(point)

plt.show()


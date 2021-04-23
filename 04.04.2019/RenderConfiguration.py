import json
class RenderConfiguration(object):
	class __RenderConfiguration:
		def __init__(self):
		
			self.dirPath=None
			self.filePrefix=None
			self.offset =None
			self.imageNo=None
			self.xSpace =None
			self.ySpace =None
			self.zSpace =None
			self.digits=None
			self.extent_1=None
			self.extent_3=None
			self.data ={}
			self.allrows=None
			self.intensity=[]
			self.opacity = []	
			
			
			
			
		
		def loadStackData(self):
	   		
	   	
			self.data['LoadStack'] = []  
			
			self.data['LoadStack'].append({  
    					'path': str(self.dirPath),
    					'image_prefix':str(self.filePrefix),
    					'offset':str(self.offset),
    					'imageNo':str(self.imageNo),
    					'digits':str(self.digits),
    					'extent_1':str(self.extent_1),
    					'extent_3':str(self.extent_3),
    					'xSpace':str(self.xSpace),
    					'ySpace':str(self.ySpace),
    					'zSpace':str(self.zSpace)
    					})
		
		'''
		def getIntensityOpacity(self):
		
			n=self.allrows
			for i in range(0,n):
			
					
				self.intensity.append(self.intensity)
				self.opacity.append(self.opacity)
				
		
		'''
		
		def intensityOpacity(self):
		
			n=self.allrows
			print(self.intensity)
			self.data['intensityOpacity'] = []
			
			
			self.data['intensityOpacity'].append({
						'intensity':str(self.intensity),
						'opacity':str(self.opacity)
				
				})
		
			return self.data	
		
		
			
	
	instance = None
	
	def __new__(cls): # __new__ always a classmethod
	        if not RenderConfiguration.instance:
	        	RenderConfiguration.instance = RenderConfiguration.__RenderConfiguration()
	        	print("new instance is assigned")
	            
	        else:
	        	print("old instance is set")
    
        	return RenderConfiguration.instance
		
'''		
x=VolumeConfiguration()

x.dirPath = "bag"
x.filePrefix = "fsr"
x.offset =56
x.imageNo=588
x.xSpace =0.1
x.ySpace =0.1
x.zSpace =0.1
y=VolumeConfiguration()
z=x.loadStackData()
	
#print(y.__dict__)
print(z)
#print(x.__dict__)
with open('data.txt', 'w') as outfile:  
   json.dump(z, outfile)	
'''		
		
		
		
		
				
		
		

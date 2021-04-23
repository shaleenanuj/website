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
			self.intensity= None
			self.opacity=None
			#self.digits=None
					
		def loadStackData(self):
	   		self.data = {}  
			self.data['LoadStack'] = []  
			self.data['LoadStack'].append({  
    					'path': str(self.dirPath),
    					'image_prefix':str(self.filePrefix),
    					'offset':str(self.offset),
    					'imageNo':str(self.imageNo),
    					'xSpace':str(self.xSpace),
    					'ySpace':str(self.ySpace),
    					'zSpace':str(self.zSpace)
					})
					
					
		def intensityAndOpacity(self):
		
			
		
			#return data
		
		#should we define another list for the intensity and opacity value ?
		#although it shouldn't affect as each image will be assigned a new file
		
		
		'''
		def __str__(self):
			return self.data	
		'''


	
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
		
		
		
		
				
		
		

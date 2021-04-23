import json

class VolumeConfiguration:
	class __VolumeConfiguration:
		def __init__(self,dirPath,filePrefix,offset,imageNo,xSpace,ySpace,zSpace):
		
			self.dirPath=dirPath
			self.filePrefix=filePrefix
			self.offset =offset
			self.imageNo=imageNo
			self.xSpace =xSpace
			self.ySpace =ySpace
			self.zSpace =zSpace
		
		def __str__(self):
			return	self.data		
	'''		
	def loadStackData(self):
		self.data = {}  
		self.data['LoadStack'] = []  
		self.data['LoadStack'].append({  
    				'path': str(self.dirPath),
    				'image_prefix':str(self.filrPreifx),
    				'offset':str(self.offset),
    				'imageNo':str(self.imageNo),
    				'xSpace':str(self.xSpace),
    				'ySpace':str(self.ySpace),
    				'zSpace':str(self.zSpace)
				})
		return self.data
	'''	
		
	instance = None
	
	def __new__(cls,dirPath,filePrefix,offset,imageNo,xSpace,ySpace,zSpace): # __new__ always a classmethod
	        if not VolumeConfiguration.instance:
	        	VoluneConfiguration.instance = __VolumeConfiguration()
	        	print("new instance is assigned")
	            
	        else:
	        	print("old instance is set")
    
        	return VolumeConfiguration.instance
		
		
x=VolumeConfiguration("bag","fsr",56,588,0.1,0.1,0.1)
'''
x.dirPath = "bag"
x.filePrefix = "fsr"
x.offset =56
x.imageNo=588
x.xSpace =0.1
x.ySpace =0.1
x.zSpace =0.1
#x.loadStackData()
'''			
print(x.__dict__)
with open('data.txt', 'w') as outfile:  
   json.dump(x.data, outfile)	
		
		
		
		
		
				
		
		

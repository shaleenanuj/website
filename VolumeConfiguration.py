import json
class VolumeConfiguration(object):
	class __VolumeConfiguration:
		def __init__(self):
		
			self.dirPath=None
			self.filePrefix=None
			self.offset =None
			self.imageNo=None
			self.xSpace =None
			self.ySpace =None
			self.zSpace =None
		
		def __str__(self):
			return self.data		
	
	instance = None
	
	def __new__(cls): # __new__ always a classmethod
	        if not VolumeConfiguration.instance:
	        	VolumeConfiguration.instance = VolumeConfiguration.__VolumeConfiguration()
	        	print("new instance is assigned")
	            
	        else:
	        	print("old instance is set")
    
        	return VolumeConfiguration.instance
		
		
x=VolumeConfiguration()

x.dirPath = "bag"
x.filePrefix = "fsr"
x.offset =56
x.imageNo=588
x.xSpace =0.1
x.ySpace =0.1
x.zSpace =0.1
y=VolumeConfiguration()
	
print(y.__dict__)

print(x.__dict__)
with open('data.txt', 'w') as outfile:  
   json.dump(x.__dict__, outfile)	
		
		
		
		
		
				
		
		

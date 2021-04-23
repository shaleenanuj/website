#DumpData.py
import json

class DumpData(object):

	def __init__(self,driver):
		# initialize the dialog with the UI designed in PLoadStackDialogUi
		self.driver = driver
	
	
	
	def dump_d(self):
	
			
		self.data = {}  
		slef.data['loadStack'] = []  
		self.data['loadStack'].append({  
    				'path': 'xyz',
    				'image prefix': 'img',
    				'offset': '3',
    				'number of images':'abc'
				})
				
		'''		
		data['people'].append({  
    				'name': 'Larry',
    				'website': 'google.com',
    				'from': 'Michigan'
				})
		data['people'].append({  
    				'name': 'Tim',
    				'website': 'apple.com',
    				'from': 'Alabama'
				})
		'''
		
	#def save_file(self):
	
	with open('data1.txt','w') as outfile: 
		
		json.dump(data , outfile)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

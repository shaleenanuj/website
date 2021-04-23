import pickle
import datetime
import time
class Logger(object):
	class __Logger:
	
		def __init__(self):
			
			
			print("in init")
			
		def log(self,action):
			
			log_dict = {}
				
			
			#import time
			ts = time.time()
			print(ts)
			
			#import datetime
			time_stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%b-%d %H:%M:%S')
		
			#print(time_stamp)
			
			log_string = (time_stamp + ' '+ action)
			
			f = open('data.log',"a")
			f.write(log_string + '\n')
	
	
	instance = None
	
	def __new__(cls):
		print("logger instance created")
		if not Logger.instance:
			Logger.instance = Logger.__Logger()
			
			
		return Logger.instance

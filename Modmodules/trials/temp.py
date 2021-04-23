
import glob
import os
import sys

def fileList(filePath):
	list1 = glob.glob(filePath+"*.tif")
	return list1


list = fileList('/home/pssarkar/Pranav/Graphite_recons_16bit/')
print(len(list)) #len() returns a txt value
 
filename_list = [] # for storing the basename
#list.sort()

#print list
#sys.exit()
image_prefix='' #alphabatical part of the basename
offset_list =[]
imageprefix_list = []
for index in range(len(list)):

	'''
	limit=list[index].rfind('/')
	str1=list[index].substring[0,limit]
	offset=list[index].substring[limit,len(list)]
	print str1
	'''
	
	
	filename_list = os.path.basename(list[index])#function to extract the basename
	
	#print(os.path.basename(list[index]))
	
	#image_prefix= []
	#offset= []				
	
	
	
	offset ='' #numerical part of the basename
	image_prefix='' #alphabatical part of the basename
	
	for c in range(len(filename_list)):
		
		if filename_list[c].isdigit():
			offset = offset + filename_list[c] 
					    	
		else:
			image_prefix = image_prefix + filename_list[c]	
	
				
	offset_list.append(offset + "  ")

	#filename_list.append(os.path.basename(list[index]))
#intoffset = map(int , offset_list)
offset_list.sort(key = int )
print(offset_list[0])

l = image_prefix.find('.')
print l 
image_prefix = image_prefix[0:l]
print (image_prefix)
#print (filename_list)

#print (sorted(filename_list, key=cmp_to_key(locale.strcoll)))
#print offset


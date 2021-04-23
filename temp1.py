# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:09:20 2019

@author: pssarkar
"""

import cv2
import numpy as np

img=cv2.imread('/home/pssarkar/Pranav/Graphite_recons_8bit/01.tif',1)
cv2.imshow('image',img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

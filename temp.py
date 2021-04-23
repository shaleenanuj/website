# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:37:59 2019

@author: pssarkar
"""

import cv2
import numpy as nm
img=cv2.imread('cameraman.tif',0)
cv2.imshow('abs',img)
cv2.waitkey(0)
cv2.destroyAllWindows()

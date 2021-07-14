# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 17:06:01 2021

@author: uqgpere2
"""


import sys
import string 
import os
import math
import traceback
import glob
import itertools

import openpyxl
from openpyxl import Workbook


import arcpy
from arcpy.sa import *

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Allow output to overwrite...
arcpy.env.overwriteOutput = True

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

#%%

shape_file_path = r'C:\00-C-GPM_INFO\04-C-RDM\04-C-02-Python\04-C-02-03-TSFs-Exposure\09-Results-shapes\EXPOSURE_SHPs\GFPLAIN_1_exposure_simplified.shp'
field_to_modify = ['RASTERVALU']

#%%  

with arcpy.da.UpdateCursor(shape_file_path, field_to_modify) as cursor:
  for row in cursor:
      if row[0] <0: # this is a simple conditional assuming the column is float()
          row[0] = 0
      cursor.updateRow(row)


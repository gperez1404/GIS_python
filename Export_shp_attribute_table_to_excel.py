# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:19:57 2020

This Script extarcts the attribute table from a shapefile to an excel file 
This excel file has headings and can be loaded as a dataframe in R or Python

@author: uqgpere2
"""

###############################################################################
#               IMPORTANT REMARKS BEFORE RUNNING THIS SCRIPT
###############################################################################

# This script can only be run on Python 2.7 shell or under Spyder using ArcGIS's
# Python 2.7 as interpreter :

#  C:\Python27\ArcGIS10.7\python.exe

# This script imports arcpy so you need to have ArcGIS installed and with license

###############################################################################
#  ^    ^     ^  IMPORTANT REMARKS BEFORE RUNNING THIS MODEL    ^    ^     ^  
###############################################################################

###############################################################################
#                        PACKAGES YOU NEED TO LOAD
###############################################################################
#%% 
# These are the packages you need to load files
import os
import sys
import string
import math
import traceback
import glob
import arcpy
from arcpy.sa import *
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Allow output to overwrite...
arcpy.env.overwriteOutput = True

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

#%%
###############################################################################
#  ^  ^  ^  ^  ^  ^  ^   PACKAGES YOU NEED TO LOAD       ^  ^  ^  ^  ^  ^  ^ 
###############################################################################


###############################################################################
#                       DEFINITION OF FILE LOCATIONS
###############################################################################
#%%
# Path of the main folder for the simulations
current_working_directory=r'C:/00-C-GPM_INFO/04-C-RDM/04-C-02-Python/04-C-02-03-TSFs-Exposure'    

# FOLDER NAMES----------------------------------------------------------------

# Folder name with inputs files
Input_files_folder_name= r'04-Inputs-files'

# Folder name with input rasters
Input_rasters_folder_name= r'05-Inputs-rasters'

# Folder name with input shapefiles
Input_shapes_folder_name= r'06-Inputs-shapes'


# the output files folder
Output_files_folder_name= r'07-Results-files'

# Folder name with output shapefiles
Output_rasters_folder_name= r'08-Results-rasters'

# Folder name with output rasters
Output_shapes_folder_name= r'09-Results-shapes'

# Folder Names for intermediate results
Conditional_rasters_Folder_name = "CONDITIONAL_RASTERS_CTs"                  

# FOLDER PATHS-----------------------------------------------------------------

#  #  #  #  #
#  Inputs
# #  #  #  #

# Path to input files:
Inputpath_files= os.path.join(current_working_directory,Input_files_folder_name)

# Path to input shapes:
Inputpath_shapes= os.path.join(current_working_directory,Input_shapes_folder_name)

# Path to input rasters:
Inputpath_rasters= os.path.join(current_working_directory,Input_rasters_folder_name)


#  #  #  #  #
#  Outputs
# #  #  #  #

# Path to files shapes:
OutPath_files= os.path.join(current_working_directory,Output_files_folder_name)

# Path to raster results:
OutPath_rasters= os.path.join(current_working_directory,Output_rasters_folder_name)

# Path to shapefile results:
OutPath_shapes= os.path.join(current_working_directory,Output_shapes_folder_name)


# FILE NAMES-------------------------------------------------------------------

# The shapefile you want to convert to excel
shape= r'TSFs_with_IDs_paper.shp'

new_extension='.dbf'

filename, ext = os.path.splitext(shape)

shape_table= filename + new_extension

extension_result='.xls'

output_attribute_table_name= filename + extension_result

# here you create the paths to the attribute table and the results
input_attribute_table=os.path.join(Inputpath_shapes,shape_table)

output_attribute_table=os.path.join(OutPath_files,output_attribute_table_name)
#%%
###############################################################################
# ^  ^  ^  ^  ^  ^  ^  DEFINITION OF FILE  LOCATIONS ^  ^  ^  ^  ^  ^  ^  ^  ^
###############################################################################
###############################################################################
#                            Pre - run procedures
###############################################################################

# Allow outputs to overwrite...
arcpy.env.overwriteOutput = True

#Checkout Spatial Analyst extension
arcpy.AddMessage("Checking license... ")
if arcpy.CheckExtension("Spatial") == "Available":
    arcpy.CheckOutExtension("Spatial")
    arcpy.AddMessage("Spatial Analyst license checked out... ")
else:
    arcpy.AddMessage("Spatial Analyst license needed... ")
    raise LicenseError

###############################################################################
#      ^       ^      ^     pre- run procedures    ^       ^      ^    
###############################################################################


###############################################################################
#                                CONVERSION
###############################################################################

# convert the attribute table of a shapefile into an Excel table
arcpy.TableToExcel_conversion(input_attribute_table, output_attribute_table)


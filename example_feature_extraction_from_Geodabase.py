# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 15:20:47 2021

@author: uqgpere2
"""


# references: 

# https://gist.github.com/d-wasserman/e9c98be1d0caebc2935afecf0ba239a0
# https://gis.stackexchange.com/questions/130240/opening-table-from-file-geodatabase-in-arcpy

import sys
import os
import traceback
import glob
import itertools

import openpyxl
from openpyxl import Workbook

import arcpy
from arcpy import env
from arcpy.sa import *

import pandas as pd

#Allow output to overwrite...
arcpy.env.overwriteOutput = True

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

###############################################################################
#                                                              Nested functions        
###############################################################################

"""This function will convert an arcgis table into a pandas dataframe with an object ID index, and the selected
    input fields. Uses TableToNumPyArray to get initial data.
    :param - in_fc - input feature class or table to convert
    :param - input_fields - fields to input into a da numpy converter function /if none tehn covnerts all fields
    :param - query - sql like query to filter out records returned
    :param - skip_nulls - skip rows with null values
    :param - null_values - values to replace null values with.
    :returns - pandas dataframe"""
    
def table_to_data_frame(in_table, input_fields=None, where_clause=None):

    OIDFieldName = arcpy.Describe(in_table).OIDFieldName
    if input_fields:
        final_fields = [OIDFieldName] + input_fields
    else:
        final_fields = [field.name for field in arcpy.ListFields(in_table)]
    data = [row for row in arcpy.da.SearchCursor(in_table, final_fields, where_clause=where_clause)]
    fc_dataframe = pd.DataFrame(data, columns=final_fields)
    fc_dataframe = fc_dataframe.set_index(OIDFieldName, drop=True)
    return fc_dataframe

###############################################################################
# Nested functions        ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^
###############################################################################

#%%
# here you need to paste the location of the Geodatabase:
env.workspace = r"C:\00-C-GPM_INFO\04-C-RDM\04-C-02-Python\04-C-02-00-Tutorials\01-Input-files\TSFs_data.gdb"

# locations to save the shps files and the excel files:
outLocation =r'C:\00-C-GPM_INFO\04-C-RDM\04-C-02-Python\04-C-02-00-Tutorials\05-Output-Shapefiles'

# here you get all the feature elements inside the gdb:
List_of_shps_files_inside_the_gdb = arcpy.ListFeatureClasses()
print(List_of_shps_files_inside_the_gdb)

#%%
# Here you create individual shapefiles for all the features inside the dbf 
arcpy.FeatureClassToShapefile_conversion (List_of_shps_files_inside_the_gdb, outLocation)

#%%
# Here you create individual shp fiels for each feature and extart the attribute 
# table into an excel file. You can then load the excel files as pandas dataframes or yu can load them in R
x=0
for dataset in List_of_shps_files_inside_the_gdb:
     
     dataset_name=str(List_of_shps_files_inside_the_gdb[x])    
     shp_name= dataset_name+r'.shp'
     attribute_table_name= dataset_name+r'.dbf'
     excel_name=dataset_name + r'.xls'
     
     shp_location= os.path.join(outLocation,shp_name)
     arcpy.FeatureClassToShapefile_conversion (dataset, outLocation)
     
     attribute_table_location=os.path.join(outLocation,attribute_table_name)
     excel_file_location=os.path.join(outLocation,excel_name)
     # here you convert the attribute table into an excel file
     arcpy.TableToExcel_conversion(attribute_table_location, excel_file_location)
     
     x=x+1
     print('attribute table exported successfully !')

     
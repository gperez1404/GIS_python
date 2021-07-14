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


# here you need to paste the location of the Geodatabase:
env.workspace = r"C:\data....location of the .gdb"

# here you get all the ".dbf" elements:

List_of_dbf_files_inside_the_gdb = arcpy.ListTables("*")

#this loop goes over all the dbf elements

for dataset in List_of_dbf_files_inside_the_gdb:
     with arcpy.da.SearchCursor(dataset, "*") as currrent_dbf:
         
         # here you convert the dbf into a pandas dataframe:
         
         df_table= table_to_data_frame(currrent_dbf)
         
         # You can save a pandas df asexcel or you can also print it on console
         print(df_table)
         df_table.to_csv(r'C:\ locations to save...', index=False, encoding='utf-8')
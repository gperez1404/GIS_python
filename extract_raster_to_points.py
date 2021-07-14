# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 22:59:30 2020

@author: uqgpere2
"""


# Input_parameters:
#
#                   Input_points_filepath
#                   Input_raster_filepath
#                   Output_points_filepath
#                   Distance


# Example of Syntaxis
#arcpy.ExtractValuesToPoints(in_point_features, in_raster, out_point_features, {interpolate_values}, {add_attributes})
    
#Arguments:
#in_point_features      The input point features defining the locations from which 
#                       you want to extract the raster cell values. 
                   
#in_raster              The raster dataset whose values will be extracted. 

#out_point_features     The output point feature dataset containing the extracted raster values. 

#interpolate_values     Specifies whether or not interpolation will be used.
#                       "INTERPOLATE"
#                       "NONE"    

#add_attributes         Determines if the raster attributes are written to the output point feature dataset.
#                       "ALL"
#                       "VALUE_ONLY-- > recomended 
    

def raster_values_to_points(Input_points_filepath,Input_raster_filepath,Output_points_filepath):
    #Import system modules
    import arcpy
    from arcpy.sa import *
    from datetime import datetime
    
    
    # Allow output to overwrite...
    arcpy.env.overwriteOutput = True
    
    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    
    arcpy.sa.xtractValuesToPoints(Input_points_filepath,Input_raster_filepath,Output_points_filepath,"INTERPOLATE","VALUE_ONLY")

    
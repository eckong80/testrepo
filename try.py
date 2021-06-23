# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:10:41 2018

@author: kongee
"""

# search keyword MASTER_CURVE in LampControlTraces.log & get datetime
import csv

with open('LampControlTraces.log', 'r') as lampfile:
    lamp_trace = csv.reader(lampfile, delimiter = ',')
    for row in lamp_trace:
        if row[1] == 'MASTER_CURVE_PWM':
            print (row[0])
            #print (row[1])
    
    
# use datetime and search in ThermoCamera_filtered.log
    
    
    
# print or get data from column 7
    

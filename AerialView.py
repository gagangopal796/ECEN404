# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:30:54 2021

@author: kenny
"""
#image is only collected on return path at altitude of 16ft
#Units given in inches or feet
#Will be grayscale in 403, but upgraded to RGB in 404

#modules
import csv
import numpy

#this block will be replaced with actual inputs from drone in 404
#import image as csv
AerialInput = numpy.zeros((1400, 32), dtype = int)
AerialTemp = numpy.zeros((100, 32), dtype = int)

openTestCase = open('TwoDfile.csv', 'r')
csvReader = csv.reader(openTestCase)
AerialInput = list(csvReader)

#create new csv for final output
AerialOut = "AerialOut.csv"
AerialOutt = open(AerialOut, 'w', newline = '\n')
writeArialOut = csv.writer(AerialOutt)
AerialFinal =  numpy.zeros((1400, 32), dtype = int)

#cut horizontal slice based on assumed speed of 5 feet per second
# This is the main portion of the file, where I take snippets then stitch
i = 0
while i < 14: #will be converted to time instead of distance in 404
    r = 0
    #below loop will be subject of most "tinkering in 404 to accomoadate flight
    #path and speed
    #below loop is a simulated screenshot that captures partial snip of path
    while r < 100:
        j = 0
        while (j < 32):
            AerialTemp[r][j] = AerialInput[r + (i * 100)][j]
            j += 1
        r +=1
    #below loop writes "stitches" screenshot snip to matrix
    r = 0
    while r < 100:
        j = 0
        while (j < 32):
            AerialFinal[r + (i * 100)][j] = AerialTemp[r][j]
            j += 1
        r +=1
    i += 1

#add slice to new image csv
writeArialOut.writerows(AerialFinal)

#close files
AerialOutt.close()
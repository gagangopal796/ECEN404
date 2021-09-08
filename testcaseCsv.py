# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:42:59 2021

@author: kenny
"""

#Units given in inches or feet
#Resolution is assumed to be uniformly 1 square foot

#modules
import random
import csv


#A linear 1400 feet will be surveyed, corresponding to 1400 rows of data points
#The drone can detect objects at a radius of 16 feet
#This corresponds to a column width of 32 data points

#fill sheet with expected floor value of 0 in
allDataList = []
i = 0
while i < 1400:
    allDataList.append([0] * 32)
    i +=1
    
    
#objects to detect 

#uncomment to test singular object
#objectList = ['car1']

objectList = ['car1','car2', 'tallTree', 'medTree', 'firehydrant', 'wall1', 
              'wall2', 'wall3', 'building1', 'building2', 'building3', 'box1',
              'box2', 'circle']
    
#car1
#15ft by 6ft
def car1(startRow, startCol):
    if (((startRow + 14) < 1400) and ((startCol + 5) < 32 )):
        allDataList[startRow][startCol] = 36
        allDataList[startRow][startCol + 1] = 36
        allDataList[startRow][startCol + 2] = 36
        allDataList[startRow][startCol + 3] = 36
        allDataList[startRow][startCol + 4] = 36
        allDataList[startRow][startCol + 5] = 36
    
        allDataList[startRow + 1][startCol] = 36
        allDataList[startRow + 1][startCol + 1] = 36
        allDataList[startRow + 1][startCol + 2] = 36
        allDataList[startRow + 1][startCol + 3] = 36
        allDataList[startRow + 1][startCol + 4] = 36
        allDataList[startRow + 1][startCol + 5] = 36
     
        allDataList[startRow + 2][startCol] = 48
        allDataList[startRow + 2][startCol + 1] = 48
        allDataList[startRow + 2][startCol + 2] = 48
        allDataList[startRow + 2][startCol + 3] = 48
        allDataList[startRow + 2][startCol + 4] = 48
        allDataList[startRow + 2][startCol + 5] = 48
        
        allDataList[startRow + 3][startCol] = 60
        allDataList[startRow + 3][startCol + 1] = 60
        allDataList[startRow + 3][startCol + 2] = 60
        allDataList[startRow + 3][startCol + 3] = 60
        allDataList[startRow + 3][startCol + 4] = 60
        allDataList[startRow + 3][startCol + 5] = 60
        
        allDataList[startRow + 4][startCol] = 60
        allDataList[startRow + 4][startCol + 1] = 60
        allDataList[startRow + 4][startCol + 2] = 60
        allDataList[startRow + 4][startCol + 3] = 60
        allDataList[startRow + 4][startCol + 4] = 60
        allDataList[startRow + 4][startCol + 5] = 60
    
        allDataList[startRow + 5][startCol] = 60
        allDataList[startRow + 5][startCol + 1] = 60
        allDataList[startRow + 5][startCol + 2] = 60
        allDataList[startRow + 5][startCol + 3] = 60
        allDataList[startRow + 5][startCol + 4] = 60
        allDataList[startRow + 5][startCol + 5] = 60
    
        allDataList[startRow + 6][startCol] = 60
        allDataList[startRow + 6][startCol + 1] = 60
        allDataList[startRow + 6][startCol + 2] = 60
        allDataList[startRow + 6][startCol + 3] = 60
        allDataList[startRow + 6][startCol + 4] = 60
        allDataList[startRow + 6][startCol + 5] = 60
        
        allDataList[startRow + 7][startCol] = 60
        allDataList[startRow + 7][startCol + 1] = 60
        allDataList[startRow + 7][startCol + 2] = 60
        allDataList[startRow + 7][startCol + 3] = 60
        allDataList[startRow + 7][startCol + 4] = 60
        allDataList[startRow + 7][startCol + 5] = 60
        
        allDataList[startRow + 8][startCol] = 60
        allDataList[startRow + 8][startCol + 1] = 60
        allDataList[startRow + 8][startCol + 2] = 60
        allDataList[startRow + 8][startCol + 3] = 60
        allDataList[startRow + 8][startCol + 4] = 60
        allDataList[startRow + 8][startCol + 5] = 60
        
        allDataList[startRow + 9][startCol] = 60
        allDataList[startRow + 9][startCol + 1] = 60
        allDataList[startRow + 9][startCol + 2] = 60
        allDataList[startRow + 9][startCol + 3] = 60
        allDataList[startRow + 9][startCol + 4] = 60
        allDataList[startRow + 9][startCol + 5] = 60
    
        allDataList[startRow + 10][startCol] = 60
        allDataList[startRow + 10][startCol + 1] = 60
        allDataList[startRow + 10][startCol + 2] = 60
        allDataList[startRow + 10][startCol + 3] = 60
        allDataList[startRow + 10][startCol + 4] = 60
        allDataList[startRow + 10][startCol + 5] = 60
        
        allDataList[startRow + 11][startCol] = 60
        allDataList[startRow + 11][startCol + 1] = 60
        allDataList[startRow + 11][startCol + 2] = 60
        allDataList[startRow + 11][startCol + 3] = 60
        allDataList[startRow + 11][startCol + 4] = 60
        allDataList[startRow + 11][startCol + 5] = 60
        
        allDataList[startRow + 12][startCol] = 48
        allDataList[startRow + 12][startCol + 1] = 48
        allDataList[startRow + 12][startCol + 2] = 48
        allDataList[startRow + 12][startCol + 3] = 48
        allDataList[startRow + 12][startCol + 4] = 48
        allDataList[startRow + 12][startCol + 5] = 48
        
        allDataList[startRow + 13][startCol] = 36
        allDataList[startRow + 13][startCol + 1] = 36
        allDataList[startRow + 13][startCol + 2] = 36
        allDataList[startRow + 13][startCol + 3] = 36
        allDataList[startRow + 13][startCol + 4] = 36
        allDataList[startRow + 13][startCol + 5] = 36
    
        allDataList[startRow + 14][startCol] = 36
        allDataList[startRow + 14][startCol + 1] = 36
        allDataList[startRow + 14][startCol + 2] = 36
        allDataList[startRow + 14][startCol + 3] = 36
        allDataList[startRow + 14][startCol + 4] = 36
        allDataList[startRow + 14][startCol + 5] = 36
   
#car2
#6ft by 15ft
def car2(startRow, startCol):
    if (((startRow + 5) < 1400) and ((startCol + 14) < 32 )):
        allDataList[startRow][startCol] = 36
        allDataList[startRow][startCol + 1] = 36
        allDataList[startRow][startCol + 2] = 36
        allDataList[startRow][startCol + 3] = 48
        allDataList[startRow][startCol + 4] = 60
        allDataList[startRow][startCol + 5] = 60  
        allDataList[startRow][startCol + 6] = 60
        allDataList[startRow][startCol + 7] = 60
        allDataList[startRow][startCol + 8] = 60
        allDataList[startRow][startCol + 9] = 60
        allDataList[startRow][startCol + 10] = 60
        allDataList[startRow][startCol + 11] = 60
        allDataList[startRow][startCol + 12] = 48
        allDataList[startRow][startCol + 13] = 36
        allDataList[startRow][startCol + 14] = 36

        allDataList[startRow + 1][startCol] = 36
        allDataList[startRow + 1][startCol + 1] = 36
        allDataList[startRow + 1][startCol + 2] = 36
        allDataList[startRow + 1][startCol + 3] = 48
        allDataList[startRow + 1][startCol + 4] = 60
        allDataList[startRow + 1][startCol + 5] = 60   
        allDataList[startRow + 1][startCol + 6] = 60
        allDataList[startRow + 1][startCol + 7] = 60
        allDataList[startRow + 1][startCol + 8] = 60
        allDataList[startRow + 1][startCol + 9] = 60
        allDataList[startRow + 1][startCol + 10] = 60
        allDataList[startRow + 1][startCol + 11] = 60
        allDataList[startRow + 1][startCol + 12] = 48
        allDataList[startRow + 1][startCol + 13] = 36
        allDataList[startRow + 1][startCol + 14] = 36
 
        allDataList[startRow + 2][startCol] = 36
        allDataList[startRow + 2][startCol + 1] = 36
        allDataList[startRow + 2][startCol + 2] = 36
        allDataList[startRow + 2][startCol + 3] = 48
        allDataList[startRow + 2][startCol + 4] = 60
        allDataList[startRow + 2][startCol + 5] = 60   
        allDataList[startRow + 2][startCol + 6] = 60
        allDataList[startRow + 2][startCol + 7] = 60
        allDataList[startRow + 2][startCol + 8] = 60
        allDataList[startRow + 2][startCol + 9] = 60
        allDataList[startRow + 2][startCol + 10] = 60
        allDataList[startRow + 2][startCol + 11] = 60
        allDataList[startRow + 2][startCol + 12] = 48
        allDataList[startRow + 2][startCol + 13] = 36
        allDataList[startRow + 2][startCol + 14] = 36
        
        allDataList[startRow + 3][startCol] = 36
        allDataList[startRow + 3][startCol + 1] = 36
        allDataList[startRow + 3][startCol + 2] = 36
        allDataList[startRow + 3][startCol + 3] = 48
        allDataList[startRow + 3][startCol + 4] = 60
        allDataList[startRow + 3][startCol + 5] = 60   
        allDataList[startRow + 3][startCol + 6] = 60
        allDataList[startRow + 3][startCol + 7] = 60
        allDataList[startRow + 3][startCol + 8] = 60
        allDataList[startRow + 3][startCol + 9] = 60
        allDataList[startRow + 3][startCol + 10] = 60
        allDataList[startRow + 3][startCol + 11] = 60
        allDataList[startRow + 3][startCol + 12] = 48
        allDataList[startRow + 3][startCol + 13] = 36
        allDataList[startRow + 3][startCol + 14] = 36
        
        allDataList[startRow + 4][startCol] = 36
        allDataList[startRow + 4][startCol + 1] = 36
        allDataList[startRow + 4][startCol + 2] = 36
        allDataList[startRow + 4][startCol + 3] = 48
        allDataList[startRow + 4][startCol + 4] = 60
        allDataList[startRow + 4][startCol + 5] = 60   
        allDataList[startRow + 4][startCol + 6] = 60
        allDataList[startRow + 4][startCol + 7] = 60
        allDataList[startRow + 4][startCol + 8] = 60
        allDataList[startRow + 4][startCol + 9] = 60
        allDataList[startRow + 4][startCol + 10] = 60
        allDataList[startRow + 4][startCol + 11] = 60
        allDataList[startRow + 4][startCol + 12] = 48
        allDataList[startRow + 4][startCol + 13] = 36
        allDataList[startRow + 4][startCol + 14] = 36
        
        allDataList[startRow + 5][startCol] = 36
        allDataList[startRow + 5][startCol + 1] = 36
        allDataList[startRow + 5][startCol + 2] = 36
        allDataList[startRow + 5][startCol + 3] = 48
        allDataList[startRow + 5][startCol + 4] = 60
        allDataList[startRow + 5][startCol + 5] = 60   
        allDataList[startRow + 5][startCol + 6] = 60
        allDataList[startRow + 5][startCol + 7] = 60
        allDataList[startRow + 5][startCol + 8] = 60
        allDataList[startRow + 5][startCol + 9] = 60
        allDataList[startRow + 5][startCol + 10] = 60
        allDataList[startRow + 5][startCol + 11] = 60
        allDataList[startRow + 5][startCol + 12] = 48
        allDataList[startRow + 5][startCol + 13] = 36
        allDataList[startRow + 5][startCol + 14] = 36
        
#tallTree
#15 feet tall
def tallTree(startRow, startCol):
    if (((startRow + 2) < 1400) and ((startCol + 2) < 32 )):
        allDataList[startRow][startCol] = 96
        allDataList[startRow][startCol + 1] = 96
        allDataList[startRow][startCol + 2] = 96
        allDataList[startRow + 1][startCol] = 96
        allDataList[startRow + 1][startCol + 1] = 180
        allDataList[startRow + 1][startCol + 2] = 96
        allDataList[startRow + 2][startCol] = 96
        allDataList[startRow + 2][startCol + 1] = 96
        allDataList[startRow + 2][startCol + 2] = 96
        
#medTree
#12 feet tall
def medTree(startRow, startCol):
    if (((startRow + 2) < 1400) and ((startCol + 2) < 32 )):
        allDataList[startRow][startCol] = 96
        allDataList[startRow][startCol + 1] = 96
        allDataList[startRow][startCol + 2] = 96
        allDataList[startRow + 1][startCol] = 96
        allDataList[startRow + 1][startCol + 1] = 144
        allDataList[startRow + 1][startCol + 2] = 96
        allDataList[startRow + 2][startCol] = 96
        allDataList[startRow + 2][startCol + 1] = 96
        allDataList[startRow + 2][startCol + 2] = 96
    
#firehydrant (30 inch tall)
def firehydrant(startRow, startCol):
    if (((startRow) < 1400) and ((startCol) < 32 )):
        allDataList[startRow][startCol] = 30

#wall1
#parallelwall (8 foot high wall)
def wall1(startRow, startCol):
    if (((startRow) < 1400) and ((startCol + 5) < 32 )):
        allDataList[startRow][startCol] = 84
        allDataList[startRow][startCol + 1] = 84
        allDataList[startRow][startCol + 2] = 84
        allDataList[startRow][startCol + 3] = 84
        allDataList[startRow][startCol + 4] = 84
        allDataList[startRow][startCol + 5] = 84

#wall2
#perpendicular wall (8 foot high wall)
def wall2(startRow, startCol):
    if (((startRow + 5) < 1400) and ((startCol) < 32 )):
        allDataList[startRow][startCol] = 84
        allDataList[startRow + 1][startCol] = 84
        allDataList[startRow + 2][startCol] = 84
        allDataList[startRow + 3][startCol] = 84
        allDataList[startRow + 4][startCol] = 84
        allDataList[startRow + 5][startCol] = 84 
    
#wall3
#Diagonal wall (8 foot high wall)
def wall3(startRow, startCol):
    if (((startRow + 4) < 1400) and ((startCol + 3) < 32 )):
        allDataList[startRow + 1][startCol] = 84
        allDataList[startRow + 1][startCol + 1] = 84
        allDataList[startRow + 2][startCol + 1] = 84
        allDataList[startRow + 2][startCol + 2] = 84
        allDataList[startRow + 3][startCol + 3] = 84
        allDataList[startRow + 4][startCol + 3] = 84 
    
#building1
#big building (10ft by 10ft and 30ft tall)
def building1(startRow, startCol):
    if (((startRow + 10) < 1400) and ((startCol + 10) < 32 )):
        allDataList[startRow][startCol] = 360
        allDataList[startRow][startCol + 1] = 360
        allDataList[startRow][startCol + 2] = 360
        allDataList[startRow][startCol + 3] = 360
        allDataList[startRow][startCol + 4] = 360
        allDataList[startRow][startCol + 5] = 360
        allDataList[startRow][startCol + 6] = 360
        allDataList[startRow][startCol + 7] = 360
        allDataList[startRow][startCol + 8] = 360
        allDataList[startRow][startCol + 9] = 360
        allDataList[startRow + 1][startCol] = 360
        allDataList[startRow + 1][startCol + 1] = 360
        allDataList[startRow + 1][startCol + 2] = 360
        allDataList[startRow + 1][startCol + 3] = 360
        allDataList[startRow + 1][startCol + 4] = 360
        allDataList[startRow + 1][startCol + 5] = 360
        allDataList[startRow + 1][startCol + 6] = 360
        allDataList[startRow + 1][startCol + 7] = 360
        allDataList[startRow + 1][startCol + 8] = 360
        allDataList[startRow + 1][startCol + 9] = 360
        allDataList[startRow + 2][startCol] = 360
        allDataList[startRow + 2][startCol + 1] = 360
        allDataList[startRow + 2][startCol + 2] = 360
        allDataList[startRow + 2][startCol + 3] = 360
        allDataList[startRow + 2][startCol + 4] = 360
        allDataList[startRow + 2][startCol + 5] = 360
        allDataList[startRow + 2][startCol + 6] = 360
        allDataList[startRow + 2][startCol + 7] = 360
        allDataList[startRow + 2][startCol + 8] = 360
        allDataList[startRow + 2][startCol + 9] = 360
        allDataList[startRow + 3][startCol] = 360
        allDataList[startRow + 3][startCol + 1] = 360
        allDataList[startRow + 3][startCol + 2] = 360
        allDataList[startRow + 3][startCol + 3] = 360
        allDataList[startRow + 3][startCol + 4] = 360
        allDataList[startRow + 3][startCol + 5] = 360
        allDataList[startRow + 3][startCol + 6] = 360
        allDataList[startRow + 3][startCol + 7] = 360
        allDataList[startRow + 3][startCol + 8] = 360
        allDataList[startRow + 3][startCol + 9] = 360
        allDataList[startRow + 4][startCol] = 360
        allDataList[startRow + 4][startCol + 1] = 360
        allDataList[startRow + 4][startCol + 2] = 360
        allDataList[startRow + 4][startCol + 3] = 360
        allDataList[startRow + 4][startCol + 4] = 360
        allDataList[startRow + 4][startCol + 5] = 360
        allDataList[startRow + 4][startCol + 6] = 360
        allDataList[startRow + 4][startCol + 7] = 360
        allDataList[startRow + 4][startCol + 8] = 360
        allDataList[startRow + 4][startCol + 9] = 360 
        allDataList[startRow + 5][startCol] = 360
        allDataList[startRow + 5][startCol + 1] = 360
        allDataList[startRow + 5][startCol + 2] = 360
        allDataList[startRow + 5][startCol + 3] = 360
        allDataList[startRow + 5][startCol + 4] = 360
        allDataList[startRow + 5][startCol + 5] = 360
        allDataList[startRow + 5][startCol + 6] = 360
        allDataList[startRow + 5][startCol + 7] = 360
        allDataList[startRow + 5][startCol + 8] = 360
        allDataList[startRow + 5][startCol + 9] = 360
        allDataList[startRow + 6][startCol] = 360
        allDataList[startRow + 6][startCol + 1] = 360
        allDataList[startRow + 6][startCol + 2] = 360
        allDataList[startRow + 6][startCol + 3] = 360
        allDataList[startRow + 6][startCol + 4] = 360
        allDataList[startRow + 6][startCol + 5] = 360
        allDataList[startRow + 6][startCol + 6] = 360
        allDataList[startRow + 6][startCol + 7] = 360
        allDataList[startRow + 6][startCol + 8] = 360
        allDataList[startRow + 6][startCol + 9] = 360
        allDataList[startRow + 7][startCol] = 360
        allDataList[startRow + 7][startCol + 1] = 360
        allDataList[startRow + 7][startCol + 2] = 360
        allDataList[startRow + 7][startCol + 3] = 360
        allDataList[startRow + 7][startCol + 4] = 360
        allDataList[startRow + 7][startCol + 5] = 360
        allDataList[startRow + 7][startCol + 6] = 360
        allDataList[startRow + 7][startCol + 7] = 360
        allDataList[startRow + 7][startCol + 8] = 360
        allDataList[startRow + 7][startCol + 9] = 360
        allDataList[startRow + 8][startCol] = 360
        allDataList[startRow + 8][startCol + 1] = 360
        allDataList[startRow + 8][startCol + 2] = 360
        allDataList[startRow + 8][startCol + 3] = 360
        allDataList[startRow + 8][startCol + 4] = 360
        allDataList[startRow + 8][startCol + 5] = 360
        allDataList[startRow + 8][startCol + 6] = 360
        allDataList[startRow + 8][startCol + 7] = 360
        allDataList[startRow + 8][startCol + 8] = 360
        allDataList[startRow + 8][startCol + 9] = 360
        allDataList[startRow + 9][startCol] = 360
        allDataList[startRow + 9][startCol + 1] = 360
        allDataList[startRow + 9][startCol + 2] = 360
        allDataList[startRow + 9][startCol + 3] = 360
        allDataList[startRow + 9][startCol + 4] = 360
        allDataList[startRow + 9][startCol + 5] = 360
        allDataList[startRow + 9][startCol + 6] = 360
        allDataList[startRow + 9][startCol + 7] = 360
        allDataList[startRow + 9][startCol + 8] = 360
        allDataList[startRow + 9][startCol + 9] = 360

#building2
#med building (10ft by 10ft by 10ft)
def building2(startRow, startCol):
    if (((startRow + 10) < 1400) and ((startCol + 10) < 32 )):
        allDataList[startRow][startCol] = 120
        allDataList[startRow][startCol + 1] = 120
        allDataList[startRow][startCol + 2] = 120
        allDataList[startRow][startCol + 3] = 120
        allDataList[startRow][startCol + 4] = 120
        allDataList[startRow][startCol + 5] = 120
        allDataList[startRow][startCol + 6] = 120
        allDataList[startRow][startCol + 7] = 120
        allDataList[startRow][startCol + 8] = 120
        allDataList[startRow][startCol + 9] = 120
        allDataList[startRow + 1][startCol] = 120
        allDataList[startRow + 1][startCol + 1] = 120
        allDataList[startRow + 1][startCol + 2] = 120
        allDataList[startRow + 1][startCol + 3] = 120
        allDataList[startRow + 1][startCol + 4] = 120
        allDataList[startRow + 1][startCol + 5] = 120
        allDataList[startRow + 1][startCol + 6] = 120
        allDataList[startRow + 1][startCol + 7] = 120
        allDataList[startRow + 1][startCol + 8] = 120
        allDataList[startRow + 1][startCol + 9] = 120
        allDataList[startRow + 2][startCol] = 120
        allDataList[startRow + 2][startCol + 1] = 120
        allDataList[startRow + 2][startCol + 2] = 120
        allDataList[startRow + 2][startCol + 3] = 120
        allDataList[startRow + 2][startCol + 4] = 120
        allDataList[startRow + 2][startCol + 5] = 120
        allDataList[startRow + 2][startCol + 6] = 120
        allDataList[startRow + 2][startCol + 7] = 120
        allDataList[startRow + 2][startCol + 8] = 120
        allDataList[startRow + 2][startCol + 9] = 120
        allDataList[startRow + 3][startCol] = 120
        allDataList[startRow + 3][startCol + 1] = 120
        allDataList[startRow + 3][startCol + 2] = 120
        allDataList[startRow + 3][startCol + 3] = 120
        allDataList[startRow + 3][startCol + 4] = 120
        allDataList[startRow + 3][startCol + 5] = 120
        allDataList[startRow + 3][startCol + 6] = 120
        allDataList[startRow + 3][startCol + 7] = 120
        allDataList[startRow + 3][startCol + 8] = 120
        allDataList[startRow + 3][startCol + 9] = 120
        allDataList[startRow + 4][startCol] = 120
        allDataList[startRow + 4][startCol + 1] = 120
        allDataList[startRow + 4][startCol + 2] = 120
        allDataList[startRow + 4][startCol + 3] = 120
        allDataList[startRow + 4][startCol + 4] = 120
        allDataList[startRow + 4][startCol + 5] = 120
        allDataList[startRow + 4][startCol + 6] = 120
        allDataList[startRow + 4][startCol + 7] = 120
        allDataList[startRow + 4][startCol + 8] = 120
        allDataList[startRow + 4][startCol + 9] = 120      
        allDataList[startRow + 5][startCol] = 120
        allDataList[startRow + 5][startCol + 1] = 120
        allDataList[startRow + 5][startCol + 2] = 120
        allDataList[startRow + 5][startCol + 3] = 120
        allDataList[startRow + 5][startCol + 4] = 120
        allDataList[startRow + 5][startCol + 5] = 120
        allDataList[startRow + 5][startCol + 6] = 120
        allDataList[startRow + 5][startCol + 7] = 120
        allDataList[startRow + 5][startCol + 8] = 120
        allDataList[startRow + 5][startCol + 9] = 120
        allDataList[startRow + 6][startCol] = 120
        allDataList[startRow + 6][startCol + 1] = 120
        allDataList[startRow + 6][startCol + 2] = 120
        allDataList[startRow + 6][startCol + 3] = 120
        allDataList[startRow + 6][startCol + 4] = 120
        allDataList[startRow + 6][startCol + 5] = 120
        allDataList[startRow + 6][startCol + 6] = 120
        allDataList[startRow + 6][startCol + 7] = 120
        allDataList[startRow + 6][startCol + 8] = 120
        allDataList[startRow + 6][startCol + 9] = 120
        allDataList[startRow + 7][startCol] = 120
        allDataList[startRow + 7][startCol + 1] = 120
        allDataList[startRow + 7][startCol + 2] = 120
        allDataList[startRow + 7][startCol + 3] = 120
        allDataList[startRow + 7][startCol + 4] = 120
        allDataList[startRow + 7][startCol + 5] = 120
        allDataList[startRow + 7][startCol + 6] = 120
        allDataList[startRow + 7][startCol + 7] = 120
        allDataList[startRow + 7][startCol + 8] = 120
        allDataList[startRow + 7][startCol + 9] = 120
        allDataList[startRow + 8][startCol] = 120
        allDataList[startRow + 8][startCol + 1] = 120
        allDataList[startRow + 8][startCol + 2] = 120
        allDataList[startRow + 8][startCol + 3] = 120
        allDataList[startRow + 8][startCol + 4] = 120
        allDataList[startRow + 8][startCol + 5] = 120
        allDataList[startRow + 8][startCol + 6] = 120
        allDataList[startRow + 8][startCol + 7] = 120
        allDataList[startRow + 8][startCol + 8] = 120
        allDataList[startRow + 8][startCol + 9] = 120
        allDataList[startRow + 9][startCol] = 120
        allDataList[startRow + 9][startCol + 1] = 120
        allDataList[startRow + 9][startCol + 2] = 120
        allDataList[startRow + 9][startCol + 3] = 120
        allDataList[startRow + 9][startCol + 4] = 120
        allDataList[startRow + 9][startCol + 5] = 120
        allDataList[startRow + 9][startCol + 6] = 120
        allDataList[startRow + 9][startCol + 7] = 120
        allDataList[startRow + 9][startCol + 8] = 120
        allDataList[startRow + 9][startCol + 9] = 120
    
#building3
#small building (5ft by 5ft and 10ft tall)
def building3(startRow, startCol):
    if (((startRow + 4) < 1400) and ((startCol + 4) < 32 )):
        allDataList[startRow][startCol] = 120
        allDataList[startRow][startCol + 1] = 120
        allDataList[startRow][startCol + 2] = 120
        allDataList[startRow][startCol + 3] = 120
        allDataList[startRow][startCol + 4] = 120
        allDataList[startRow + 1][startCol] = 120
        allDataList[startRow + 1][startCol + 1] = 120
        allDataList[startRow + 1][startCol + 2] = 120
        allDataList[startRow + 1][startCol + 3] = 120
        allDataList[startRow + 1][startCol + 4] = 120
        allDataList[startRow + 2][startCol] = 120
        allDataList[startRow + 2][startCol + 1] = 120
        allDataList[startRow + 2][startCol + 2] = 120
        allDataList[startRow + 2][startCol + 3] = 120
        allDataList[startRow + 2][startCol + 4] = 120
        allDataList[startRow + 3][startCol] = 120
        allDataList[startRow + 3][startCol + 1] = 120
        allDataList[startRow + 3][startCol + 2] = 120
        allDataList[startRow + 3][startCol + 3] = 120
        allDataList[startRow + 3][startCol + 4] = 120
        allDataList[startRow + 4][startCol] = 120
        allDataList[startRow + 4][startCol + 1] = 120
        allDataList[startRow + 4][startCol + 2] = 120
        allDataList[startRow + 4][startCol + 3] = 120
        allDataList[startRow + 4][startCol + 4] = 120     
        
#box1
#small box 2ft by 2ft box
def box1(startRow, startCol):
    if (((startRow + 1) < 1400) and ((startCol + 1) < 32 )):
        allDataList[startRow][startCol] = 48
        allDataList[startRow][startCol + 1] = 48
        allDataList[startRow + 1][startCol] = 48
        allDataList[startRow + 1][startCol + 1] = 48

#box2
#big box 4ft by 4ft box by 4ft
def box2(startRow, startCol):
    if (((startRow + 3) < 1400) and ((startCol + 3) < 32 )):
        allDataList[startRow][startCol] = 48
        allDataList[startRow][startCol + 1] = 48
        allDataList[startRow][startCol + 2] = 48
        allDataList[startRow][startCol + 3] = 48
        allDataList[startRow + 1][startCol] = 48
        allDataList[startRow + 1][startCol + 1] = 48
        allDataList[startRow + 1][startCol + 2] = 48
        allDataList[startRow + 1][startCol + 3] = 48
        allDataList[startRow + 2][startCol] = 48
        allDataList[startRow + 2][startCol + 1] = 48
        allDataList[startRow + 2][startCol + 2] = 48
        allDataList[startRow + 2][startCol + 3] = 48
        allDataList[startRow + 3][startCol] = 48
        allDataList[startRow + 3][startCol + 1] = 48
        allDataList[startRow + 3][startCol + 2] = 48
        allDataList[startRow + 3][startCol + 3] = 48

#circle object
#uniform height circule
def circle(startRow, startCol):
    if (((startRow + 5) < 1400) and ((startCol + 14) < 32 )):
        allDataList[startRow][startCol] = 48
        allDataList[startRow][startCol + 1] = 48
        allDataList[startRow][startCol + 2] = 48
        allDataList[startRow][startCol + 3] = 48
        allDataList[startRow + 1][startCol] = 48
        allDataList[startRow + 1][startCol + 1] = 48
        allDataList[startRow + 1][startCol + 2] = 48
        allDataList[startRow + 1][startCol + 3] = 48
        allDataList[startRow + 2][startCol] = 48
        allDataList[startRow + 2][startCol + 1] = 48
        allDataList[startRow + 2][startCol + 2] = 48
        allDataList[startRow + 2][startCol + 3] = 48


#place objects randomly         
rows2 = 1
emptyRow = [0] * 1395
while (rows2 < 1395):
    emptyRowCount = 1
    while emptyRowCount < 32:
        emptyRow[rows2 - 1] += allDataList[rows2 - 1][emptyRowCount]
        emptyRowCount += 1
    if emptyRow[rows2 - 1] == 0:
        functionChoice = random.choice(objectList)
        eval(functionChoice + '(rows2, random.randint(0,32))')
        #substitute below below for above to test single objects
        #randomCol = random.randint(0,32)
        #car2(rows2, randomCol)
    rows2 += 1


#write array to usuable excel file
y = "TwoDfile.csv"
finalFile = open(y, 'w', newline = '\n')
write = csv.writer(finalFile)
write.writerows(allDataList)

#confirm code has run
print("finished")  
     
#close file
finalFile.close()
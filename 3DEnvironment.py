# -*- coding: utf-8 -*-
"""
@author: Ken Good
"""

#modules
import time
import csv
import math
import numpy


#trip information
#2,640 feet forward, then backwards => 5280 feet
#total flight time = 15 min => 900 seconds
#pace = 5280 / 900 => 5.86 ft per second

#distance in feet (single direction)
Distance_Surveyed = 800
#time in seconds (roundtrip) excluding turn time
Alloted_time = 20
#pace in feet per second
Pace = Distance_Surveyed * 2 / Alloted_time

#start program
print("Type 'Y' and 'Enter' to start")
status = input()
Flight = False
if status == 'y' or 'Y':
    Flight = True

#intake data
#collect data once per foot
Data = numpy.zeros((Distance_Surveyed + 1, 5), dtype = int)
Distance_Count = -1
while (Flight == True):
    time.sleep(1 / Pace)
    Distance_Count += 1
    #read data from sensors
    Left_Sensor = 1
    Middle_Sensor = 2
    Right_Sensor = 3
    
    #write data to array
    if Distance_Count <= Distance_Surveyed:
        Data[Distance_Count][1] = Left_Sensor
        Data[Distance_Count][2] = Middle_Sensor
        Data[Distance_Count][3] = Right_Sensor
    if Distance_Count >= Distance_Surveyed:
        Data[Distance_Surveyed - Distance_Count][0] = Left_Sensor
        Data[Distance_Surveyed - Distance_Count][4] = Right_Sensor

    if (Distance_Count % 500 == 0) and (Distance_Count < Distance_Surveyed):
        print(str(Distance_Count) + " Feet")
    if ((Distance_Surveyed - Distance_Count) < 100) and (Distance_Count % 20 == 0) and (Distance_Count <= Distance_Surveyed):
        print(str(Distance_Count) + " Feet")
        print("prepare to stop")
    if Distance_Count == Distance_Surveyed:
        print("Stop")
        print("Turn and Reach elevation in... \n10")
        time.sleep(1)
        print("9")
        time.sleep(1)
        print("8")
        time.sleep(1)
        print("7")
        time.sleep(1)
        print("6")
        time.sleep(1)
        print("5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Walk") 
    if Distance_Count >= Distance_Surveyed * 2:
        Flight = False
print("Flight complete")

#write array to usuable excel file
y = "TwoDfile.csv"
finalFile = open(y, 'w', newline = '\n')
write = csv.writer(finalFile)
write.writerows(Data)





#
#
#       3D Environment Construction
#         (Distance Calculations)
#
#

#8 foot flyby
#convert test case to drone scan information
#this will not be necessary for actual implementation
openTestCase = open('TwoDfile.csv', 'r')
csvReader = csv.reader(openTestCase)
eightFtTest = list(csvReader)

openTestCase = open('TwoDfile.csv', 'r')
csvReader = csv.reader(openTestCase)
TwoDCopy = list(csvReader)

#Line of sight (LOS) determines minimum height of object to be detected at a distance
#below block sets threshold for detection
#eightFtLOS = list(eightFtTest)
eightFtLOS = numpy.zeros((Distance_Surveyed, 32), dtype = int)

i = 0
while i < Distance_Surveyed:
    j = 8
    while (j > 7) and (j < 25):
        #Left Sensor
        if j < 15:
            eightFtLOS[i][j] = (96 /8) * (j - 8)
            
        #Middle Sensor
        elif (j == 16):
            eightFtLOS[i][j] = 0
            
        #Right Sensor
        elif j > 16:
            eightFtLOS[i][j] = 96 - ((96/8) * (j - 16))
        j += 1
    i += 1

i = 0
while i < Distance_Surveyed:
    j = 8
    while (j > 7) and (j < 25):
        #Left Sensor
        if (j < 16) and (int(eightFtTest[i][j]) > int(eightFtLOS[i][j])):
            eightFtTest[i][j] = math.sqrt(2) * (96 - int(eightFtLOS[i][j]))
            
        elif (j < 16) and not(int(eightFtTest[i][j]) > int(eightFtLOS[i][j])):
            eightFtTest[i][j] = 0
            
        #Middle Sensor
        elif (j == 16) and (int(eightFtTest[i][j]) > int(eightFtLOS[i][j])):
            eightFtTest[i][j] = eightFtTest[i][j]

        #Right Sensor
        elif j > 16  and (int(eightFtTest[i][j]) > int(eightFtLOS[i][j])):
            eightFtTest[i][j] = math.sqrt(2) * (96 - int(eightFtLOS[i][j]))
            
        elif (j < 16) and not(int(eightFtTest[i][j]) > int(eightFtLOS[i][j])):
            eightFtTest[i][j] = 0
        j += 1
    i += 1

#write array to usuable excel file
eight = "EightFtTest.csv"
eightFt = open(eight, 'w', newline = '\n')
write = csv.writer(eightFt)
write.writerows(eightFtTest)

#input and claculation

#confirm code has run
print("finished")  
     
#close file
eightFt.close()


#16 foot flyby


#convert test case to drone scan information
#this will not be necessary for actual implementation
#below block sets threshold for detection
sixteenFtTest = list(eightFtTest)

sixteenFtLOS = numpy.zeros((Distance_Surveyed, 32), dtype = int)

i = 0
while i < Distance_Surveyed:
    j = 0
    while (j < 32):
        #Left Sensor
        if j < 8:
            sixteenFtLOS[i][j] = (192 /16) * (j)
            
        #Right Sensor
        elif j > 24:
            sixteenFtLOS[i][j] = 192 - ((192/16) * (j - 16))
        j += 1
    i += 1

i = 0
while i < Distance_Surveyed:
    j = 0
    while (j < 32):
        #Left Sensor
        if (j < 8) and (int(sixteenFtTest[i][j]) > int(sixteenFtLOS[i][j])):
            sixteenFtTest[i][j] = math.sqrt(2) * (192 - int(sixteenFtLOS[i][j]))
            
        elif (j < 8) and not(int(sixteenFtTest[i][j]) > int(sixteenFtLOS[i][j])):
            sixteenFtTest[i][j] = 0
            
        #Right Sensor
        elif ((j > 24) and (j < 32))  and (int(sixteenFtTest[i][j]) > int(sixteenFtLOS[i][j])):
            sixteenFtTest[i][j] = math.sqrt(2) * (192 - int(sixteenFtLOS[i][j]))
            
        elif ((j > 24) and (j < 32))  and not(int(sixteenFtTest[i][j]) > int(sixteenFtLOS[i][j])):
            sixteenFtTest[i][j] = 0
        j += 1
    i += 1

#write array to usuable excel file
sixteen = "sixteenFtTest.csv"
sixteenFt = open(sixteen, 'w', newline = '\n')
write = csv.writer(sixteenFt)
write.writerows(sixteenFtTest)


#grab sensor input (simulated by grabbing points from above data set)
#iterate through data and writes it if it is in los
SensorArray = numpy.zeros((Distance_Surveyed, 5), dtype = int)

#for 8ft pass
i = 0
while i < Distance_Surveyed:
    j = 8
    jLeft = 0
    jRight = 32
    while (j > 7) and (j < 25):
        #Left Sensor
        if (j < 15) and (sixteenFtTest[i][j] != 0) and (j > jLeft):
            SensorArray[i][1] = sixteenFtTest[i][j]
            jLeft = j
            
        #Middle Sensor
        elif (j == 16):
            SensorArray[i][2] = sixteenFtTest[i][j]
            
        #Right Sensor
        elif (j > 16) and (sixteenFtTest[i][j] != 0) and (j < jRight):
            SensorArray[i][3] = sixteenFtTest[i][j]
            jRight = j
        j += 1
    i += 1
    
#for 16ft pass
i = 0
while i < Distance_Surveyed:
    j = 0
    jLeft = 0
    jRight = 32
    while (j < 32):
        #Left Sensor
        if (j < 8) and (sixteenFtTest[i][j] != 0) and (j > jLeft):
            SensorArray[i][0] = sixteenFtTest[i][j]
            jLeft = j
            
        #Right Sensor
        elif (j > 24) and (j < 32) and (sixteenFtTest[i][j] != 0) and (j < jRight):
            SensorArray[i][4] = sixteenFtTest[i][j]
            jRight = j
        j += 1
    i += 1


SensorValues = "SensorInput.csv"
SensorTemp = open(SensorValues, 'w', newline = '\n')
write = csv.writer(SensorTemp)
write.writerows(SensorArray)


#Sensor Data Processing (convert to height and distance)
#Height Array
ObjectHeight  = numpy.zeros((Distance_Surveyed, 5), dtype = int) 
i = 0
while i < Distance_Surveyed:
    j = 0
    while (j < 5):
        if j == 0:
            if SensorArray[i][j] == 0:
                ObjectHeight[i][j] = 0
            else:
                ObjectHeight[i][j] = 192 - (SensorArray[i][j] / math.sqrt(2))
        if j == 1:
            if SensorArray[i][j] == 0:
                ObjectHeight[i][j] = 0
            else:
               ObjectHeight[i][j] = 96 - (SensorArray[i][j] / math.sqrt(2))
        if j == 2:
            ObjectHeight[i][j] = SensorArray[i][j]
        if j == 3:
            if SensorArray[i][j] == 0:
                ObjectHeight[i][j] = 0
            else:
                ObjectHeight[i][j] = 96 - (SensorArray[i][j] / math.sqrt(2))
        if j == 4:
            if SensorArray[i][j] == 0:
                ObjectHeight[i][j] = 0
            else:
                ObjectHeight[i][j] = 192 - (SensorArray[i][j] / math.sqrt(2))
        j += 1
    i += 1
    
ObjHeight = "ObjectHeight.csv"
HeightTemp = open(ObjHeight, 'w', newline = '\n')
write = csv.writer(HeightTemp)
write.writerows(ObjectHeight)

#Distance Array
#Saves distances as coordinate points
#these 5 data points are representative of the actual inputs that will be received
#(one for each sensor per pass)
ObjectDistance  = numpy.zeros((Distance_Surveyed, 5), dtype = int) 
i = 0
while i < Distance_Surveyed:
    j = 0
    while (j < 5):
        if j == 0:
            if SensorArray[i][j] == 0:
                ObjectDistance[i][j] = 0
            else:
                ObjectDistance[i][j] = int (16 - ( (SensorArray[i][j] / math.sqrt(2))) /12)
        if j == 1:
            if SensorArray[i][j] == 0:
                ObjectDistance[i][j] = 0
            else:
               ObjectDistance[i][j] = int (16 - ( (SensorArray[i][j] / math.sqrt(2)))/12)
        if j == 2:
           ObjectDistance[i][j] = 16
        if j == 3:
            if SensorArray[i][j] == 0:
                ObjectDistance[i][j] = 0
            else:
                ObjectDistance[i][j] = int (16 + ((SensorArray[i][j] / math.sqrt(2)))/12)
        if j == 4:
            if SensorArray[i][j] == 0:
                ObjectDistance[i][j] = 0
            else:
                ObjectDistance[i][j] = int(16 +  ((SensorArray[i][j] / math.sqrt(2)))/12)
        j += 1
    i += 1
    
ObjDistance = "ObjectDistance.csv"
DistanceTemp = open(ObjDistance, 'w', newline = '\n')
write = csv.writer(DistanceTemp)
write.writerows(ObjectDistance)


#seperate objects from background with thresholding in 404
#threshold ground (remove objects smaller than 2 feet tall)


#pick out objects from background and 
i = 1
ObjectRow = numpy.zeros((1000), dtype = int) #max area of detectable object is 1000 Square feet
ObjectCol = numpy.zeros((1000), dtype = int)
ObjectArray = numpy.zeros((Distance_Surveyed, 32), dtype = int)
TwoDCopy = list(numpy.float_(TwoDCopy))

#TwoDCopy is assumed simulated data, but in 404 will be inputs from
#image recognition subsystem.
c = 0
while c < Distance_Surveyed:
    d = 0
    while d < 32:
        if d < 8:
            if  (ObjectDistance[c][0] > 0) and (TwoDCopy[c][d] != 0):
                ObjectArray[c][d]  = ObjectHeight[c][0]
        if d > 7 and d < 16:
            if  (ObjectDistance[c][1] > 0) and (TwoDCopy[c][d] != 0):
                ObjectArray[c][d]  = ObjectHeight[c][1]
        if d == 16:
            if  (ObjectDistance[c][2] > 0) and (TwoDCopy[c][d] != 0):
                ObjectArray[c][d]  = ObjectHeight[c][2]
        if d > 16 and d < 24:
            if  (ObjectDistance[c][3] > 0) and (TwoDCopy[c][d] != 0):
                ObjectArray[c][d]  = ObjectHeight[c][3]
        if d > 23:
            if  (ObjectDistance[c][4] > 0) and (TwoDCopy[c][d] != 0):
                ObjectArray[c][d] = ObjectHeight[c][4]
        d += 1
    c += 1

#write array to usuable excel file
ObjectsFinal = "ObjectsFinal.csv"
ObjectTemp = open(ObjectsFinal, 'w', newline = '\n')
write = csv.writer(ObjectTemp)
write.writerows(ObjectArray)



#apply uniform height to seperated objects


ObjectTemp.close()
sixteenFt.close()

#confirm code has run
print("finished1") 

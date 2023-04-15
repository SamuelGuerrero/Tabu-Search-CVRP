import numpy as np

def getData(lenData):
    data = []
    for i in np.arange(lenData):
        data.append([])
        data[i].append(-1)
        data[i].append([-1,-1])
        data[i].append(-1)
    
    return data

def convertListCharToString(listChar):
    new = ""
    for x in listChar:
        new += x
    return new


def getCVRPFileData(namePath):
    with open(namePath) as f:
        file = f.readlines()

    string = convertListCharToString(file)

    stringDimensions = "DIMENSION : "
    dimensionsIndex  = string.find(stringDimensions) + len(stringDimensions)
    dimension = ""

    while(string[dimensionsIndex] != '\n'):
        dimension += string[dimensionsIndex]
        dimensionsIndex += 1

    dimension = int(dimension)
    data = getData(dimension)
    stringCord = "NODE_COORD_SECTION" 
    initialIndex = string.find(stringCord) + len(stringCord) + 2
    indicator = 0

    i = 0
    while(string[initialIndex] != 'D'):
        number = ""
        while(ord(string[initialIndex]) != 32 and string[initialIndex] != '\n'):
            number += string[initialIndex]
            initialIndex += 1
        if(len(number) > 0):        
            if indicator == 0:
                data[i][0] = (int(number) - 1)
                indicator += 1
            elif indicator == 1:
                data[i][1][0] = int(number)
                indicator += 1      
            elif indicator == 2:
                data[i][1][1] = int(number)
                indicator = 0
                i += 1
        initialIndex +=1

    stringCost = "DEMAND_SECTION"
    initialIndex = string.find(stringCost) + len(stringCost) + 2
    indicator = 0
    i = 0
    while(string[initialIndex] != 'D'):
        number = ""
        while(ord(string[initialIndex]) != 32 and string[initialIndex] != '\n'):
            number += string[initialIndex]
            initialIndex += 1
        if(len(number) > 0):        
            if indicator == 0:
                indicator += 1
            elif indicator == 1:
                data[i][2] = int(number)
                indicator = 0     
                i += 1
        initialIndex +=1
    
    stringCapacity = "CAPACITY : "
    initialIndex = string.find(stringCapacity) + len(stringCapacity)
    capacity = ""
    while(string[initialIndex] != '\n'):
        capacity += string[initialIndex]
        initialIndex += 1

    return data, int(capacity)
import pandas as pd
import numpy as np
import shutil as sh
from PIL import Image
from pathlib import Path


workDir = 'C:\\Users\\marce\\Projects\\CursVC\\ProjectVC\\'


def generateTrainImagesSet():
    testList = pd.read_json('./train.json')
    totalElements = 0
    movedElements = 0
    failedElements = 0
    failedElementsList = []
    for i in range(testList.shape[0]):
        imageFileName = 'train_'+str(i).zfill(5)+'.jpg'
        metadataFileName = 'train_'+str(i).zfill(5)+'.txt'
        metadataContent = ''
        response = copyFile(testList.iloc[i][0],'./trainImages/'+imageFileName)
        totalElements = totalElements+1

        if response == True:
            movedElements = movedElements+1
            metadataContent = metadataContent +str(testList.iloc[i][5])+' '+str(testList.iloc[i][1])+' '+str(testList.iloc[i][2])+' '+str(testList.iloc[i][3])+' '+str(testList.iloc[i][4])+'\n' 
            textFile = open('./trainImages/'+metadataFileName, 'w')
            textFile.write(metadataContent) 
            textFile.close()
            
        if response == False:
            failedElements = failedElements+1
            failedElementsList.append(testList.iloc[i][0])
    
    return totalElements, movedElements, failedElements, failedElementsList


def generateTestImagesSet():
    testList = pd.read_json('./test.json')
    totalElements = 0
    movedElements = 0
    failedElements = 0
    failedElementsList = []
    for i in range(testList.shape[0]):
        imageFileName = 'test_'+str(i).zfill(5)+'.jpg'
        metadataFileName = 'test_'+str(i).zfill(5)+'.txt'
        metadataContent = ''
        response = copyFile(testList.iloc[i][0],'./testImages/'+imageFileName)
        totalElements = totalElements+1

        if response == True:
            movedElements = movedElements+1
            metadataContent = metadataContent +str(testList.iloc[i][5])+' '+str(testList.iloc[i][1])+' '+str(testList.iloc[i][2])+' '+str(testList.iloc[i][3])+' '+str(testList.iloc[i][4])+'\n' 
            textFile = open('./testImages/'+metadataFileName, 'w')
            textFile.write(metadataContent) 
            textFile.close()
            
        if response == False:
            failedElements = failedElements+1
            failedElementsList.append(testList.iloc[i][0])
    
    return totalElements, movedElements, failedElements, failedElementsList


def copyFile(origin, destination):
    if fileExists(origin):
        sh.copy(origin, destination)
        return True
    return False

def fileExists(fileName):
    file = Path(fileName)
    if file.is_file():
        return True
    return False

def showImage(fileName):
    img = Image.open(fileName)
    img.show()
    

response1 = generateTestImagesSet()
print(response1)

response2 = generateTrainImagesSet()
print(response2)



#showImage('./grup/grup2.jpg')

#origin = './grup/grup2.jpg'
#destination = './testImages/1.jpg'

#response = copyFile(origin, destination)


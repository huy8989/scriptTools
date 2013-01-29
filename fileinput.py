# -*- coding: GBK -*-

#@author 89huy89@gmail.com 

#@version 2012-12-24 16:11 
import shutil 
import time

FILEPATH = "D://UserData/jianye.liu/Desktop/ValidateComparatorNormalTest.validateComparator.csv"
FILEPATHNEW="D://newCSV.csv"


def addToFile(filePath,newFilePath): 
    file = open(filePath)
    file2 = open(newFilePath,'w+')
    for line in file.readlines():
        print(line)
        file2.write(line.replace('\n','')+',,,,,,\n')
    file.close()
    file2.close()



if  __name__ == "__main__": 
    print "begin\n" 
    
    addToFile(FILEPATH,FILEPATHNEW)
    
    print "end\n" 
    time.sleep(2);
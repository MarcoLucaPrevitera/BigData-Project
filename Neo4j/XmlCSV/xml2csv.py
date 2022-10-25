import xml.etree.ElementTree as ET
import csv
import math
import random
import copy
 
tree = ET.parse("out30M.xml")
root = tree.getroot()
out_csv = open('output.csv','w', newline='', encoding='UTF-8')
csvwriter = csv.writer(out_csv)

currIndex = 4
csvIndex = {}
keyList = []
csvHeader = ["type","date","key","pubtype"]

#find all types of pubblications and loads to a dictionary
for child in root:
    if child.tag not in csvIndex:
        csvIndex[child.tag]={}

#scan all pub types
for pub_type in csvIndex.keys():
    maxDict = {} #object to store the maximum number of attributes for each pubblication type
    
    for elem in root.findall(pub_type):
        thisDict = {}
        keyList.append(elem.attrib["key"])#save the key of that article in a list for randomic assigment
        
        for innerTag in elem:
            #counts the number of each tags for an element
            if innerTag.tag in thisDict:
                thisDict[innerTag.tag]+=1
            else:
                thisDict[innerTag.tag]=1 #we create the tag in the dictionary
            
            #updates the total count for that pubblication type
            if innerTag.tag in maxDict:
                if thisDict[innerTag.tag] > maxDict[innerTag.tag]:
                    maxDict[innerTag.tag] = thisDict[innerTag.tag]
            else:
                maxDict[innerTag.tag]=1 #we create the tag in the dictionary
    
    #load the found number of attributes for that pubblication type in the global model of indexes
    for key in maxDict.keys():
        csvIndex[pub_type][key] = currIndex
        currIndex = currIndex+maxDict[key]
        
        #creates the header for the csv
        for n in range(maxDict[key]):
            csvHeader.append(pub_type+"/"+key+str(n))



csvwriter.writerow(csvHeader) #write the header row

#loads the data in the csv one type at time
for pub_type in csvIndex.keys():
    for elem in root.findall(pub_type):
        row = [""] * currIndex #array initialization
        tmpIndex = copy.deepcopy(csvIndex) #duplicate the index model for writing
        
        #load fixed attributes of pubblications
        row[0] = pub_type
        row[1] = elem.attrib["mdate"]
        row[2] = elem.attrib["key"]
        if "publtype" in elem.attrib:
            row[3] = elem.attrib["publtype"]
        
        #load dynamic values of tags
        for innerTag in elem:
            row_pos = tmpIndex[pub_type][innerTag.tag] #get the write column position
            row[row_pos] = innerTag.text #write the corrisponding value
            tmpIndex[pub_type][innerTag.tag]+=1 #increment the writing position
            
        csvwriter.writerow(row)
        
out_csv.close()
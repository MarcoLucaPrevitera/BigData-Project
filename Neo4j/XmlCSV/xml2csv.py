import xml.etree.ElementTree as ET
import csv
import math
import random
import copy
 
tree = ET.parse("out30M.xml")
root = tree.getroot()
out_csv = open('output.csv','w', newline='', encoding='utf-8')
csvwriter = csv.writer(out_csv)

currIndex = 1
csvIndex = {}
keyList = []
csvHeader = ["type"]

#find all types of pubblications and loads to a dictionary
for child in root:
    if child.tag not in csvIndex:
        csvIndex[child.tag]={}

#scan all pub types
for pub_type in csvIndex.keys():
    maxDict = {}
    
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
    
    #load the found number of attributes in the global dictionary of indexes
    for key in maxDict.keys():
        csvIndex[pub_type][key] = currIndex
        currIndex = currIndex+maxDict[key]
        
        #creates the header for the csv
        for n in range(maxDict[key]):
            csvHeader.append(pub_type+"/"+key+str(n))



csvwriter.writerow(csvHeader)

for pub_type in csvIndex.keys():
    for elem in root.findall(pub_type):
        row = [""] * currIndex #array initialization
        tmpIndex = copy.deepcopy(csvIndex)
        
        row[0]=pub_type
        for innerTag in elem:
            row_pos = tmpIndex[pub_type][innerTag.tag]
            row[row_pos] = innerTag.text
            tmpIndex[pub_type][innerTag.tag]+=1
            
        csvwriter.writerow(row)
        
out_csv.close()
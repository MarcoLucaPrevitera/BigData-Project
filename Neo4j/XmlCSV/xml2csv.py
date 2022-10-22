import xml.etree.ElementTree as ET
import csv
 
tree = ET.parse("out30M.xml")
root = tree.getroot()
 
out_csv = open('output.csv', 'w')


typeList = []

for child in root:
    typeList.append(child.tag)

typeList = list(set(typeList))
print(typeList)

for pub_type in typeList:
    tmpList = []
    print("Elaborating ", pub_type, ":")
    for elem in root.findall(pub_type):
        for inner in elem.iter():
            tmpList.append(inner.tag)
    tmpList = list(set(tmpList))
    print(tmpList)
    print("")

 
# csvwriter = csv.writer(out_csv)
# resident_head = []
 
# count = 0
# for member in root.findall('Resident'):
    # resident = []
    # address_list = []
    # # if count == 0:
        # # name = member.find('Name').tag
        # # resident_head.append(name)
        # # Phone = member.find('Phone').tag
        # # resident_head.append(Phone)
        # # Email = member.find('Email').tag
        # # resident_head.append(Email)
         
        # # csvwriter.writerow(resident_head)
        # # count = count + 1
 
    # name = member.find('Name').text
    # resident.append(name)
    # Phone = member.find('Phone').text
    # resident.append(Phone)
    # Email = member.find('Email').text
    # resident.append(Email)
    # csvwriter.writerow(resident)


# Resident_data.close()
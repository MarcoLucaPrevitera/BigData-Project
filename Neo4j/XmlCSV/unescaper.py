import html
import fileinput

totMB = 40

inputFile="D:/Uni/Magistrale - 1/Systems and methods for big and unstructured data/Progetto/Data/dblp.xml"
outputFile="D:/Uni/Magistrale - 1/Systems and methods for big and unstructured data/Progetto/Data/out"+str(totMB)+"MB.xml"

input = open(inputFile,'rb')
text = input.read(totMB*1000000)
output = open("temp.xml",'wb')
output.write(text)
output.close()

output = open(outputFile, 'a', encoding="UTF-8")
output.truncate(0)
count = 0

for lines in fileinput.input(["temp.xml"]):
    uLine = html.unescape(lines)
    uLine = uLine.replace('&', " and ")
    uLine = uLine.replace("<i>", "")
    uLine = uLine.replace("</i>", "")
    uLine = uLine.replace("<sup>", "")
    uLine = uLine.replace("</sup>", "")
    uLine = uLine.replace("<sub>", "")
    uLine = uLine.replace("</sub>", "")
    uLine = uLine.replace("<<", "")
    uLine = uLine.replace(">>", "")
    output.write(uLine)
    count+=1
    if count % 1000000 == 0:
        print(count)
    

output.close()
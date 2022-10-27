import html
import fileinput

totMB = 100

inputFile="D:/Uni/Magistrale - 1/Systems and methods for big and unstructured data/Progetto/Data/dblp.xml"
outputFile="D:/Uni/Magistrale - 1/Systems and methods for big and unstructured data/Progetto/Data/out"+str(totMB)+"M.xml"

input = open(inputFile,'rb')
text = input.read(totMB*1000000)
output = open("temp.xml",'wb')
output.write(text)
output.close()

output = open(outputFile, 'a', encoding="UTF-8")
output.truncate(0)
count = 0

for lines in fileinput.input(["temp.xml"]):
    line = lines.replace("<i>", "")
    line = line.replace("</i>", "")
    line = line.replace("<sup>", "")
    line = line.replace("</sup>", "")
    line = line.replace("<sub>", "")
    line = line.replace("</sub>", "")
    line = line.replace("&lt;", "")
    line = line.replace("&gt;", "")
    line = line.replace('&amp;', " and ")
    uLine = html.unescape(line)
    output.write(uLine)
    count+=1
    if count % 1000000 == 0:
        print(count)
    

output.close()
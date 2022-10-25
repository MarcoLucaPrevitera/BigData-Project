import html
import fileinput

inputFile="dblp.xml"
outputFile="out30M.xml"

input = open(inputFile,'rb')
text = input.read(30000000)
output = open("temp.xml",'wb',encoding="utf-8")
output.write(text)
output.close()

output = open(outputFile, 'a', encoding="utf-8")
output.truncate(0)
count = 0

for lines in fileinput.input(["temp.xml"]):
    uLine = html.unescape(lines)
    andLine = uLine.replace('&', " and ")
    output.write(andLine)
    count+=1
    if count % 1000000 == 0:
        print(count)
    

output.close()
import csv

out_csv = open('out_text.csv','w', newline='', encoding='UTF-8')
csvwriter = csv.writer(out_csv)
csvwriter.writerow(["id","text"])

incremental = 0


for f_name in ["269-0.txt","282-0.txt","786-0.txt"]:
    inputFile = open('./Sources/'+f_name, encoding='utf8')
    lines = inputFile.read().split("\n\n")

    for i in range(0,len(lines)):
        lines[i] = lines[i].replace("\n", "")
        if len(lines[i])>200:
            csvwriter.writerow([incremental, lines[i]])
            incremental += 1
    inputFile.close()

out_csv.close()
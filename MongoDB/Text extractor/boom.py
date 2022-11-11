import pandas as pd
 

with open('Sources/269-0.txt',encoding='utf8') as f:
    data = f.read()
    splat = data.split("\n\n")

with open('Sources/282-0.txt',encoding='utf8') as f:
    data = f.read()
    arr = data.split("\n\n")
    splat.append(arr)
    
with open('Sources/786-0.txt',encoding='utf8') as f:
    data = f.read()
    arr = data.split("\n\n")
    splat.append(arr)
    
pd.DataFrame(splat).to_csv('paragraphs.csv', index_label = "Index", header  = ['Paragraph text'])    

import json
import random
#from pprint import pprint
#import sys

main_json = open('main.json', encoding="UTF-8")
main_data = json.load(main_json)
#pprint (main_data)
main_json.close()

authors_pub = {}
doc_preview = {}

def sostisuisci_tags(articolo):
    lista_tags = [t['tag'] for t in articolo['tags']]
    articolo['tags'] = lista_tags


#find all publications for each author
for doc in main_data:
    for author in doc["authors"]:
        name = author["name"]

        if name not in authors_pub: #insert the author in the dictionary if not present
            authors_pub[name]=[]

        temp ={"title" : doc["title"], "date" : doc["date"], "doc_id" : doc["doc_id"]}
        authors_pub[name].append(temp) #insert the document preview in the dictionary


#create a preview for all the documents
for doc in main_data:
    id = doc["doc_id"]
    doc_preview[id] = {"ref_id" : id, "title" : doc["title"], "date" : doc["date"]}


#write the article data in the final author JSON
author_json = open('author.json', encoding="UTF-8")
author_data = json.load(author_json)
author_json.close()

for author in author_data:
    name = author["name"]
    
    if name in authors_pub:
        author["documents"] = authors_pub[name]

aut_output = json.dumps(author_data, indent=1, ensure_ascii=False)

with open("final_aut.json","w", encoding="UTF-8") as aut_file: #write the output file
    aut_file.write(aut_output)


#generate bibliograpy references and write the final JSON for articles
for article in main_data:
    num_citation = random.randrange(0,8)

    bib_list = []
    while len(bib_list) < num_citation:
        id = random.randrange(1, len(main_data))
        if id != article["doc_id"]:
            bib_list.append(doc_preview[id])

    if num_citation != 0:
        article["bibliography"] = bib_list
    
    sostisuisci_tags(article)


main_output = json.dumps(main_data, indent=1, ensure_ascii=False)


with open("final_main_tagparsed.json","w", encoding="UTF-8") as main_file: #write the output file
    main_file.write(main_output)
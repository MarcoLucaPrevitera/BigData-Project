import json

main_json = open('main.json', encoding="UTF-8")
main_data = json.load(main_json)

authors_pub = {}

for i in main_data:
    for author in i["authors"]:
        name = author["name"]
        if name not in authors_pub:
            authors_pub[name]=[]
        temp ={"title" : i["title"], "date" : i["date"], "doc_id" : i["doc_id"]}
        authors_pub[name].append(temp)

print(authors_pub["Frank Manola"])

author_json = open('author.json', encoding="UTF-8")
author_data = json.load(author_json)



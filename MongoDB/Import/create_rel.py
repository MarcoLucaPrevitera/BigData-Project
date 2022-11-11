import json

main_json = open('main.json', encoding="UTF-8")
main_data = json.load(main_json)

for elem in main_data[0]:
    print(elem.title)

print(main_data)

author_json = open('author.json', encoding="UTF-8")
author_data = json.load(author_json)


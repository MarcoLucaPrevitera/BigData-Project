import csv
import random

orig_incollection = open('incollectionFormatted.csv.txt', encoding="UTF-8")
orig_written_by = open('writtenBy-inc-authorFormatted.csv.txt', encoding="UTF-8")

orig_book = open('bookFormatted.csv.txt', encoding="UTF-8")
orig_edited_by = open('editedBy-book-authorFormatted.csv.txt', encoding="UTF-8")

orig_cite = open('citesFormatted.csv.txt', encoding="UTF-8")
orig_book_inc = open('contain-book-incollectionFormatted.csv.txt', encoding="UTF-8")



csv_incollection = list(csv.reader(orig_incollection))
csv_written_by = list(csv.reader(orig_written_by, delimiter = ';'))
csv_book = list(csv.reader(orig_book))
csv_edited_by = list(csv.reader(orig_edited_by, delimiter = ';'))
csv_cite = list(csv.reader(orig_cite))
csv_book_inc = list(csv.reader(orig_book_inc, delimiter = ';'))


def create_inc():

    #add authors
    header = True
    
    for line in csv_written_by:
        if header == False:
            curr_incollection = line[0]
            curr_author = line[1]

            header1 = True
            for inc in csv_incollection:
                tmp = inc[0]
                if len(inc) == 6 and header1 == False:
                    inc.append([])

                if tmp == curr_incollection:
                    inc[6].append(curr_author)
                
                header1 = False

        header = False

    csv_incollection[0].append('author_array')


    #add citation
    header = True
    for line in csv_cite:
        if header == False:
            curr_incollection = line[0]
            curr_cite = line[1]

            header1 = True
            for inc in csv_incollection:
                tmp = inc[0]
                if len(inc) == 7 and header1 == False:
                    inc.append([])

                if tmp == curr_incollection and len(inc[7]) < random.randint(7,15):
                    inc[7].append(curr_cite)

                header1 = False

        header = False


    csv_incollection[0].append('cited_inc_array')



    #add book id
    header = True
    for line in csv_book_inc:
        if header == False:
            curr_incollection = line[1]
            curr_book = line[0]

            header1 = True
            for inc in csv_incollection:
                tmp = inc[0]
                if tmp == curr_incollection:
                    inc.append(curr_book)
                header1 = False
        header = False


    csv_incollection[0].append('book_id')


    out_csv = open('./final/incollection.csv','w', newline='', encoding='UTF-8')

    for row in csv_incollection:
        csvwriter = csv.writer(out_csv, delimiter=";")
        csvwriter.writerow(row)


def create_book():
    #add authors
    header = True
    
    for line in csv_edited_by:
        if header == False:
            curr_book = line[0]
            curr_author = line[1]

            header1 = True
            for inc in csv_book:
                tmp = inc[0]
                if len(inc) == 7 and header1 == False:
                    inc.append([])

                if tmp == curr_book:
                    inc[7].append(curr_author)
                
                header1 = False

        header = False

    csv_book[0].append('editor_array')

    out_csv = open('./final/book.csv','w', newline='', encoding='UTF-8')

    for row in csv_book:
        csvwriter = csv.writer(out_csv, delimiter=";")
        csvwriter.writerow(row)



create_inc()
create_book()

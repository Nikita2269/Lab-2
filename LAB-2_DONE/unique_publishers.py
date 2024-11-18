from csv import reader

file_path = "books-en.csv"

def get_unique_publishers():
    publishers = set()
    with open(file_path, 'r', encoding='ISO-8859-1') as csvfile:
        table = reader(csvfile, delimiter=';')
        headers = next(table)
        for row in table:
            publisher = row[4].strip()
            if publisher:
                publishers.add(publisher)
    return publishers

unique_publishers = get_unique_publishers()

for publisher in sorted(unique_publishers):
    print(publisher)

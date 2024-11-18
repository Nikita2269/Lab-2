from csv import reader
import random

file_path = "books-en.csv"
output_file = "bibliographic_references.txt"

def generate_references():
    references = []
    with open(file_path, 'r', encoding='ISO-8859-1') as csvfile:
        table = reader(csvfile, delimiter=';')
        headers = next(table)
        rows = list(table)
        random_rows = random.sample(rows, 20)
        for i, row in enumerate(random_rows, start=1):
            author = row[2].strip()
            title = row[1].strip()
            year = row[3].strip()
            reference = f"{i}. {author}. {title} - {year}"
            references.append(reference)
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("\n".join(references))
    print(f"Библиографические ссылки сохранены в файл '{output_file}'.")

generate_references()

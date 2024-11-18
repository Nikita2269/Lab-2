from csv import reader

file_path = "books-en.csv"
count = 0

with open(file_path, 'r', encoding='ISO-8859-1') as csvfile:
    table = reader(csvfile, delimiter=';')
    headers = next(table)
    for row in table:
        if len(row[1]) > 30:
            count += 1

print(f"Количество записей с длиной названия более 30 символов: {count}")

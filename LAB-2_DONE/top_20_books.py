from csv import reader

file_path = "books-en.csv"

def get_top_20_books():
    books = []
    with open(file_path, 'r', encoding='ISO-8859-1') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)
        for row in table:
            title = row[1].strip()
            downloads = int(row[5].strip())
            books.append((title, downloads))
    
    books.sort(key=lambda x: x[1], reverse=True)
    return books[:20]

top_books = get_top_20_books()

for i, (title, downloads) in enumerate(top_books, start=1):
    print(f"{i}. {title} - {downloads} скачиваний")

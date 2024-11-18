from csv import reader

file_path = "books-en.csv"

def search_books_by_author(author_name):
    results = []
    with open(file_path, 'r', encoding='ISO-8859-1') as csvfile:
        table = reader(csvfile, delimiter=';')
        headers = next(table)
        for row in table:
            author = row[2].strip()
            year = row[3].strip()
            title = row[1].strip()
            if author_name.lower() in author.lower() and year.isdigit() and int(year) < 1990:
                results.append(title)
    
    return results


search = input("Введите имя автора для поиска (или часть имени): ").strip()
books = search_books_by_author(search)

if books:
    print(f"Найдены книги автора '{search}', опубликованные до 1990 года:")
    for book in books:
        print(f"- {book}")
else:
    print(f"Книги автора '{search}', опубликованные до 1990 года, не найдены.")

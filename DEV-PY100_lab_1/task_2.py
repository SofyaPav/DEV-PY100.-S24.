B = 1
KB = 1024 * B
MB = 1024 * KB
count_of_pages_per_book = 100
count_of_strings_per_page = 50
count_of_symbols_per_string = 25
storage_of_symbol_B = 4 * B
storage_of_one_book_B = (count_of_pages_per_book * count_of_strings_per_page *
                         count_of_symbols_per_string * storage_of_symbol_B)
storage_of_diskette_B = 1.44 * MB
count_of_books_on_diskette = int(round(storage_of_diskette_B / storage_of_one_book_B, 0))
print("Количество книг, помещающихся на дискету:", count_of_books_on_diskette)

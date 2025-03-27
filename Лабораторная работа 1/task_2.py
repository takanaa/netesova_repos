# TODO Найдите количество книг, которое можно разместить на дискете

disketa_bytes = 1.44 * 1024 * 1024
book_bytes = 100 * 50 * 25 * 4
result = disketa_bytes // book_bytes
print("Количество книг, помещающихся на дискету:", int(result))

BYTES_ONE_CHAR = 4
pages = 100
lines = 50
chars = 25

total_bytes = pages * lines * chars * BYTES_ONE_CHAR

disk_size = 1.44 * 1024 ** 2
num_books = int(disk_size // total_bytes)

print("Количество книг, помещающихся на дискету:", num_books)

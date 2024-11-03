# TODO Найдите количество книг, которое можно разместить на дискете

free_space_mbytes = 1.44
pages_in_book = 100
lines_on_page = 50
symbols_in_line = 25
symbol_weight_bytes = 4

free_space_bytes = free_space_mbytes * 1024 * 1024
book_weight_bytes = pages_in_book * lines_on_page * symbols_in_line * symbol_weight_bytes
book_amount = int(free_space_bytes // book_weight_bytes)

print("Количество книг, помещающихся на дискету:", book_amount)

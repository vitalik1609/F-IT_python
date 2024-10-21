# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
rows = 50
symbols = 25
bytes_per_symbol = 4

book_weight = pages*rows*symbols*bytes_per_symbol #в байтах

v_disc = 1.44
mb_kb = 1024
kb_b = 1024
total = v_disc*mb_kb*kb_b
print("Количество книг, помещающихся на дискету:", int(total//book_weight))

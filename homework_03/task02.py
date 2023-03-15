# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
from random import randint as r_int
from random import shuffle

some_list = [str(i) for i in range(1, 15) for _ in range(1, r_int(1, 4))]
shuffle(some_list)
print(some_list)

doubled_elements = [elem for elem in set(some_list) if some_list.count(elem) > 1]
print(doubled_elements)

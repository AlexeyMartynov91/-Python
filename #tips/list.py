# Транспонированая матрица
old_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
new_list = zip(*old_list)
print(list(new_list))

# Поиск уникальных
my_list = [10, 10, 3, 4, 5, 9, 30, 30]
print(list(set(my_list)))

a = [(i, j)  # пример записи с двумя переменными и условиями
     for i in range(3) if i % 3 == 0
     for j in range(4) if j % 2 == 0
     ]
print(a)


a = [f"{i} * {j} = {j*i}"  # умножение
     for i in range(3)
     for j in range(4)

     ]
print(a)


matrix = [[0, 1, 2, 3],
          [10, 11, 12, 13],
          [20, 21, 22, 23]
          ]
a = [x  # из двумерного списка делает одномерный, с перечислением всех под элементов
     for row in matrix
     for x in row
     ]
print(a)


m, n = 3, 4
# получаем "b" списков с "a" элементами в каждом
matrix = [[a for a in range(m)] for b in range(n)]
print(matrix)


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# возводит в элементы в квадрат, оставляя вложенность как есть
b = [[x ** 2 for x in row] for row in a]
print(b)

c = [x ** 2  # возводит в элементы в квадрат, список становится одномерным
     for row in a
     for x in row
     ]
print(c)


a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

a = [[row[i] for row in a]
     for i in range(len(a[0]))]  # Транспонированная  матрица
print(a)

# Возведение в квадрат с элемента полученного с другой с помощью функции
g = [u ** 2 for u in [x + 1 for x in range(5)]]
print(g)

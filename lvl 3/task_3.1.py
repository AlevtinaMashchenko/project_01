# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)



############ Решение ############

import random

class Matrix:
    def __init__(self, rows = 5, columns = 7):
        self.rows = rows
        self.columns = columns
        self.content = []
        for j in range(self.rows):
            k=[]
            for i in range(self.columns):
                k.append(random.randint(1, 9))
            self.content.append(k)
        
    def print_Matrix(self):
        return self.content
    
    def edit_Matrix(self, rows1, columns1, value):
         self.rows1 = rows1
         self.columns1 = columns1
         self.value = value
         self.content[rows1-1][columns1-1] = value
         print('Таблица с обновленными данными:')
         return self.content

    def print_columns_and_rows(self):
        return f'Количество строк равно: {self.rows}. Количество колонок равно: {self.columns}.'
        
     
my_table = Matrix()

print(*my_table.print_Matrix(), sep='\n')
print(*my_table.edit_Matrix(1,1,"Hello Teaher!"), sep='\n')
print(my_table.print_columns_and_rows())

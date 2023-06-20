# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:





############ решение задачи ############


# создание таблицы Students

# import sqlite3

# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# query = '''CREATE TABLE Students (
#     Student_Id INTEGER,
#     Student_Name TEXT,
#     School_Id INTEGER PRIMATY KEY)'''
# cursor.execute(query)
# connection.commit()
# connection.close()

# наполнение таблицы
# import sqlite3

# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# query = '''INSERT INTO Students (Student_Id , Student_Name , School_Id)
# VALUES
# ('201', 'Иван', '1'),
# ('202', 'Петр', '2'),
# ('203', 'Анастасия', '3'),
# ('204', 'Игорь', '4')'''
# cursor.execute(query)
# connection.commit()
# connection.close()



# вывод информации о школе и студенте.

import sqlite3

def get_connection():
    connection = sqlite3.connect('teachers.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_student_data(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = 'SELECT * FROM Students JOIN School ON Students.School_Id = School.School_Id WHERE Students.Student_Id = ?'
        cursor.execute(query,(student_id,))
        records = cursor.fetchmany()
        for row in records:
            print("Id студента:", row[0])
            print("Имя студента:", row[1])
            print("Id школы:", row[2])
            print("Название школы:", row[4])   
        close_connection(connection)
        
    except (Exception, sqlite3.Error) as error:
        print('Ошибка в получении данных ', error)

get_student_data(201)
 

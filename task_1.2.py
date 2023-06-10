# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
# решение пункт А

import random
first_song = random.choice(my_favorite_songs)
second_song = random.choice(my_favorite_songs)
third_song = random.choice(my_favorite_songs)
time_of_songs = first_song[-1] + second_song[-1] + third_song[-1]

if ((time_of_songs * 100)%100) >= 60:
    time_of_songs = time_of_songs-.60 + 1

print('Три песни звучат', round(time_of_songs, 2), 'минут')



# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# решение пункт В

first_song2 = random.choice(list(my_favorite_songs_dict))
second_song2 = random.choice(list(my_favorite_songs_dict))
third_song2 = random.choice(list(my_favorite_songs_dict))
time_of_songs2 = my_favorite_songs_dict[first_song2] + my_favorite_songs_dict[second_song2] + my_favorite_songs_dict[third_song2]

if ((time_of_songs2 * 100)%100) >= 60:
    time_of_songs2 = time_of_songs2-.60 + 1

print('Три песни звучат', round(time_of_songs2, 2), 'минут')



# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# решение пункт С

print('Три случайные песни', first_song[0], ',' , second_song[0], ',' , third_song[0])
print('Три случайные песни', first_song2, ',' , second_song2, ',' , third_song2)


# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 




# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# вариант 1
print(my_favorite_songs[0:14], my_favorite_songs[64:], my_favorite_songs[16:30], my_favorite_songs[51:62])

# вариант 2
my_favorite_songs = my_favorite_songs.split(',')
print(my_favorite_songs[0], my_favorite_songs[-1], my_favorite_songs[1], my_favorite_songs[-2], sep ='')
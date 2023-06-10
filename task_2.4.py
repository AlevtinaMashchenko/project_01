# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"


# решение пункт А

def remove_exclamation_marks(s):
    if '!' in s:
        s = s.replace('!', '')
    print(s)
remove_exclamation_marks()


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"


# решение пункт В

def remove_last_em(s):
    if s[-1] == '!' in s:
        s = s[:-1]
    print(s)
remove_last_em()


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    s = s.split()
    s_str = []
    for i in s:
        if i.count('!') != 1:
            s = s_str.append(i)
    print( ' '.join(s_str))

remove_word_with_one_em()
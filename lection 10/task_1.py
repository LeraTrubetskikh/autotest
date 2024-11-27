# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_random_name():
    while True:
        first_word = [random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 15))]
        second_word = [random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 15))]
        yield ' '.join([''.join(first_word), ''.join(second_word)])


# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

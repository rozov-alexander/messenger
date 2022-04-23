"""1. Каждое из слов «разработка», «сокет», «декоратор» представить 
в строковом формате и проверить тип и содержание соответствующих переменных. 
Затем с помощью онлайн-конвертера преобразовать строковые представление 
в формат Unicode и также проверить тип и содержимое переменных."""


FIRST_STR = 'разработка'
print(FIRST_STR)
print(type(FIRST_STR))
SECOND_STR = 'сокет'
print(SECOND_STR)
print(type(SECOND_STR))
THIRD_STR = 'декоратор'
print(THIRD_STR)
print(type(THIRD_STR))

print('----------------------------------------------------')
# строка, как последовательность юникод-символов
FIRST_WORD = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' # разработка
SECOND_WORD = '\u0441\u043e\u043a\u0435\u0442' # сокет
THIRD_WORD = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440' # декоратор
print(FIRST_WORD, type(FIRST_WORD))
print(SECOND_WORD, type(SECOND_WORD))
print(THIRD_WORD, type(THIRD_WORD))

print(FIRST_WORD == FIRST_STR)
print(SECOND_WORD == SECOND_STR)
print(THIRD_WORD == THIRD_STR)
print('----------------------------------------------------')

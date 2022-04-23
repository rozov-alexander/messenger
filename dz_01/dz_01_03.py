"""3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать 
в байтовом типе. Важно: решение должно быть универсальным, т.е. не зависеть от того, какие 
конкретно слова мы исследуем."""


def convert_to_bytes(some_str):
    try:
        return bytes(some_str, 'ascii')
    except:
        print(f'Строку "{some_str}" невозможно записать в байтовом типе')


str_1 = 'attribute'
str_2 = 'класс'
str_3 = 'функция'
str_4 = 'type'

convert_to_bytes(str_1)
convert_to_bytes(str_2)
convert_to_bytes(str_3)
convert_to_bytes(str_4)

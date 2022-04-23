"""2. Каждое из слов «class», «function», «method» записать в байтовом типе. 
Сделать это необходимо в автоматическом, а не ручном режиме, с помощью добавления 
литеры b к текстовому значению, (т.е. ни в коем случае не используя методы encode, 
decode или функцию bytes) и определить тип, содержимое и длину соответствующих переменных."""


def convert_to_bytes(some_str):
    try:
        byte_str = eval(f"b'{some_str}'")
        print(type(byte_str))
        print(byte_str)
        print(len(byte_str))
    except SyntaxError:
        print(f"Строку '{some_str}' нельзя преобразовать в bytes")


test_str_1 = 'class'
test_str_2 = 'function'
test_str_3 = 'method'
test_str_4 = 'Класс'

convert_to_bytes(test_str_1)
convert_to_bytes(test_str_2)
convert_to_bytes(test_str_3)
convert_to_bytes(test_str_4)

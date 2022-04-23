"""4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» 
из строкового представления в байтовое и выполнить обратное преобразование 
(используя методы encode и decode)."""


def string_to_bytes(some_str):
    return some_str.encode('utf-8')
    

def bytes_to_string(byte_str):
    return byte_str.decode('utf-8')


str_1 = 'разработка'
str_2 = 'администрирование'
str_3 = 'protocol'
str_4 = 'standard'

print(string_to_bytes(str_1))
print(bytes_to_string(string_to_bytes(str_1)))
print(string_to_bytes(str_2))
print(bytes_to_string(string_to_bytes(str_2)))
print(string_to_bytes(str_3))
print(bytes_to_string(string_to_bytes(str_3)))
print(string_to_bytes(str_4))
print(bytes_to_string(string_to_bytes(str_4)))

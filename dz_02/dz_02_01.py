"""1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку 
определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» 
файл в формате CSV. Для этого:
    • Создать функцию get_data(), в которой в цикле осуществляется перебор файлов 
    с данными, их открытие и считывание данных. В этой функции из считанных данных 
    необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы», 
    «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в 
    соответствующий список. Должно получиться четыре списка — например, os_prod_list, 
    os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для 
    хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета 
    в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». 
    Значения для этих столбцов также оформить в виде списка и поместить в файл main_data 
    (также для каждого файла);
    • Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. 
    В этой функции реализовать получение данных через вызов функции get_data(), а также 
    сохранение подготовленных данных в соответствующий CSV-файл;
    • Проверить работу программы через вызов функции write_to_csv()."""
from chardet import detect
import re
import csv


def get_data(filenames):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for file in filenames:
        with open(f"{file}", 'rb') as f:
            raw_content = f.read()
        encoding = detect(raw_content)['encoding']
        content = raw_content.decode(encoding=encoding)
        print(content)
        os_prod_list.append(re.findall(r'Изготовитель системы:\s*(\S*)', content))
        os_name_list.append(re.findall(r'Название ОС:\s*(.+)\r', content))
        os_code_list.append(re.findall(r'Код продукта:\s*(.+)\r', content))
        os_type_list.append(re.findall(r'Тип системы:\s*(.+)\r', content))
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)
    data_matrix = [os_prod_list, os_name_list, os_code_list, os_type_list]
    for _ in range(len(data_matrix[0])):
        main_data.append([os_prod_list[_][0], os_name_list[_][0], os_code_list[_][0], os_type_list[_][0]])
    return main_data


filenames = ['info_1.txt', 'info_2.txt', 'info_3.txt']
result_file = 'result.csv'


def write_to_csv(filenames, result_file):
    result = get_data(filenames)
    with open(f'{result_file}', 'w') as f:
        f_n = csv.writer(f)
        for row in result:
            f_n.writerow(row)

write_to_csv(filenames, result_file)

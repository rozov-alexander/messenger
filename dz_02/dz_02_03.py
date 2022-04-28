"""3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий 
сохранение данных в файле YAML-формата. Для этого:
    • Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, 
    второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число 
    с юникод-символом, отсутствующим в кодировке ASCII (например, €);
    • Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить 
    стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы 
    с юникодом: allow_unicode = True;
    • Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными."""

from yaml import load, dump


data_to_yaml = {
     'fields': ['id', 'action', 'to', 'from', 'encoding', 'message'],
     'total': 4321,
     'price': {
        'service1': '99₽',
        'service2': '15€',
        'service3': '40¥',
    }
}

with open('file.yaml', 'w', encoding='utf-8') as f:
    dump(data_to_yaml, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open('file.yaml', 'r', encoding='utf-8') as f:
    data = load(f)

if (data == data_to_yaml):
    print('Данные совпадают')
else:
    print('Что то пошло не так')

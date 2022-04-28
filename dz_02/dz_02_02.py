"""2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON 
с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
    • Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), 
    количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна 
    предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать 
    величину отступа в 4 пробельных символа;
    • Проверить работу программы через вызов функции write_order_to_json() с передачей в нее 
    значений каждого параметра."""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open('orders.json', 'w', encoding='utf-8') as f:
        write_data = data['orders']
        write_dict = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        write_data.append(write_dict)
        json.dump(data, f, indent=4, ensure_ascii=False)



write_order_to_json('Товар1', '5', '3000', 'Покупатель_1', '25.04.2022')
write_order_to_json('Товар2', '2', '1400', 'Покупатель_2', '22.04.2022')
write_order_to_json('Товар3', '12', '5600', 'Покупатель_3', '21.04.2022')
write_order_to_json('Товар4', '22', '11200', 'Покупатель_4', '19.04.2022')

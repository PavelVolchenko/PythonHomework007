""" Модель - отвечает за внутреннюю логику работы программы. Здесь мы можем скрыть способы хранения данных,
    а так же правила и алгоритмы обработки информации.                                                 """

import json
import csv


def read_db():
    file = [string.strip() for string in open('database.txt', 'r', encoding='UTF-8').readlines()]
    data = list()
    while file:
        entry = lambda x: x[:x.index('') + 1]
        data.append(entry(file))
        file = file[file.index('') + 1:]
    return data


def show_guide(data):
    for id, person in enumerate(data, 1):
        print(f'{id}. {person[0]:<10} {person[1]:<8}\tТелефон: {person[2]:<10}\tОписание: {person[3]}')


def delete_record(data):
    index = int(input("Введите номер записи для удаления: "))
    data.pop(index-1)
    save_changes(data)
    return data


def create_record(data):
    new_record = list()
    new_record.append(input('Фамилия: '))
    new_record.append(input('Имя: '))
    new_record.append(input('Телефон: '))
    new_record.append(input('Описание: '))
    new_record.append('')
    data.append(new_record)
    save_changes(data)
    return data


def update_record(data):
    index = int(input('Введите номер записи которую следует обновить: '))
    rec = int(input('0 - фамилия\n1 - имя\n2 - телефон\n3 - описание\nИзменить: '))
    data[index-1][rec] = input('Новые данные: ')
    save_changes(data)
    return data


def save_changes(data):
    with open('database.txt', 'w', encoding='UTF-8') as file:
        for string in data:
            for s in string:
                file.write(s + '\n')
    print('*** Изменения успешно сохранены ***')
    return data


def prepare_export(data):
    out_data = list()
    for rec in data:
        entry = lambda x: x[:x.index('')]
        person = {'last_name': entry(rec)[0],
                  'first_name': entry(rec)[1],
                  'telephone': entry(rec)[2],
                  'description': entry(rec)[3]}
        out_data.append(person)
    return out_data


def json_export(data: dict):
    data = prepare_export(data)
    with open('database.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file)
        print(f'*** Данные экспортированы в файл {file.name}')


def csv_export(data: dict):
    data = prepare_export(data)
    with open('database.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writerows(data)
        print(f'*** Данные экспортированы в файл {file.name}')

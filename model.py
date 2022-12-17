""" Модель - отвечает за внутреннюю логику работы программы. Здесь мы можем скрыть способы хранения данных,
    а так же правила и алгоритмы обработки информации.                                                 """

import json
import csv


# def read_db():
#     file = [string.strip() for string in open('database.txt', 'r', encoding='UTF-8').readlines()]
#     data = list()
#     while file:
#         entry = lambda x: x[:x.index('')]
#         person = {'last_name': entry(file)[0],
#                   'first_name': entry(file)[1],
#                   'telephone': entry(file)[2],
#                   'description': entry(file)[3]}
#         data.append(person)
#         file = file[file.index('') + 1:]
#     return data


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
        print(f'\n{id}. {person[0]} {person[1]}')
        print(f'Телефон: {person[2]}')
        print(f'Описание: {person[3]}')


# def show_guide(data):
#     for id, person in enumerate(data):
#         print(f'\n{id}. {person.get("first_name")} {person.get("last_name")}')
#         print(f'Телефон: {person.get("telephone")}')
#         print(f'Описание: {person.get("description")}')

def delete_record(data):
    index = int(input("\nВведите номер записи для удаления: "))
    data.pop(index-1)
    return data


def create_record(data):
    new_record = list()
    new_record.append(input('\nФамилия: '))
    new_record.append(input('Имя: '))
    new_record.append(input('Телефон: '))
    new_record.append(input('Описание: '))
    new_record.append('')
    data.append(new_record)
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


def update_record(data):
    index = int(input('\nВведите номер записи которую следует обновить: '))
    rec = int(input('\n0 - фамилия\n1 - имя\n2 - телефон\n3 - описание\nИзменить: '))
    data[index-1][rec] = input('Новые данные: ')
    return data


def json_export(data: dict):
    data = prepare_export(data)
    with open('database.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file)
        print(f'\nДанные экспортированы в файл {file.name}')


def csv_export(data: dict):
    data = prepare_export(data)
    with open('database.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writerows(data)
        print(f'\nДанные экспортированы в файл {file.name}')

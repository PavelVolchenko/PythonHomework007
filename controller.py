""" Контроллер - обеспечивает связь между Моделью и действиями пользователя, полученными в результате
    взаимодействия с Представлением. Координирует моменты обновления состояний Модели и Представления.
    Принимает большинство решений о переходах приложения из одного состояния в другое. Фактически на
    каждое действие, которое может сделать пользователь в Представлении, должен быть определен
    обработчик в Контроллере. Этот обработчик выполнит соответствующие манипуляции над моделью,
    и в случае необходимости сообщит Представлению о наличии изменений.                           """

from model import show_guide
from view import show_menu as ui
from model import json_export
from model import csv_export
from model import delete_record
from model import create_record
from model import update_record


def controller(data):
    position = -1
    while position != 9:
        position = ui()
        match position:
            case 1:
                show_guide(data)
            case 2:
                delete_record(data)
            case 3:
                create_record(data)
            case 4:
                update_record(data)
            case 7:
                json_export(data)
            case 8:
                csv_export(data)
    else:
        print("Конец работы")



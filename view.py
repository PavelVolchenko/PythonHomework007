""" Представление - отвечает за отображение данных модели. Здесь мы предоставляем интерфейс для
    взаимодействия пользователя с Моделью.                                                  """


def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Показать все записи")
    print("2. Удалить запись")
    print("3. Добавить запись")
    print("4. Обновить запись")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))
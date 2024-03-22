from Write import select
import edit

while True:
    """ Выводит меню в котором вводится число выбора в переменную var.
        Проверяет значение переменной var и выбирает действие:
        1 - вызывают функцию select из модуля Write.
        2 - записывает введёные значения в класс editing и вызывает функцию.
        3 - записывает введёные значения в класс editing и вызывает функцию.
        4 - записывает введёные значения в класс editing и вызывает функцию.
        5 - печатает о неверном вводе
     """
    var = input("Выберите действие:\n 1 - Вывести общую сумму звонков по городам\n 2 - Внести новый звонок\n 3 - Изменить данные по звонку\n 4 - Удалить данные по звонку\n")
    if var == "1":
        select()
        """ Прекращает цикл """
        break
    elif var == "2":
        item1 = input("Введите время начала звонка\n")
        item1 = item1.strip()
        item2 = input("Введите город\n")
        item2 = item2.strip()
        item3 = input("Введите время разговора\n")
        item3 = item3.strip()
        data = edit.editing(item1, item2, item3, None)
        data.insert()
        """ Прекращает цикл """
        break
    elif var == "3":
        item1 = input("Введите id звонка\n")
        item1 = item1.strip()
        item2 = input("Введите время начала звонка\n")
        item2 = item2.strip()
        item3 = input("Введите город\n")
        item3 = item3.strip()
        item4 = input("Введите время разговора\n")
        item4 = item4.strip()
        data = edit.editing(item2, item3, item4, item1)
        data.update()
        """ Прекращает цикл """
        break
    elif var == "4":
        item1 = input("Введите id звонка\n")
        item1 = item1.strip()
        data = edit.editing(None, None, None, item1)
        data.delete()
        """ Прекращает цикл """
        break
    else:
        print("Неправильный выбор\n")
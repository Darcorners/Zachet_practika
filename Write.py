from ConnDB import connection


class Write:
    def __init__(self, x):
        """ Инициализирует переменную класса Write """
        self.str = x

    def insert(self):
        """ Открывает файл в режиме добавления строк и записывает в строку переменную """
        with open('result.txt', 'a', encoding='utf-8') as file:
            file.write(self.str)


def select():
    """ Открывает файл в режиме записи (очистив его от записей) и закрывает его """
    clear = open("result.txt", 'w')
    clear.close()
    with connection.cursor() as cursor:
        """ Отправляет запрос в базу данных,
        записывает результат запроса в переменную
        """
        cursor.execute(""" SELECT * FROM Cities WHERE 1""")
        resultq = cursor.fetchall()
        for i in resultq:
            """ Отправляет запрос в базу данных и получает название города c общей суммой звонков в этом городе """
            cursor.execute(f""" SELECT `Город`, SUM(`Тариф` * `Время разговора`) AS 'Сумма' FROM `phone_history` WHERE `Город` = '{i['city']}' """)
            resultqq = cursor.fetchall()
            for d in resultqq:
                """ В stg записывается отформатированная строка для записи в файл.
                     в переменную writing записыватеся класс Write и его переменные.
                     из writing используется функция insert класса Write
                """
                stg = f"{d['Город']} - {d['Сумма']}\n"
                writing = Write(stg)
                writing.insert()

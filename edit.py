from ConnDB import connection
from Write import Write
class editing:

    def __init__(self, x, y, z, n):
        """ Инициализирует переменные класса editing """
        self.time_start = x
        self.city = y
        self.time = z
        self.id = n

    def insert(self):
        """ Открывает файл в режиме записи (очистив его от записей) и закрывает его """
        clear = open("result.txt", 'w')
        clear.close()
        with connection.cursor() as cursor:
            """ Отправляет запрос в базу данных,
                записывает результат запроса в переменную 
            """
            cursor.execute(f"""SELECT id FROM Cities WHERE city = '{self.city}'""")
            city = cursor.fetchone()
            """ Отправляет запрос в базу данных, записывает результат запроса в переменную """
            cursor.execute(f""" INSERT INTO `History`(`time_start`, `city`, `time`) VALUES ('{self.time_start}', {city['id']}, {self.time}); """)
            cursor.execute(f""" SELECT LAST_INSERT_ID() AS Id """)
            resultq = cursor.fetchone()
            cursor.execute(f""" SELECT * FROM `phone_history` WHERE id = {resultq['Id']} """)
            resultq = cursor.fetchone()
            """ Подтверждает изменение в базе данных """
            connection.commit()
            """ В stg записывается отформатированная строка для записи в файл.
                в переменную writing записыватеся класс Write и его переменные.
                из writing используется функция insert класса Write
            """
            stg = f"id = {resultq['id']}, город: {resultq['Город']}, время начала: {resultq['Время начала']}, время разговора: {resultq['Время разговора']}, сумма: {resultq['Сумма']}"
            ins = Write(stg)
            ins.insert()
    def update(self):
        """ Открывает файл в режиме записи (очистив его от записей) и закрывает его """
        clear = open("result.txt", 'w')
        clear.close()
        with connection.cursor() as cursor:
            """ Отправляет запрос в базу данных,
                записывает результат запроса в переменную
            """
            cursor.execute(f"""SELECT id FROM Cities WHERE city = '{self.city}'""")
            city = cursor.fetchone()
            cursor.execute(f""" UPDATE `History` SET `time_start`= '{self.time_start}',`city`=  {city['id']},`time`= {self.time} WHERE `id` = {self.id};""")
            cursor.execute(f""" SELECT * FROM `phone_history`    WHERE `id` = {self.id} """)
            resultq = cursor.fetchone()
            """ В stg записывается отформатированная строка для записи в файл.
                в переменную writing записыватеся класс Write и его переменные.
                из writing используется функция insert класса Write
            """
            stg = f"id = {resultq['id']}, город: {resultq['Город']}, время начала: {resultq['Время начала']}, время разговора: {resultq['Время разговора']}, сумма: {resultq['Сумма']}"
            ins = Write(stg)
            ins.insert()
            """ Подтверждает изменение в базе данных """
            connection.commit()

    def delete(self):
        with connection.cursor() as cursor:
            """ Отправляет запрос в базу данных, записывает результат запроса в переменную """
            cursor.execute(f""" DELETE FROM `History` WHERE `id` = {self.id}; """)
            """ Подтверждает изменение в базе данных """
            connection.commit()
            print("Удаление успешно")
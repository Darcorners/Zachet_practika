from ConnDB import connection
import Queries
class write:
    def __init__(self, x):
        self.str = x

    def insert(self):
        with open('result.txt','a',encoding='utf-8') as file:
            file.write(self.str)
def select():
    with connection.cursor() as cursor:
        cursor.execute(Queries.Select_Cities)
        resultq = cursor.fetchall()
        for i in resultq:
            cursor.execute(Queries.Select_tax(i['city']))
            resultqq = cursor.fetchall()
            for i in resultqq:
                stg = f"{i['Город']} {i['Сумма']}\n"
                writing = write(stg)
                writing.insert()
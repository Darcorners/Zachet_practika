Select_Cities = """ SELECT * FROM Cities WHERE 1"""

def Select_tax(city):
    Select_Tax = f""" SELECT `Город`, SUM(`Тариф` * `Время разговора`) AS 'Сумма' FROM `phone_history` WHERE `Город` = '{city}' """
    return Select_Tax
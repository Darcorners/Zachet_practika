from Config import host, user, password, database
from pymysql import connect, cursors

connection = connect(
    host=host,
    user=user,
    password=password,
    database=database,
    cursorclass=cursors.DictCursor
)
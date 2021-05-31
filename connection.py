import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='pass123',
    database='serpiencovid',
    auth_plugin='mysql_native_password'
)


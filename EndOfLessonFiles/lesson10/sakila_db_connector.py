import mysql.connector
import logging

# You can also provide the arguments for the connect method by unpacking the following dictionary
# db_configs = {'user': 'root',
#               'password': 'password123',
#               'host': '127.0.0.1',
#               'database': 'sakila'}

cnx = mysql.connector.connect(user='root',
                              password='password123',
                              host='127.0.0.1',
                              database='sakila')
cursor = cnx.cursor()
query = """SELECT * FROM sakila.actor LIMIT 20;"""
result = cursor.execute(query)
rows = cursor.fetchall()
print(rows)
print(type(rows[0]))
cursor.close()
cnx.close()

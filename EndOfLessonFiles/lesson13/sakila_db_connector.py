import mysql.connector
import logging


class SakilaDBConnector:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def execute_actor_table_query(self, first_name):
        """
        Accesses the actor table in the sakila database
        :return: python list
        """
        logging.info(f"{self.execute_actor_table_query.__name__} has started")
        cnx = mysql.connector.connect(user=self.user,
                                      password=self.password,
                                      host=self.host,
                                      database=self.database)
        cursor = cnx.cursor()
        query = """SELECT * FROM sakila.actor WHERE first_name=%s"""
        cursor.execute(query, [first_name])
        rows = cursor.fetchall()
        first_name = [rows[i][1] for i in range(len(rows))]
        last_name = [rows[i][2] for i in range(len(rows))]
        name_string = ""
        for i in range(len(first_name)):
            first = first_name[i]
            last = last_name[i]
            full_name = first + " " + last + " "
            name_string = name_string + full_name
        cursor.close()
        cnx.close()
        logging.info(f"{self.execute_actor_table_query.__name__} has ended")
        return name_string

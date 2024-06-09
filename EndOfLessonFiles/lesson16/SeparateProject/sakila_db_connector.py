import mysql.connector
import logging


class SakilaDBConnector:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.cnx = None
        self.initialize_db_connection()

    def initialize_db_connection(self):
        self.cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host,
                                           database=self.database)

    def execute_actor_table_query(self, first_name):
        """
        Accesses the actor table in the sakila database
        :return: python list
        """
        logging.info(f"{self.execute_actor_table_query.__name__} has started")
        cursor = self.cnx.cursor()
        query = """SELECT * FROM sakila.actor WHERE first_name=%s"""
        cursor.execute(query, [first_name])
        rows = cursor.fetchall()
        first_name = [rows[i][1]for i in range(len(rows))]
        last_name = [rows[i][2]for i in range(len(rows))]
        name_string = ""
        for i in range(len(first_name)):
            first = first_name[i]
            last = last_name[i]
            full_name = first + " " + last + " "
            name_string = name_string + full_name
        cursor.close()
        logging.info(f"{self.execute_actor_table_query.__name__} has ended")
        return name_string

    def update_table(self):
        cursor = self.cnx.cursor()
        query = """UPDATE sakila.actor SET last_name='GARCIA' WHERE first_name='DAN' AND last_name='TORN';"""
        cursor.execute(query)
        self.cnx.commit()
        return "Table has been updated"

    def insert_into_table(self):
        cursor = self.cnx.cursor()
        query = """INSERT INTO sakila.actor (actor_id, first_name, last_name, last_update) VALUES(201, 'DANNY', 'GARCIA', now());"""
        cursor.execute(query)
        self.cnx.commit()
        return "Row has been inserted"

    def delete_from_table(self):
        cursor = self.cnx.cursor()
        query = """DELETE FROM sakila.actor WHERE first_name='DANNY' AND last_name='GARCIA'"""
        cursor.execute(query)
        self.cnx.commit()
        return "Row has been deleted"

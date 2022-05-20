"""This class handles the connection to db
and it consults the tables
"""
import logging
from os import environ
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import errorcode
from mysql.connector import connect

load_dotenv()

class SQLConnection:
    """Class for making a connection to mysql
    """
    def __init__(self) -> None:
        self.config = {
            'user': environ.get('USER_DB'),
            'password': environ.get('PWD_DB'),
            'host': environ.get('HOST'),
            'database': environ.get('DB'),
            'port': str(environ.get('PORT'))
        }
        self.cnx = None

    def connection(self):
        """Make a connection to mysql
        Returns:
            class: return cursor connection
        """
        try:
            self.cnx = connect(**self.config)
            cursor = self.cnx.cursor()
            return cursor
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.error(
                    "Something is wrong with your user name or password"
                    )
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
            else:
                logging.error(err)

    def make_query(self):
        """
            it class does a consult regarding to
            filters of the challenge
        """
        cursor = self.connection()
        query = """
            SELECT pro.address,pro.city,pro.price,pro.description\
            ,pro.year,MAX(status.name) estado,MAX(stat.update_date) up_date,\
            pro.id pro_id,MAX(stat.status_id) stat_id FROM status_history AS\
            stat INNER JOIN 
            property as pro ON stat.property_id=pro.id
            INNER JOIN status ON stat.status_id=status.id
            WHERE status.id IN (3,4,5) AND pro.address <> '' AND \
            pro.`year`  <> ''
            GROUP BY pro_id  HAVING MAX(stat.update_date) 
            ORDER BY stat.update_date DESC"""
        cursor.execute(query)
        result = []
        for item in cursor:
            result.append(
                {
                    "address": item[0],
                    "city": item[1],
                    "price": item[2],
                    "description": item[3],
                    "year": item[4],
                    "status": item[5]
                }
            )
        self.cnx.close()
        return result
    
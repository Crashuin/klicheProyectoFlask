from werkzeug.security import generate_password_hash

import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        return psycopg2.connect(
            host = config('PGSQL_HOST'),
            user = config('PGSQL_USER'),
            password = config('PGSQL_PASSWORD'),
            database = config('PGSQL_DATABASE'),
            port = config('PGSQL_PORT')
        )
    except DatabaseError as ex:
        raise ex
    

class ProductoModel():

    @classmethod
    def register(self, producto):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """INSERT INTO categoria ("nomCategoria")
                     VALUES ('{}')""".format(categoria.nomCategoria)
                cursor.execute(sql)
                connection.commit()
                return True
        except Exception as e:
            raise Exception(e)
        finally:
            connection.close()
    
    @classmethod
    def listar_categorias(cls):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT * FROM categoria"""
                cursor.execute(sql)
                clientes = cursor.fetchall()
                return clientes
        except Exception as e:
            raise Exception(e)
        finally:
            connection.close()

    
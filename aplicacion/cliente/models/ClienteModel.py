from .entities.ClienteEntity import Cliente
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

class ClienteModel():
    @classmethod
    def register(self, cliente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """INSERT INTO cliente (nombre, contrasena, direccion, documento, email, "fechaNacimiento")
                     VALUES (%s, %s, %s, %s, %s, %s)"""
                
                values = (
                    cliente.nombre,
                    generate_password_hash(cliente.contrasena),
                    cliente.direccion,
                    cliente.documento,
                    cliente.email,
                    cliente.fechaNacimiento,
                )
                
                cursor.execute(sql, values)
                connection.commit()
                print(cliente)
                return True
        except Exception as e:
            raise Exception(e)
        finally:
            connection.close()

    @classmethod
    def listar_clientes(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT * FROM cliente"""
                cursor.execute(sql)
                clientes = cursor.fetchall()
                return clientes
        except Exception as e:
            raise Exception(e)
        finally:
            connection.close()
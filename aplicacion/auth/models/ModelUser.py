from .entities.User import User

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

class ModelUser():
    @classmethod
    def login(self, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT id, usuario , contrasena, nombre, perfil, estado, ultimo_login, fecha_creacion FROM usuario 
                    WHERE usuario = '{}'""".format(user.usuario)
                cursor.execute(sql, (user.usuario))
                row = cursor.fetchone()

                if row is not None:
                    user = User(row[0], row[1], User.check_password(row[2], user.contrasena), row[3], row[4], row[5], row[6], row[7])
                    return user
                else:
                    return None

        except Exception as e:
            raise Exception(e)
        
    @classmethod
    def get_by_id(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT id, usuario, nombre, perfil, estado, ultimo_login, fecha_creacion FROM usuario 
                    WHERE id = '{}'""".format(id)
                cursor.execute(sql)
                row = cursor.fetchone()

                if row is not None:
                    logged_user = User(row[0], row[1], None ,row[2], row[3], row[4], row[5], row[6])
                    return logged_user
                else:
                    return None
        except Exception as e:
            raise Exception(e)
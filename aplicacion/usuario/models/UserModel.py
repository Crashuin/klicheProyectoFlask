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

class UserModel():

    @classmethod
    def register(self, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """INSERT INTO usuario (usuario, contrasena, nombre, perfil, estado)
                    VALUES ('{}', '{}', '{}', '{}', '{}')""".format(user.usuario, user.contrasena, user.nombre, user.perfil, user.estado)
                cursor.execute(sql)
                connection.commit()
                return True
        except Exception as e:
            raise Exception(e)
        finally:
            connection.close()

    @classmethod
    def listar_usuarios(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT * FROM usuario"""
                cursor.execute(sql)
                users = cursor.fetchall()
                print(users)
                return users
        except Exception as e:
            raise Exception(e)
        finally:
            connection.close()
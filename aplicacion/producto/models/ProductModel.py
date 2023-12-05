from werkzeug.security import generate_password_hash

#conexion a bd
from ...connection import get_connection
    

class ProductoModel():

    @classmethod
    def register(self, producto):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """INSERT INTO categoria ("nomCategoria")
                     VALUES ('{}')""".format(producto.nomCategoria)
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

    

import logging
from decouple import config
from flask import render_template

import mysql.connector


def get_connection():
    try:
        return mysql.connector.connect(
            host=config('MYSQL_HOST'),
            user=config('MYSQL_USER'),
            password=config('MYSQL_PASSWORD'),
            database=config('MYSQL_DATABASE'),
            port=config('MYSQL_PORT', default=3306, cast=int),
        )
    except Exception as e:
        logging.error(f"Error en la base de datos: {e}")
        if e.errno  == 2003 or e.errno  == 2006 or e.errno  == 1146:
                return render_template('error_conexion_servidor.html')
        return render_template('500.html'), 500


    

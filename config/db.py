# config/db.py

import psycopg2
from psycopg2 import pool

conexion_pool = psycopg2.pool.SimpleConnectionPool(
minconn=1,
maxconn=10,
host="localhost",
port="5432",
dbname="libreria",
user="postgres",
password="toorMaverick08"
)

def obtener_conexion():
    return conexion_pool.getconn()

def liberar_conexion(conn):
    conexion_pool.putconn(conn)
    
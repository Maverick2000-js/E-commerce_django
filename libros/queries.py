# libros/queries.py
from config.db import obtener_conexion, liberar_conexion

def obtener_libros_disponibles():
    conn = obtener_conexion()
    try:
        cur = conn.cursor()
        cur.execute(
        "SELECT id, titulo, precio, publicado_en, autor_id "
        "FROM libros_libro WHERE disponible = TRUE;"
        )
        columnas = [desc[0] for desc in cur.description]
        filas = cur.fetchall()
        cur.close()
        return [dict(zip(columnas, fila)) for fila in filas]
    finally:
        liberar_conexion(conn)

def obtener_libro_por_id(libro_id):
    conn = obtener_conexion()
    try:
        cur = conn.cursor()
        cur.execute(
        "SELECT id, titulo, precio, disponible, publicado_en, autor_id "
        "FROM libros_libro WHERE id = %s;",
        (libro_id,)
        )
        columnas = [desc[0] for desc in cur.description]
        fila = cur.fetchone()
        cur.close()
        return dict(zip(columnas, fila)) if fila else None
    finally:
        liberar_conexion(conn)

def crear_libro(titulo, precio, publicado_en, autor_id):
    conn = obtener_conexion()
    try:
        cur = conn.cursor()
        cur.execute(
        "INSERT INTO libros_libro (titulo, precio, disponible, publicado_en,autor_id) "
        "VALUES (%s, %s, TRUE, %s, %s) RETURNING id;",
        (titulo, precio, publicado_en, autor_id)
        )
        nuevo_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        return nuevo_id
    except Exception:
        conn.rollback()
        raise
    finally:
        liberar_conexion(conn)

def actualizar_precio(libro_id, nuevo_precio):
    conn = obtener_conexion()
    try:
        cur = conn.cursor()
        cur.execute(
        "UPDATE libros_libro SET precio = %s WHERE id = %s;",
        (nuevo_precio, libro_id)
        )
        conn.commit()
        cur.close()
    except Exception:
        conn.rollback()
        raise
    finally:
        liberar_conexion(conn)

def eliminar_libro(libro_id):
    conn = obtener_conexion()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM libros_libro WHERE id = %s;", (libro_id,))
        conn.commit()
        cur.close()
    except Exception:
        conn.rollback()
        raise
    finally:
        liberar_conexion(conn)

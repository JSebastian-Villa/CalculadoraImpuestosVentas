import psycopg2

def obtener_conexion():
    try:
        conexion = psycopg2.connect(
            dbname="credit_card_c2vn",
            user="profesor",
            password="nzvqS1m7Hb2JLjGarf8WKjyYyyiw1LLg",
            host="dpg-d3dvornfte5s73f2djm0-a.virginia-postgres.render.com",
            port="5432"
        )
        print(" Conexión exitosa a la base de datos")
        return conexion
    except Exception as e:
        print(" Error al conectar con la base de datos:", e)
        return None

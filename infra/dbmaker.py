import pyodbc


def connection(config: dict) -> pyodbc.connect:
    """ Conexao DNS com o banco de dados DBMaker. """
    try:
        return pyodbc.connect("DSN={}".format(config['dsn']))
    except pyodbc.Error as e:
        raise Exception(e)


def select_client(config: dict) -> list:
    conn = connection(config).cursor()
    try:
        cursor = conn.cursor()
        cursor.execute(""" select * from cadcli61 """)
        for row in cursor.fetchall():
            print(row)
    except Exception as e:
        raise Exception(f"erro ao conectar ao banco : {e}")
    finally:
        conn.close()

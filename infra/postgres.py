import psycopg2


def conection(config: dict) -> psycopg2.connect:
    """ Conexao com o banco de dados postgres. """

    try:
        string_connection = f"dbname='{config['dbname']}' user='{config['user']}' " \
                            f"host='{config['host']}' port='{config['port']}'" \
                            f" password='{config['password']}'"

        return psycopg2.connect(string_connection)
    except Exception as e:
        raise Exception(f"erro ao conectar ao banco : {e}")


def select_client(config: dict) -> list:
    """  seleciona todos da tabela xpto. """

    conn = conection(config)
    try:
        cursor = conn.cursor()
        cursor.execute(""" select * from portal_matricula_empresa """)
        for row in cursor.fetchall():
            print(row)
    except Exception as e:
        raise Exception(f"erro ao conectar ao banco : {e}")
    finally:
        conn.close()

from fastapi import FastAPI
import psycopg2
from psycopg2 import Error

app = FastAPI()

# Configurações de conexão com o PostgreSQL
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "nome_do_banco_de_dados"
DB_USER = "nome_do_usuario"
DB_PASSWORD = "senha_do_usuario"


def fetch_data_from_postgres(query):
    try:
        # Estabelece conexão com o PostgreSQL
        connection = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )

        # Cria um cursor para executar queries
        cursor = connection.cursor()

        # Executa a consulta
        cursor.execute(query)

        # Recupera os resultados
        records = cursor.fetchall()

        # Fecha a conexão e o cursor
        cursor.close()
        connection.close()

        return records

    except (Exception, Error) as error:
        print("Erro ao conectar ao PostgreSQL:", error)


@app.get("/consulta-postgres/")
async def consultar_postgres():
    # Exemplo de consulta
    query = "SELECT * FROM tabela_exemplo;"

    # Executa a consulta no PostgreSQL
    results = fetch_data_from_postgres(query)

    # Formata os resultados em um formato JSON
    json_results = []
    for row in results:
        json_results.append({
            "coluna1": row[0],
            "coluna2": row[1],
            # Adicione mais colunas conforme necessário
        })

    return json_results

from flask import Flask
import psycopg2
import os

app1 = Flask(__name__)

@app1.route('/')
def ola():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        conn.close()
        return "Conexão com o banco PostgreSQL foi um sucesso! 🚀"
    except Exception as e:
        return f"Erro ao conectar com o banco: {e}"

if __name__ == '__main__':
    app1.run(host='0.0.0.0', port=5000)

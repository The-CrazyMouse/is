from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello_worl():
    return 'hello, World!'

@app.route('/db')
def db_connect():
    connection = mysql.connector.connect(
        host='db',
        user='root',
        password='root_password',
        database='meu_database'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT 'Conexão à base de dados bem-sucedida!'")
    result = cursor.fetchone()
    return result[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0')

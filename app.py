from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Tanner Fred in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://tannerfred_render_db_user:oWVnIWXKZ90bLETVzc5bimrh51iktj9R@dpg-dbo0mkjrjlhs73a3n8v0-a/tannerfred_render_db")
    conn.close()
    return "Database Connetion Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://tannerfred_render_db_user:oWVnIWXKZ90bLETVzc5bimrh51iktj9R@dpg-dbo0mkjrjlhs73a3n8v0-a/tannerfred_render_db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
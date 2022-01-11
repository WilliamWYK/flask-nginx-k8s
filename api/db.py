#db.py
import os
import pymysql
from flask import jsonify

db_user = 'dbuser'
db_password = '1234'
db_name = 'users'
db_host = '10.77.80.3'


def open_connection():
    try:
        conn = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name, cursorclass=pymysql.cursors.DictCursor)
    except pymysql.MySQLError as e:
        print(e)

    return conn

def get_users():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM users;')
        users = cursor.fetchall()
        
        if result > 0:
            got_users = jsonify(users)
        else:
            got_users = 'No User In DB'
    conn.close()
    return got_users

def add_user(user):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO users (name, age, weight) VALUES(%s, %s, %s)', (user["name"], user["age"], user["weight"]))
    conn.commit()
    conn.close()

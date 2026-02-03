import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="jhonsamie#1205",
        database="gest_patrimoine"
    )
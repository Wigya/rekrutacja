import psycopg2

connection = psycopg2.connect(
    host="postgres", user="user", password="user123", database="db", port=5432)

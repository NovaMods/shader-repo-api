import os
import psycopg2
import psycopg2.extensions


def connect_to_database():
    db_user = os.environ['DB_USER']
    db_pass = os.environ['DB_PASS']

    available_port = 5432

    conn = psycopg2.connect(f'postgresql://{db_user}:{db_pass}@localhost:{available_port}/shaderrepo')

    return conn


connection = connect_to_database()

import os
import time

import psycopg2
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates PostgreSQL database if it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument('--db_name', help="Database name")
        parser.add_argument('--db_user', help="Database user")
        parser.add_argument('--db_password', help="Database user password")
        parser.add_argument('--db_host', help="Database host")
        parser.add_argument('--db_port', help="Database port")

    def handle(self, *args, **options):
        db_name = options.get('db_name') or os.getenv('DJANGO_DB_NAME')
        db_user = options.get('db_user') or os.getenv('DJANGO_DB_USER')
        db_password = options.get('db_password') or os.getenv('DJANGO_DB_PASSWORD')
        db_host = options.get('db_host') or os.getenv('DJANGO_DB_HOST')
        db_port = options.get('db_port') or os.getenv('DJANGO_DB_PORT')

        def wait_for_db_creation():
            while True:
                try:
                    psycopg2.connect(
                        dbname=db_name,
                        host=db_host,
                        port=db_port,
                        user=db_user,
                        password=db_password
                    ).close()
                    return
                except psycopg2.OperationalError:
                    time.sleep(0.1)

        try:
            psycopg2.connect(dbname=db_name, host=db_host, port=db_port, user=db_user, password=db_password).close()
        except psycopg2.OperationalError:  # Если нужной БД не существует
            conn = psycopg2.connect(dbname='postgres', host=db_host, port=db_port, user=db_user, password=db_password)
            conn.autocommit = True
            with conn.cursor() as cur:
                cur.execute(f'CREATE DATABASE {db_name} OWNER {db_user}')
                cur.execute(f'REVOKE CONNECT ON DATABASE {db_name} FROM PUBLIC')
            conn.close()
            wait_for_db_creation()
            print(f'Database "{db_name}" created')

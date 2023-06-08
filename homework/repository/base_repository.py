import psycopg2


class BaseRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            user='postgres',
            password='postgres',
            host='127.0.0.1',
            port='5432',
            database='teachers_subjects'
        )

        self.connection.set_session(autocommit=True)
        self.cursor = self.connection.cursor()
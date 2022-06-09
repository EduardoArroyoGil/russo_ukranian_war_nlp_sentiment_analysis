import sqlalchemy as alch
from sqlalchemy.exc import SQLAlchemyError
import logging

# DB_ROOT_PASSWORD='1234567890'
class Load:

    def __init__(self, db_name, password):

        self.db_name = db_name
        self.password = password

    def server_conn(self):
        connection = f"mysql+pymysql://root:{self.password}@localhost"
        return alch.create_engine(connection)


    def create_db(self):
        engine = self.server_conn()
        try:
            engine.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_name};")

        except:
            logging.debug("DB already exists")

    def db_conn(self):

        connection = f"mysql+pymysql://root:{self.password}@localhost/{self.db_name}"
        return alch.create_engine(connection)

    def create_insert_table(self, query):
        engine = self.db_conn()


        try:
            engine.execute(query)

        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error

    def get_id(self, link, col_id,  column, table):

        engine = self.db_conn()

        try:
            query_sacar_id = f"SELECT {col_id} FROM {table} WHERE {column} = '{link}'"

            id_ = engine.execute(query_sacar_id).first()

            if not id_:
                return "That id already exists in DB"
            else:
                return engine.execute(query_sacar_id).first()[0]

        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error

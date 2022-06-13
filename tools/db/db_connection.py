import pandas as pd
import sqlalchemy as alch
from sqlalchemy.exc import SQLAlchemyError
import logging
import datetime


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
            logging.debug(error)
            return error

    def read_table(self, schema, table):

        engine = self.db_conn()

        query = f"SELECT * FROM {schema}.{table}"

        sql_df = pd.read_sql(
            query,
            con=engine
        )

        if 'date_inserted' in sql_df.columns:
            sql_df.drop(columns='date_inserted', inplace=True)

        return sql_df

    def get_id(self, record, col_id,  column, schema, table):

        engine = self.db_conn()

        try:
            query_get_id = f"SELECT {col_id} FROM {schema}.{table} WHERE {column} = '{record}'"

            id_ = engine.execute(query_get_id).first()

            if not id_:
                return "That tweet_id doesn't exist in DB"
            else:
                return engine.execute(query_get_id).first()[0]

        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error

    def insert_raw_tweets_into_db(self, df, schema, table):
        '''

        :param df:
        :param schema:
        :param table:
        :return:
        '''
        inserted_records = 0
        error_inserted_records = 0
        skipped_inserted_records = 0
        df_columns = list(df.columns)
        df_columns.remove('Unnamed: 0')

        string_df_columns = ",".join(df_columns)

        string_df_columns = ' ('+string_df_columns+',date_inserted'+') '

        for index, row in df.iterrows():

            # ct stores current time
            ct = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            query = f"""INSERT INTO {schema}.{table} {string_df_columns} 
                                VALUES ( 
                                {row["account_id"]}
                                , {row["account_id_check"]}
                                , {row["tweet_id"]}
                                , "{row["account_username"]}"
                                , "{row["account_name"]}"
                                , '{row["tweet_text"]}'
                                , "{row["tweet_created_at"]}"
                                , "{row["tweet_language"]}"
                                , {row["retweet_count"]}
                                , {row["reply_count"]}
                                , {row["like_count"]}
                                , {row["quote_count"]}
                                , "{row["profile_image_url"]}"
                                , {row["is_reclaimable"]}
                                , "{ct}"
                                );"""

            tweet_id = self.get_id(record=row["tweet_id"], col_id="tweet_id", column="tweet_id", schema=schema, table=table)

            if tweet_id == "That tweet_id doesn't exist in DB":
                error = self.create_insert_table(query)
                if not error:
                    inserted_records += 1
                else:
                    print('tweet ', row['tweet_id'], " has been failed in the insertion into the DB")
                    error_inserted_records += 1
            else:
                print('tweet ', row['tweet_id'], " already exists in DB")
                skipped_inserted_records += 1

        print(f"{inserted_records} records have been inserted \n",
              f"{error_inserted_records} records haven't been inserted into {schema}.{table} due to insert errors \n",
              f"{skipped_inserted_records} records haven't been inserted due to they're already in {schema}.{table}")

    def insert_transformed_tweets_into_db(self, df, schema, table):
        '''

        :param df:
        :param schema:
        :param table:
        :return:
        '''
        inserted_records = 0
        error_inserted_records = 0
        skipped_inserted_records = 0
        df_columns = list(df.columns)

        string_df_columns = ",".join(df_columns)

        string_df_columns = ' ('+string_df_columns+',date_inserted'+') '

        for index, row in df.iterrows():

            # ct stores current time
            ct = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            query = f"""INSERT INTO {schema}.{table} {string_df_columns} 
                                VALUES ( 
                                {row["account_id"]}
                                , {row["account_id_check"]}
                                , {row["tweet_id"]}
                                , "{row["account_username"]}"
                                , "{row["account_name"]}"
                                , '{row["tweet_text"]}'
                                , "{row["tweet_created_at"]}"
                                , "{row["tweet_language"]}"
                                , {row["retweet_count"]}
                                , {row["reply_count"]}
                                , {row["like_count"]}
                                , {row["quote_count"]}
                                , "{row["profile_image_url"]}"
                                , {row["is_reclaimable"]}
                                , "{row["tweet_text_translated_gpt3"]}"
                                , "{row["tweet_emotion_gpt3"]}"
                                , "{ct}"
                                );"""

            tweet_id = self.get_id(record=row["tweet_id"], col_id="tweet_id", column="tweet_id", schema=schema, table=table)

            if tweet_id == "That tweet_id doesn't exist in DB":
                error = self.create_insert_table(query)
                if not error:
                    inserted_records += 1
                else:
                    print('tweet ', row['tweet_id'], f" has been failed in the insertion into the DB due to: {error}")
                    error_inserted_records += 1
            else:
                print('tweet ', row['tweet_id'], " already exists in DB")
                skipped_inserted_records += 1

        print(f"{inserted_records} records have been inserted into {schema}.{table}\n",
              f"{error_inserted_records} records haven't been inserted into {schema}.{table} due to insert errors \n",
              f"{skipped_inserted_records} records haven't been inserted due to they're already in {schema}.{table}")
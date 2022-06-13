import twitter_module.twitter_transformation as twitter_transformation
import tools.db.db_connection as db_connection

import pandas as pd
import logging
import os
from dotenv import load_dotenv
from pathlib import Path


def start(df=pd.read_csv('data/sample/twitter_df_gpt3.csv')):
    '''

    :return:
    '''

    df_columns = list(df.columns)
    if 'Unnamed: 0' in df_columns:
        df.drop(columns='Unnamed: 0', inplace=True)

    dotenv_path = Path("./.env")
    load_dotenv(dotenv_path=dotenv_path)

    db_root_password = os.getenv("DB_ROOT_PASSWORD")
    db_transformed = db_connection.Load(db_name='twitter_transformed', password=db_root_password)
    logging.debug('connected to db_transformed')

    #  INSERTING GPT3 TRANSFORMED DATA INTO DB
    logging.info('INSERTING GPT3 TRANSFORMED DATA INTO DB')
    db_transformed.insert_transformed_tweets_into_db(df, schema='twitter_transformed', table='tweets_emotional')
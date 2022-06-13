import openai_module.openai_trasnformation as openai_transformation
import twitter_module.twitter_connection as twitter_connection
import twitter_module.twitter_transformation as twitter_transformation
import tools.db.db_connection as db_connection
import tools.db.queries_table_generator as query_generator

import pandas as pd
from tqdm.auto import tqdm  # https://tqdm.github.io/docs/tqdm/#pandas
import logging
import os
from dotenv import load_dotenv
from pathlib import Path


def start():
    '''

    :return:
    '''

    dotenv_path = Path("./.env")
    load_dotenv(dotenv_path=dotenv_path)


    # READ TWEETS FROM DB
    db_root_password = os.getenv("DB_ROOT_PASSWORD")
    db_raw = db_connection.Load(db_name='twitter_transformed', password=db_root_password)
    logging.debug('connected to db_raw')
    logging.info('READ TWEETS FROM DB')

    df = db_raw.read_table(schema='twitter_raw', table='tweets_raw')

    return df
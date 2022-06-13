import twitter_module.twitter_transformation as twitter_transformation
import tools.db.db_connection as db_connection

import pandas as pd
import logging
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path("./.env")
load_dotenv(dotenv_path=dotenv_path)

twitter_utils = twitter_transformation.TwitterUtils()

db_root_password = os.getenv("DB_ROOT_PASSWORD")
db_raw = db_connection.Load(db_name='twitter_transformed', password=db_root_password)
logging.debug('connected to db_raw')

#  INSERTING RAW DATA INTO DB
logging.info('INSERTING RAW DATA INTO DB')
df = pd.read_csv('data/sandbox/twitter_df.csv')

df = twitter_utils.align_column_raw_types_to_insert(df)

db_raw.insert_raw_tweets_into_db(df, schema='twitter_raw', table='tweets_raw')
import tools.db.db_connection as db_connection
import tools.db.queries_table_generator as query_generator

import logging
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path("./.env")
load_dotenv(dotenv_path=dotenv_path)


#  CONNECTING TO DB
db_root_password = os.getenv("DB_ROOT_PASSWORD")
db_raw = db_connection.Load(db_name='twitter_raw', password=db_root_password)
logging.debug('connected to db_raw')

db_raw.create_db()
logging.debug('create db_raw if not exists')

q_gen = query_generator.RawTables()
db_raw.create_insert_table(query=q_gen.create_tweets_raw)
logging.debug('create table  if not exists')

db_raw = db_connection.Load(db_name='twitter_transformed', password=db_root_password)
logging.debug('connected to db_raw')

db_raw.create_db()
logging.debug('create db_raw if not exists')

q_gen = query_generator.RawTables()
db_raw.create_insert_table(query=q_gen.create_tweets_transformed)
logging.debug('create table  if not exists')

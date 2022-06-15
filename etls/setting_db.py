import tools.db.db_connection as db_connection
import tools.db.queries_table_generator as query_generator

import logging
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path("./.env")
load_dotenv(dotenv_path=dotenv_path)


def start():
    '''

    :return:
    '''
    #  CONNECTING:

    #  RAW TO DB
    db_root_password = os.getenv("DB_ROOT_PASSWORD")
    db_raw = db_connection.Load(db_name='twitter_raw', password=db_root_password)
    logging.debug('connected to db_raw')

    db_raw.create_db()
    logging.debug('create db_raw if not exists')

    q_gen = query_generator.RawObjects()
    db_raw.create_insert_table(query=q_gen.create_tweets_raw)
    logging.debug('create table if not exists: tweets_raw')
    db_raw.create_insert_table(query=q_gen.create_v_twitter_accounts_raw)
    logging.debug('create or replace view: v_twitter_accounts_raw')
    db_raw.create_insert_table(query=q_gen.create_v_twitter_accounts_metrics_raw)
    logging.debug('create or replace view: v_twitter_accounts_metrics_raw')
    db_raw.create_insert_table(query=q_gen.create_v_tweets_priority_raw)
    logging.debug('create or replace view: v_tweets_priority_raw')

    # TRANSFORMED DB

    db_transformed = db_connection.Load(db_name='twitter_transformed', password=db_root_password)
    logging.debug('connected to db_transformed')

    db_transformed.create_db()
    logging.debug('create db_transformed if not exists')

    q_gen = query_generator.TransformedObjects()
    db_transformed.create_insert_table(query=q_gen.create_tweets_emotional)
    logging.debug('create table if not exists: tweets_emotional')
    db_transformed.create_insert_table(query=q_gen.create_v_tweets_emotional_model)
    logging.debug('create or replace view: v_tweets_emotional_model')

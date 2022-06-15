import tools.db.db_connection as db_connection
import logging
import os
from dotenv import load_dotenv
from pathlib import Path
import datetime


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

    df = db_raw.read_table(schema='twitter_raw', table='v_tweets_priority_raw', where='priority=2')

    # ct stores current time
    ct = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    df.sample(5).to_csv('data/sample/twitter_raw.tweets_raw/tweets_raw.csv')
    df.to_csv(f'data/production/twitter_raw.tweets_raw/tweets_raw_refreshed_{ct}.csv')

    return df
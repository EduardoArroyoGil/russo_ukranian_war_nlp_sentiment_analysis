import twitter_module.twitter_connection as twitter_connection
import twitter_module.twitter_transformation as twitter_transformation

from tqdm.auto import tqdm  # https://tqdm.github.io/docs/tqdm/#pandas
import logging
import os
from dotenv import load_dotenv
from pathlib import Path
import datetime


def start():

    dotenv_path = Path("./.env")
    load_dotenv(dotenv_path=dotenv_path)

    #  CONNECTING TO TWITTER
    twitter_bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    twitter_conn = twitter_connection.Twitter(bearer_token=twitter_bearer_token)
    logging.debug('connected to Twitter')

    #  EXTRACTING DATA FROM TWITTER
    logging.info('EXTRACT DATA FROM TWITTER')
    twitter_response, twitter_df = twitter_conn.search_recent_tweet(text_to_search='Guerra de Ucrania', number_of_pages=1000)

    twitter_utils = twitter_transformation.TwitterUtils()
    logging.debug('Start Check of accounts')
    tqdm.pandas(desc="ETL is chekcing viability of accounts", colour='blue')
    twitter_df["is_reclaimable"] = twitter_df.progress_apply(lambda x: twitter_utils
                                                             .check_correct_acc_tw_association(x.account_id,
                                                                                               x.account_id_check), axis=1)
    logging.debug('Finish Check of accounts')

    df_columns = list(twitter_df.columns)
    if 'Unnamed: 0' in df_columns:
        twitter_df.drop(columns='Unnamed: 0', inplace=True)

    # ct stores current time
    ct = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    twitter_df.sample(5).to_csv('data/sample/twitter_df.csv')
    twitter_df.to_csv(f'data/production/twitter_df_{ct}.csv')

    return twitter_df

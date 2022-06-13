import etls.setting_db as setting_db
import etls.inserting_raw_data_into_db as inserting_raw_data_into_db

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

dotenv_path = Path(".env")
load_dotenv(dotenv_path=dotenv_path)

logging.debug('Inside the ETL')

#  CONNECTING TO TWITTER AND OPENAI
# twitter_bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
# twitter_conn = twitter_connection.Twitter(bearer_token=twitter_bearer_token)
# logging.debug('connected to Twitter')
gpt3_api_key = os.getenv("GPT3_API_KEY")
gpt3_transformation = openai_transformation.GPT3Transformation(api_key=gpt3_api_key)
logging.debug('connected to GPT3')


#  CONNECTING TO DB
setting_db


#  EXTRACTING DATA FROM TWITTER
# logging.info('EXTRACT DATA FROM TWITTER')
# twitter_response, twitter_df = twitter_conn.search_recent_tweet_100(text_to_search='Guerra de Ucrania', max_results=10)
#
twitter_utils = twitter_transformation.TwitterUtils()
# logging.debug('Start Check of accounts')
# tqdm.pandas(desc="ETL is chekcing viability of accounts", colour='blue')
# twitter_df["is_reclaimable"] = twitter_df.progress_apply(lambda x: twitter_utils
#                                                          .check_correct_acc_tw_association(x.account_id,
#                                                                                            x.account_id_check), axis=1)
# logging.debug('Finish Check of accounts')
# twitter_df.to_csv('data/sandbox/twitter_df.csv')

#  INSERTING RAW DATA INTO DB
inserting_raw_data_into_db

# READ TWEETS FROM DB
db_root_password = os.getenv("DB_ROOT_PASSWORD")
db_raw = db_connection.Load(db_name='twitter_transformed', password=db_root_password)
logging.debug('connected to db_raw')
logging.info('READ TWEETS FROM DB')

df = db_raw.read_table(schema='twitter_raw', table='tweets_raw')

#  EMOTIONAL ANALYSIS FOR EACH TWEET WITH GPT3
logging.info('EMOTIONAL ANALYSIS FOR EACH TWEET WITH GPT3')

logging.debug('Start Translate tweets to english')
tqdm.pandas(desc="GPT3 is translating", colour='black')
df["tweet_text_translated_gpt3"] = df["tweet_text"].progress_apply(gpt3_transformation
                                                                                   .translate_to_english)
logging.debug('Finish Translate tweets to english')

# logging.debug('Start classification of language for each tweet')
# tqdm.pandas(desc="GPT3 is checking the language of the tweet", colour='black')
# df["tweet_language_gpt3"] = df["tweet_text"].progress_apply(gpt3_transformation.language_of_text)
# logging.debug('Finish classification of language for each tweet')

logging.debug('Start emotional analysis by GPT3')
tqdm.pandas(desc="GPT3 analyzing the emotion of the tweet!!!!", colour='black')
df["tweet_emotion_gpt3"] = df["tweet_text"].progress_apply(gpt3_transformation.emotion_of_text)
logging.debug('Finish emotional analysis by GPT3')

#  INSERTING GPT3 TRANSFORMED DATA INTO DB
logging.info('INSERTING GPT3 TRANSFORMED DATA INTO DB')

db_raw.insert_transformed_tweets_into_db(df, schema='twitter_transformed', table='tweets_emotional')
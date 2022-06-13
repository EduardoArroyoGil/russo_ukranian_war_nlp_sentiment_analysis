import etls.setting_db as setting_db
import etls.inserting_raw_data_into_db as inserting_raw_data_into_db
import etls.extraction_raw_db as extraction_raw_db
import etls.transforming_gpt3 as transforming_gpt3
import etls.inserting_transformed_gpt3_into_db as inserting_transformed_gpt3_into_db

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

#  CONNECTING TO TWITTER
# twitter_bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
# twitter_conn = twitter_connection.Twitter(bearer_token=twitter_bearer_token)
# logging.debug('connected to Twitter')


#  CONNECTING TO DB
setting_db.start()


#  EXTRACTING DATA FROM TWITTER
# logging.info('EXTRACT DATA FROM TWITTER')
# twitter_response, twitter_df = twitter_conn.search_recent_tweet_100(text_to_search='Guerra de Ucrania', max_results=10)
#
# twitter_utils = twitter_transformation.TwitterUtils()
# logging.debug('Start Check of accounts')
# tqdm.pandas(desc="ETL is chekcing viability of accounts", colour='blue')
# twitter_df["is_reclaimable"] = twitter_df.progress_apply(lambda x: twitter_utils
#                                                          .check_correct_acc_tw_association(x.account_id,
#                                                                                            x.account_id_check), axis=1)
# logging.debug('Finish Check of accounts')
# twitter_df.to_csv('data/sandbox/twitter_df.csv')

#  INSERTING RAW DATA INTO DB
inserting_raw_data_into_db.start()

# READ TWEETS FROM DB
df_raw = extraction_raw_db.start()

#  EMOTIONAL ANALYSIS FOR EACH TWEET WITH GPT3
df_trans = transforming_gpt3.start(df_raw)

#  INSERTING GPT3 TRANSFORMED DATA INTO DB
inserting_transformed_gpt3_into_db.start(df_trans)

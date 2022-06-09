import openai_module.openai_connection as openai_connection
import openai_module.openai_trasnformation as openai_trasnformation
import twitter_module.twitter_connection as twitter_connection
import twitter_module.twitter_transformation as twitter_transformation
import tools.db.db_connection as db_connection
import pandas as pd
import re

from tqdm.auto import tqdm  # https://tqdm.github.io/docs/tqdm/#pandas
import logging


logging.debug('Inside the ETL')

twitter_conn = twitter_connection.Twitter(bearer_token='AAAAAAAAAAAAAAAAAAAAAHAhdQEAAAAAqIbsC3QZW5jWqDu8%2FF2g%2BhTStug'
                                                       '%3Dq4S5oh53c0j6dlYJRpsVwsKdHe6xuqDIECKtwHonL9g8zAshi0')
logging.debug('connected to Twitter')
# twitter_conn_apikey = twitter_connection.Twitter(consumer_key='kNpZqaQNMmCZYJq617etZ2eDI',
#                                                  consumer_secret='XPo4jhxsaCtPSMmZJoBfBKPtCo3Ta4dtn3s7QvA7HngluokQes',
#                                                  access_token='1239341432135135232-9ekFhk3wxl5RIMY2eLI4IjCOoQY5J1',
#                                                  access_token_secret='ixAXyTs7J29cMvzFem2rk3FDLwtQEyAXk1W6MB3fL6nhD')
gpt3_transformation = openai_trasnformation.GPT3Transformation(api_key='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')
logging.debug('connected to GPT3')

db = db_connection.Load(db_name='twitter_raw', password='1234567890')
logging.debug('connected to db')

db.create_db()
logging.debug('create db if not exists')

twitter_utils = twitter_transformation.TwitterUtils()

#  EXTRACTING DATA FROM TWITTER
logging.info('EXTRACT DATA FROM TWITTER')
twitter_response, twitter_df = twitter_conn.search_recent_tweet_100(text_to_seearch='Guerra de Ucrania')

logging.debug('Start Check of accounts')
tqdm.pandas(desc="ETL is chekcing viability of accounts", colour='blue')
twitter_df["is_reclaimable"] = twitter_df.progress_apply(lambda x: twitter_utils.check_correct_acc_tw_association(x.account_id, x.account_id_check), axis=1)
logging.debug('Finish Check of accounts')
twitter_df.to_csv('data/sandbox/twitter_df.csv')




#  EMOTIONAL ANALYSIS FOR EACH TWEET WITH GPT3
logging.info('EMOTIONAL ANALYSIS FOR EACH TWEET WITH GPT3')

logging.debug('Start Translate tweets to english')
tqdm.pandas(desc="GPT3 is translating", colour='black')
twitter_df["tweet_text_translated_gpt3"] = twitter_df["tweet_text"].progress_apply(gpt3_transformation.translate_to_english)
logging.debug('Finish Translate tweets to english')

logging.debug('Start classification of language for each tweet')
tqdm.pandas(desc="GPT3 is checking the language of the tweet", colour='black')
twitter_df["tweet_language_gpt3"] = twitter_df["tweet_text"].progress_apply(gpt3_transformation.language_of_text)
logging.debug('Finish classification of language for each tweet')

logging.debug('Start emotional analysis by GPT3')
tqdm.pandas(desc="GPT3 analyzing the emotion of the tweet!!!!", colour='black')
twitter_df["tweet_emotion_gpt3"] = twitter_df["tweet_text"].progress_apply(gpt3_transformation.emotion_of_text)
logging.debug('Finish emotional analysis by GPT3')

twitter_df.to_csv('data/sandbox/twitter_df_gpt3.csv')
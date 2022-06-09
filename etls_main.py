import openai_module.openai_connection as openai_connection
import openai_module.openai_trasnformation as openai_trasnformation
import twitter_module.twitter_connection as twitter_connection
import twitter_module.twitter_transformation as twitter_transformation
import pandas as pd
import re
from tqdm.auto import tqdm # https://tqdm.github.io/docs/tqdm/#pandas


twitter_conn = twitter_connection.Twitter(bearer_token='AAAAAAAAAAAAAAAAAAAAAHAhdQEAAAAAqIbsC3QZW5jWqDu8%2FF2g%2BhTStug%3Dq4S5oh53c0j6dlYJRpsVwsKdHe6xuqDIECKtwHonL9g8zAshi0')
# twitter_conn = twitter_connection.Twitter(consumer_key='kNpZqaQNMmCZYJq617etZ2eDI',
#                  consumer_secret='XPo4jhxsaCtPSMmZJoBfBKPtCo3Ta4dtn3s7QvA7HngluokQes',
#                  access_token='1239341432135135232-9ekFhk3wxl5RIMY2eLI4IjCOoQY5J1',
#                  access_token_secret='ixAXyTs7J29cMvzFem2rk3FDLwtQEyAXk1W6MB3fL6nhD')
gpt3_transformation = openai_trasnformation.GPT3Transformation(api_key='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')

twitter_utils = twitter_transformation.TwitterUtils()

#  EMOTIONAL ANALYSIS FOR EACH TWEET
twitter_response, twitter_df = twitter_conn.search_recent_tweet(text_to_seearch='Guerra de Ucrania', number_of_pages=2)
# twitter_response, twitter_df = twitter_conn.search_all_tweet_100(text_to_seearch='Guerra de Ucrania')



tqdm.pandas(desc="ETL is chekcing viability of accounts", colour='blue')
twitter_df["is_reclaimable"] = twitter_df.progress_apply(lambda x: twitter_utils.check_correct_acc_tw_association(x.account_id, x.account_id_check), axis=1)

twitter_df.to_csv('data/sandbox/twitter_df.csv')

tqdm.pandas(desc="GPT3 is translating", colour='black')
twitter_df["tweet_text_translated_gpt3"] = twitter_df["tweet_text"].progress_apply(gpt3_transformation.translate_to_english)

tqdm.pandas(desc="GPT3 is checking the language of the tweet", colour='black')
twitter_df["tweet_language_gpt3"] = twitter_df["tweet_text"].progress_apply(gpt3_transformation.language_of_text)

tqdm.pandas(desc="GPT3 analyzing the emotion of the tweet!!!!", colour='black')
twitter_df["tweet_emotion_gpt3"] = twitter_df["tweet_text"].progress_apply(gpt3_transformation.emotion_of_text)

twitter_df.to_csv('data/sandbox/twitter_df_gpt3.csv')
import openai_module.openai_trasnformation as openai_transformation

import pandas as pd
from tqdm.auto import tqdm  # https://tqdm.github.io/docs/tqdm/#pandas
import logging
import os
from dotenv import load_dotenv
from pathlib import Path

def start(df=pd.read_csv('data/sample/twitter_df.csv')):

    '''

    :param df:  by default transforming df from sample data
    :return:
    '''

    df_columns = list(df.columns)
    if 'Unnamed: 0' in df_columns:
        df.drop(columns='Unnamed: 0', inplace=True)

    dotenv_path = Path("./.env")
    load_dotenv(dotenv_path=dotenv_path)

    #  CONNECTING TO OPENAI
    gpt3_api_key = os.getenv("GPT3_API_KEY")
    gpt3_transformation = openai_transformation.GPT3Transformation(api_key=gpt3_api_key)
    logging.debug('connected to GPT3')

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

    df_columns = list(df.columns)
    if 'Unnamed: 0' in df_columns:
        df.drop(columns='Unnamed: 0', inplace=True)

    df.sample(5).to_csv('data/sample/twitter_df_gpt3.csv')

    return df

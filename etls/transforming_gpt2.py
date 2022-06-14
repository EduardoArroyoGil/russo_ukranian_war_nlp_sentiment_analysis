import transfomer_module.transformer_gpt2 as transformer_gpt2

import pandas as pd
from tqdm.auto import tqdm  # https://tqdm.github.io/docs/tqdm/#pandas
import logging
import datetime

def start(df=pd.read_csv('data/sample/twitter_raw.tweets_raw/tweets_raw.csv')):

    '''

    :param df:  by default transforming df from sample data
    :return:
    '''

    df_columns = list(df.columns)
    if 'Unnamed: 0' in df_columns:
        df.drop(columns='Unnamed: 0', inplace=True)

    #  CONNECTING TO OPENAI
    gpt2_transformation = transformer_gpt2.GPT2Transformation()
    logging.debug('connected to GPT2')

    #  SAVE GPT2 MODELS AND TOKENIZERS
    # gpt2_transformation.download_model_gpt2lmh()
    # gpt2_transformation.download_model_gpt2()
    # gpt2_transformation.download_tokenizer_gpt2lmh()

    #  EMOTIONAL ANALYSIS FOR EACH TWEET WITH GPT2
    logging.info('EMOTIONAL ANALYSIS FOR EACH TWEET WITH GPT2')

    logging.debug('Start Translate tweets to english')
    tqdm.pandas(desc="GPT2 is translating", colour='#a6a6a6')
    df["tweet_text_translated_gpt2"] = df["tweet_text"].progress_apply(gpt2_transformation
                                                                       .translate_to_english)
    logging.debug('Finish Translate tweets to english')

    logging.debug('Start emotional analysis by GPT2')
    tqdm.pandas(desc="GPT2 analyzing the emotion of the tweet!!!!", colour='#a6a6a6')
    df["tweet_emotion_gpt2"] = df["tweet_text_translated_gpt2"].progress_apply(gpt2_transformation.emotion_of_text)
    logging.debug('Finish emotional analysis by GPT2')

    df_columns = list(df.columns)
    if 'Unnamed: 0' in df_columns:
        df.drop(columns='Unnamed: 0', inplace=True)

    # ct stores current time
    ct = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    df.sample(5).to_csv('data/sample/twitter_df_gpt2.csv')
    df.to_csv(f'data/production/twitter_df_gpt2_{ct}.csv')

    return df

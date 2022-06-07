import openai_module.openai_connection as openai_connection
import pandas as pd
import re


class GPT3Transformation:

    def __init__(self, api_key):
        self.api_key = api_key

    def translate_to_english(self, tweet):
        gpt3_conn = openai_connection.GPT3(api_key=self.api_key)

        query = f'Can you translate this tweet to english: {tweet}'
        tweet_translated = gpt3_conn.query(prompt=query)

        return tweet_translated

    def language_of_text(self, tweet):
        gpt3_conn = openai_connection.GPT3(api_key=self.api_key)

        query = f'In what language is this tweet written in just onw word: {tweet}'
        tweet_lan_respond = gpt3_conn.query(prompt=query)
        tweet_lan = re.findall(r'\s(\w+)\.*$', tweet_lan_respond)
        tweet_lan = ''.join(tweet_lan)

        return tweet_lan.capitalize()

    def emotion_of_text(self, tweet):
        gpt3_conn = openai_connection.GPT3(api_key=self.api_key)

        tweet_translated = self.translate_to_english(tweet)

        query = f'Which emotion transmit the following twitt in just one word: {tweet_translated}'
        emo_analysis_respond = gpt3_conn.query(prompt=query)
        emo_analysis = re.findall(r'\s(\w+)\.*$', emo_analysis_respond)
        emo_analysis = ''.join(emo_analysis)

        return emo_analysis.capitalize()
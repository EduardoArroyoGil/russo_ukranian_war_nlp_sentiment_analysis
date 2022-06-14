import tweepy
import pandas as pd
from tqdm import tqdm
import time


class Twitter:

    def __init__(self, bearer_token='',
                 consumer_key='',
                 consumer_secret='',
                 access_token='',
                 access_token_secret=''):

        self.bearer_token = bearer_token
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def get_connection_bearer_token(self):
        '''
        this function is the one that allows to get connection to API twitter based on bearer token
        documentation: https://docs.tweepy.org/en/stable/client.html
        :return: the client that allows to create delete, get, post and put queries
        '''

        bearer_token = self.bearer_token

        client = tweepy.Client(bearer_token=bearer_token)

        return client

    def get_connection_api_key(self):

        consumer_key = self.consumer_key
        consumer_secret = self.consumer_secret
        access_token = self.access_token
        access_token_secret = self.access_token_secret

        client = tweepy.Client(consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token=access_token,
                               access_token_secret=access_token_secret)

        return client

    def get_response_info(self, response):

        '''
        :param response: the response obtained from tweet object of the twitter API
        :return: data frame with the columns designed:
                        "account_id",
                        "account_id_check",
                        "tweet_id",
                        "account_username",
                        "account_name",
                        "tweet_text",
                        "tweet_created_at",
                        "tweet_language",
                        "retweet_count",
                        "reply_count",
                        "like_count",
                        "quote_count",
                        "profile_image_url"
        '''

        no_tweets_data = len(response.data)
        no_tweets_includes_users = len(response.includes["users"])

        data_column_names = ["account_id_check",
                             "tweet_id",
                             "tweet_text",
                             "tweet_created_at",
                             "tweet_language",
                             "retweet_count",
                             "reply_count",
                             "like_count",
                             "quote_count"]

        include_users_column_names = ["account_id",
                                      "account_username",
                                      "account_name",
                                      "profile_image_url"]

        twitter_data_response_df = pd.DataFrame(columns=data_column_names)
        twitter_include_users_response_df = pd.DataFrame(columns=include_users_column_names)

        # Each Tweet object has default ID and text fields
        for index in range(no_tweets_data):
            tweet_id = response.data[index].id
            tweet_text = response.data[index].text
            tweet_created_at = str(response.data[index].created_at)
            tweet_language = response.data[index].lang
            account_id_check = response.data[index].author_id
            retweet_count = response.data[index].public_metrics['retweet_count']
            reply_count = response.data[index].public_metrics['reply_count']
            like_count = response.data[index].public_metrics['like_count']
            quote_count = response.data[index].public_metrics['quote_count']

            row = [account_id_check,
                   tweet_id,
                   tweet_text,
                   tweet_created_at,
                   tweet_language,
                   retweet_count,
                   reply_count,
                   like_count,
                   quote_count]

            twitter_data_response_df_length = len(twitter_data_response_df)
            twitter_data_response_df.loc[twitter_data_response_df_length] = row

        # Each Tweet object has default ID and text fields
        for index in range(no_tweets_includes_users):
            account_username = response.includes["users"][index].username
            account_name = response.includes["users"][index].name
            account_id = response.includes["users"][index].id
            profile_image_url = response.includes["users"][index].profile_image_url

            row = [account_id,
                   account_username,
                   account_name,
                   profile_image_url]

            twitter_include_users_response_df_length = len(twitter_include_users_response_df)
            twitter_include_users_response_df.loc[twitter_include_users_response_df_length] = row

        twitter_response_df = twitter_data_response_df.merge(twitter_include_users_response_df,
                                                             left_on='account_id_check', right_on='account_id',
                                                             how='left')

        column_names_order = ["account_id",
                              "account_id_check",
                              "tweet_id",
                              "account_username",
                              "account_name",
                              "tweet_text",
                              "tweet_created_at",
                              "tweet_language",
                              "retweet_count",
                              "reply_count",
                              "like_count",
                              "quote_count",
                              "profile_image_url"]

        twitter_response_df = twitter_response_df[column_names_order]

        return twitter_response_df.reset_index().drop(columns='index')

    def search_recent_tweet_100(self, text_to_search, max_results=100):
        '''

        just return 100 tweets

        documentation: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent

        :param text_to_search:
        :param max_results:
        :return:
        '''
        # Search Recent Tweets
        # This endpoint/method returns Tweets from the last seven days

        twitter_connection = self.get_connection_bearer_token()

        response = twitter_connection.search_recent_tweets(
            text_to_search,
            tweet_fields=['lang', 'created_at', 'public_metrics', 'entities'],
            user_fields=['profile_image_url'],
            media_fields=['url'],
            expansions=['author_id', 'attachments.media_keys'],
            max_results=max_results)
        # The method returns a Response object, a named tuple with data, includes,

        # In this case, the data field of the Response returned is a list of Tweet
        # objects

        twitter_response_df = self.get_response_info(response)

        return response, twitter_response_df.reset_index().drop(columns='index')

    def search_recent_tweet(self, text_to_search, start_time, end_time, number_of_pages=10 ):
        '''
        return 100*(number of pages) tweets (10 pages by default)
        :param text_to_seearch:
        :param number_of_pages:
        :return:
        '''

        # Search Recent Tweets
        # This endpoint/method returns Tweets from the last seven days

        twitter_connection = self.get_connection_bearer_token()

        responses = tweepy.Paginator(twitter_connection.search_recent_tweets,
                                     text_to_search,
                                     tweet_fields=['lang', 'created_at', 'public_metrics', 'entities'],
                                     user_fields=['profile_image_url'],
                                     media_fields=['url'],
                                     expansions=['author_id', 'attachments.media_keys'],
                                     start_time=start_time,
                                     end_time=end_time,
                                     max_results=100,
                                     limit=number_of_pages)

        # The method returns a Response object, a named tuple with data, includes,

        # In this case, the data field of the Response returned is a list of Tweet
        # objects

        responses_dict = dict()
        twitter_whole_response_df = pd.DataFrame()

        index = 0
        for response in tqdm(responses, total=number_of_pages, colour='blue', desc="ETL is extracting tweets"):
            twitter_response_df = self.get_response_info(response)
            twitter_whole_response_df = pd.concat([twitter_whole_response_df, twitter_response_df])

            responses_dict[index] = response
            time.sleep(2)
            index += 1

        return responses_dict, twitter_whole_response_df.reset_index().drop(columns='index')

    def search_all_tweet_100(self, text_to_seearch,
                             start_time='2020-01-01T00:00:00Z',
                             end_time='2020-08-01T00:00:00Z'):
        # TODO: wating for Twitter approval for Academic Research product track https://developer.twitter.com/en/products/twitter-api/academic-research
        '''

        just return 100 tweets

        documentation: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-all

        :param text_to_seearch:
        :return:
        '''
        # Search Recent Tweets
        # This endpoint/method returns Tweets from the last seven days

        twitter_connection = self.get_connection_api_key()

        response = twitter_connection.search_all_tweets(
            text_to_seearch,
            tweet_fields=['lang', 'created_at', 'public_metrics', 'entities'],
            user_fields=['profile_image_url'],
            media_fields=['url'],
            expansions=['author_id', 'attachments.media_keys'],
            start_time=start_time,
            end_time=end_time,
            max_results=10)
        # The method returns a Response object, a named tuple with data, includes,

        # In this case, the data field of the Response returned is a list of Tweet
        # objects

        twitter_response_df = self.get_response_info(response)

        return response, twitter_response_df.reset_index().drop(columns='index')

    def search_all_tweet(self, text_to_seearch, number_of_pages=10,
                             start_time='2020-01-01T00:00:00Z',
                             end_time='2020-08-01T00:00:00Z'):
        # TODO: wating for Twitter approval for Academic Research product track https://developer.twitter.com/en/products/twitter-api/academic-research
        '''
        return 100*(number of pages) tweets (10 pages by default)
        :param text_to_seearch:
        :param number_of_pages:
        :return:
        '''

        # Search Recent Tweets
        # This endpoint/method returns Tweets from the last seven days

        twitter_connection = self.get_connection_bearer_token()

        responses = tweepy.Paginator(twitter_connection.search_all_tweets,
                                     text_to_seearch,
                                     tweet_fields=['lang', 'created_at', 'public_metrics', 'entities'],
                                     user_fields=['profile_image_url'],
                                     media_fields=['url'],
                                     expansions=['author_id', 'attachments.media_keys'],
                                     start_time=start_time,
                                     end_time=end_time,
                                     max_results=100,
                                     limit=number_of_pages)

        # The method returns a Response object, a named tuple with data, includes,

        # In this case, the data field of the Response returned is a list of Tweet
        # objects

        responses_dict = dict()
        twitter_whole_response_df = pd.DataFrame()

        index = 0
        for response in tqdm(responses, total=number_of_pages, colour='blue', desc="ETL is extracting tweets"):
            twitter_response_df = self.get_response_info(response)
            twitter_whole_response_df = pd.concat([twitter_whole_response_df, twitter_response_df])

            responses_dict[index] = response
            index += 1

        return responses_dict, twitter_whole_response_df.reset_index().drop(columns='index')

import tweepy
import pandas as pd


class Twitter:

    def __init__(self, bearer_token):
        self.bearer_token = bearer_token

    def get_connection(self):
        '''
        this function is the one that allows to get connection to API twitter based on bearer token
        documentation: https://docs.tweepy.org/en/stable/client.html
        :return: the client that allows to create delete, get, post and put queries
        '''

        bearer_token = self.bearer_token
        # bearer_token = 'AAAAAAAAAAAAAAAAAAAAAHAhdQEAAAAAqIbsC3QZW5jWqDu8%2FF2g%2BhTStug%3Dq4S5oh53c0j6dlYJRpsVwsKdHe6xuqDIECKtwHonL9g8zAshi0'

        client = tweepy.Client(bearer_token=bearer_token)

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

        no_tweets = len(response.data)

        column_names = ["account_id",
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

        twitter_response_df = pd.DataFrame(columns=column_names)

        # Each Tweet object has default ID and text fields
        for index in range(no_tweets):
            account_username = response.includes["users"][0].username
            account_name = response.includes["users"][0].name
            account_id = response.includes["users"][0].id
            profile_image_url = response.includes["users"][0].profile_image_url
            tweet_id = response.data[0].id
            tweet_text = response.data[0].text
            tweet_created_at = str(response.data[0].created_at)
            tweet_language = response.data[0].lang
            account_id_check = response.data[0].author_id
            retweet_count = response.data[0].public_metrics['retweet_count']
            reply_count = response.data[0].public_metrics['reply_count']
            like_count = response.data[0].public_metrics['like_count']
            quote_count = response.data[0].public_metrics['quote_count']

            row = [account_id,
                   account_id_check,
                   tweet_id,
                   account_username,
                   account_name,
                   tweet_text,
                   tweet_created_at,
                   tweet_language,
                   retweet_count,
                   reply_count,
                   like_count,
                   quote_count,
                   profile_image_url]

            twitter_response_df_length = len(twitter_response_df)
            twitter_response_df.loc[twitter_response_df_length] = row

        return twitter_response_df

    def search_recent_tweet_100(self, text_to_seearch):
        '''

        just return 100 tweets

        documentation: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent

        :param text_to_seearch:
        :return:
        '''
        # Search Recent Tweets
        # This endpoint/method returns Tweets from the last seven days

        twitter_connection = self.get_connection()

        response = twitter_connection.search_recent_tweets(
            text_to_seearch,
            tweet_fields=['lang', 'created_at', 'public_metrics', 'entities'],
            user_fields=['profile_image_url'],
            media_fields=['url'],
            expansions=['author_id', 'attachments.media_keys'],
            max_results=100)
        # The method returns a Response object, a named tuple with data, includes,

        # In this case, the data field of the Response returned is a list of Tweet
        # objects

        twitter_response_df = self.get_response_info(response)

        return response, twitter_response_df

    def search_recent_tweet(self, text_to_seearch, number_of_pages=10):
        '''
        return 100*(number of pages) tweets (10 pages by default)
        :param text_to_seearch:
        :param number_of_pages:
        :return:
        '''

        # Search Recent Tweets
        # This endpoint/method returns Tweets from the last seven days

        twitter_connection = self.get_connection()

        responses = tweepy.Paginator(twitter_connection.search_recent_tweets,
                                     text_to_seearch,
                                     tweet_fields=['lang', 'created_at', 'public_metrics', 'entities'],
                                     user_fields=['profile_image_url'],
                                     media_fields=['url'],
                                     expansions=['author_id', 'attachments.media_keys'],
                                     max_results=100,
                                     limit=number_of_pages)

        # The method returns a Response object, a named tuple with data, includes,

        # In this case, the data field of the Response returned is a list of Tweet
        # objects

        responses_dict = dict()
        twitter_whole_response_df = pd.DataFrame()

        index = 0
        for response in responses:
            print(index)
            twitter_response_df = self.get_response_info(response)
            twitter_whole_response_df = pd.concat([twitter_whole_response_df, twitter_response_df])

            responses_dict[index] = response
            index += 1

        return responses_dict, twitter_whole_response_df

    def search_all_tweet(self, text_to_seearch):
        '''

        documentation: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-all

        :param text_to_seearch:
        :return:
        '''
        # Search Recent Tweets
        # This endpoint/method returns Tweets from the last seven days

        twitter_connection = self.get_connection()

        response = twitter_connection.search_all_tweets(
            text_to_seearch,
            tweet_fields=['lang', 'created_at', 'public_metrics', 'entities'],
            user_fields=['profile_image_url'],
            media_fields=['url'],
            expansions=['author_id', 'attachments.media_keys'],
            max_results=100)
        # The method returns a Response object, a named tuple with data, includes,

        # In this case, the data field of the Response returned is a list of Tweet
        # objects
        no_tweets = len(response.data)

        column_names = ["account_id",
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

        twitter_response_df = pd.DataFrame(columns=column_names)

        # Each Tweet object has default ID and text fields
        for index in range(no_tweets):
            account_username = response.includes["users"][0].username
            account_name = response.includes["users"][0].name
            account_id = response.includes["users"][0].id
            profile_image_url = response.includes["users"][0].profile_image_url
            tweet_id = response.data[0].id
            tweet_text = response.data[0].text
            tweet_created_at = str(response.data[0].created_at)
            tweet_language = response.data[0].lang
            account_id_check = response.data[0].author_id
            retweet_count = response.data[0].public_metrics['retweet_count']
            reply_count = response.data[0].public_metrics['reply_count']
            like_count = response.data[0].public_metrics['like_count']
            quote_count = response.data[0].public_metrics['quote_count']

            row = [account_id,
                   account_id_check,
                   tweet_id,
                   account_username,
                   account_name,
                   tweet_text,
                   tweet_created_at,
                   tweet_language,
                   retweet_count,
                   reply_count,
                   like_count,
                   quote_count,
                   profile_image_url]

            twitter_response_df_length = len(twitter_response_df)
            twitter_response_df.loc[twitter_response_df_length] = row

        return response, twitter_response_df

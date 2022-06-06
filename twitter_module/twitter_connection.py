import tweepy


class Twitter:

    def __init__(self, bearer_token):
        self.bearer_token = bearer_token

    def get_connection(self):

        bearer_token = self.bearer_token
        # bearer_token = 'AAAAAAAAAAAAAAAAAAAAAHAhdQEAAAAAqIbsC3QZW5jWqDu8%2FF2g%2BhTStug%3Dq4S5oh53c0j6dlYJRpsVwsKdHe6xuqDIECKtwHonL9g8zAshi0'

        client = tweepy.Client(bearer_token=bearer_token)

        return client

    def search_tweet(self, text_to_seearch):

        # Search Recent Tweets
        # This endpoint/method returns Tweets from the last seven days

        twitter_connection = self.get_connection()

        response = twitter_connection.search_recent_tweets(text_to_seearch)
        # The method returns a Response object, a named tuple with data, includes,


        # In this case, the data field of the Response returned is a list of Tweet
        # objects
        tweets = response.data

        response_dict ={}
        # Each Tweet object has default ID and text fields
        for tweet in tweets:
            response_dict[tweet.id] = tweet.text

        return response_dict

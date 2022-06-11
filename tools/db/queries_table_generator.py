

class RawTables:

    def __init__(self):

        self.create_tweets_raw = '''
            CREATE TABLE IF NOT EXISTS twitter_raw.tweets_raw (
                account_id                  int
                , account_id_check          int
                , tweet_id                  int
                , account_username          text
                , account_name              text
                , tweet_text                text
                , tweet_created_at          timestamp
                , tweet_language            text
                , retweet_count             int
                , reply_count               int
                , like_count                int
                , quote_count               int
                , profile_image_url         text
                , is_reclaimable            boolean
                , date_inserted             timestamp
            ) engine=innodb;
        '''


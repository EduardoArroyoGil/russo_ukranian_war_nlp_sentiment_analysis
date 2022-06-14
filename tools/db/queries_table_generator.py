

class RawTables:

    def __init__(self):

        self.create_tweets_raw = '''
            CREATE TABLE IF NOT EXISTS twitter_raw.tweets_raw (
                account_id                  bigint
                , account_id_check          bigint
                , tweet_id                  bigint not null primary key
                , account_username          text
                , account_name              text
                , tweet_text                text
                , tweet_created_at          timestamp
                , tweet_language            text
                , retweet_count             bigint
                , reply_count               bigint
                , like_count                bigint
                , quote_count               bigint
                , profile_image_url         text
                , is_reclaimable            boolean
                , date_inserted             timestamp
            ) engine=innodb;
        '''

        self.create_tweets_transformed = '''
                    CREATE TABLE IF NOT EXISTS twitter_transformed.tweets_emotional (
                        account_id                      bigint
                        , account_id_check              bigint
                        , tweet_id                      bigint not null primary key
                        , account_username              text
                        , account_name                  text
                        , tweet_text                    text
                        , tweet_created_at              timestamp
                        , tweet_language                text
                        , retweet_count                 bigint
                        , reply_count                   bigint
                        , like_count                    bigint
                        , quote_count                   bigint
                        , profile_image_url             text
                        , is_reclaimable                boolean
                        , tweet_text_translated_gpt3    text
                        , tweet_emotion_gpt3            text
                        , date_inserted                 timestamp
                    ) engine=innodb;
                '''

        self.create_view_twitter_accounts = '''
                    CREATE OR REPLACE VIEW twitter_raw.v_twitter_accounts_raw AS
                        SELECT DISTINCT
                            account_id,
                            account_id_check,
                            account_username,
                            account_name,
                            is_reclaimable
                        FROM
                            twitter_raw.tweets_raw
                        order by 1,2,3,4;
                '''

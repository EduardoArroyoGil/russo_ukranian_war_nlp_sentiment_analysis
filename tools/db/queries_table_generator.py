

class RawObjects:

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

        self.create_v_twitter_accounts_raw = '''
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

        self.create_v_twitter_accounts_metrics_raw = '''
                    CREATE OR REPLACE VIEW twitter_raw.v_twitter_accounts_metrics_raw AS
                        SELECT 
                            account_id,
                            account_username,
                            account_name,
                            count(tweet_id)     as tweets_count,
                            sum(retweet_count)  as retweet_count,
                            sum(reply_count)    as reply_count,
                            sum(like_count)     as like_count,
                            sum(quote_count)    as quote_count,
                            is_reclaimable
                        FROM
                            twitter_raw.tweets_raw
                        GROUP BY account_id, account_username, account_name, is_reclaimable
                        ORDER BY tweets_count DESC, retweet_count DESC, 
                        reply_count DESC, like_count DESC, quote_count DESC;
                '''

        self.create_v_tweets_priority_raw = '''
                    CREATE OR REPLACE VIEW twitter_raw.v_tweets_priority_raw AS
                    select tr.*,
                           political_party,
                           case
                               when political_party is not null then 1
                               when retweet_count>12000 then 2
                               when retweet_count>11300 then 3
                               when retweet_count>11230 then 4
                               when retweet_count>5000 then 5
                               when retweet_count>2000 then 6
                               else 7
                            end priority
                    from tweets_raw tr
                    left join m_political_accounts mpa on tr.account_username = mpa.account_username
                    order by priority asc
                '''


class TransformedObjects:

    def __init__(self):

        self.create_tweets_emotional = '''
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
                        , political_party               text
                        , priority                      int 
                        , tweet_text_translated_gpt3    text
                        , tweet_emotion_gpt3            text
                        , date_inserted                 timestamp
                    ) engine=innodb;
                '''
        self.create_v_tweets_emotional_model = '''
                    CREATE OR REPLACE VIEW twitter_transformed.v_tweets_emotional_model AS
                    select
                        vtpr.*,
                        te.tweet_text_translated_gpt3,
                        te.tweet_emotion_gpt3
                    from twitter_raw.v_tweets_priority_raw vtpr
                    left join twitter_transformed.tweets_emotional te on vtpr.tweet_id = te.tweet_id
                    order by priority asc
                '''

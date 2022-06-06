import openai_module.openai_connection as openai_connection
import twitter_module.twitter_connection as twitter_connection

twitter_conn = twitter_connection.Twitter(bearer_token='AAAAAAAAAAAAAAAAAAAAAHAhdQEAAAAAqIbsC3QZW5jWqDu8%2FF2g%2BhTStug%3Dq4S5oh53c0j6dlYJRpsVwsKdHe6xuqDIECKtwHonL9g8zAshi0')
gpt3_conn = openai_connection.GPT3(api_key='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')

#  SENTIMENTAL ANALYSIS FOR EACH TWEET
twitter_response = twitter_conn.search_tweet(text_to_seearch='Guerra de Ucrania')

tweets_id = list(twitter_response.keys())
tweets = list(twitter_response.values())

emo_analysis = list()
tweets_translated = list()

for tweet in tweets:

    query = f'Cual es la emocion que transmite el siguiente twitt: {tweet}'
    gpt3_response = gpt3_conn.query(prompt=query)
    emo_analysis.append(gpt3_response)


print(emo_analysis)
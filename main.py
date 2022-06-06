# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import openai
import tweepy

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def gpt3(stext):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=stext,
        temperature=0.1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    content = response.choices[0].text.split('.')

    return response.choices[0].text


def twitter():

    # consumer_key='lpbQmdFZgr4e49fIIW1EYTUE4'
    # consumer_secret='jJhzEblWvhaNwUaBtBmBlHaLZ557ACI1fcEdq78ZzvyfEu0Jq3'
    # access_token='AAAAAAAAAAAAAAAAAAAAAHAhdQEAAAAAe0j8Bthvm6akXjT2yA4jPFwbEd8%3Doz50Ff81QAXLXZ9NDMu6EAvBJVGPDYYDRt9yRwin8hyEHs7I3w'
    # access_token_secret=''

    api_key='lpbQmdFZgr4e49fIIW1EYTUE4'
    api_key_secret='jJhzEblWvhaNwUaBtBmBlHaLZ557ACI1fcEdq78ZzvyfEu0Jq3'

    bearer_token='AAAAAAAAAAAAAAAAAAAAAHAhdQEAAAAAqIbsC3QZW5jWqDu8%2FF2g%2BhTStug%3Dq4S5oh53c0j6dlYJRpsVwsKdHe6xuqDIECKtwHonL9g8zAshi0'

    # auth = tweepy.OAuth1UserHandler(
    #     consumer_key, consumer_secret, access_token, access_token_secret
    # )
    #
    # api = tweepy.API(auth)

    client = tweepy.Client(bearer_token=bearer_token)

    return client


def search_tweet(text):

    # Search Recent Tweets
    # This endpoint/method returns Tweets from the last seven days

    bearer_token='AAAAAAAAAAAAAAAAAAAAAHAhdQEAAAAAqIbsC3QZW5jWqDu8%2FF2g%2BhTStug%3Dq4S5oh53c0j6dlYJRpsVwsKdHe6xuqDIECKtwHonL9g8zAshi0'

    response = tweepy.Client(bearer_token=bearer_token).search_recent_tweets(text)
    # The method returns a Response object, a named tuple with data, includes,
    # errors, and meta fields
    # print(response.meta)

    # In this case, the data field of the Response returned is a list of Tweet
    # objects
    tweets = response.data

    response_dict ={}
    # Each Tweet object has default ID and text fields
    for tweet in tweets:
        response_dict[tweet.id] = tweet.text

    return response_dict

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    import etls_main as etls_main

    etls_main

    # respond = search_tweet('Pablo Iglesias Podemos')
    # tweets = list(respond.values())
    # emo_analysis = list()
    #
    # for tweet in tweets:
    #     query = f'Cual es la emocion que transmite el siguiente twitt: {tweet}'
    #
    #     response = gpt3(query)
    #
    #     print(response)
    #
    #     emo_analysis.append(response)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

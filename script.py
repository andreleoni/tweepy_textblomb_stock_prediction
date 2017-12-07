from textblob import TextBlob
import tweepy
import csv

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('Yahoo', "en")


with open('yahoo_tweets.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = ["source", "text"], delimiter = ';')
    writer.writeheader()

    for tweet in public_tweets:
      values = {'source':'Twitter', 'text':tweet.text}
      writer.writerow(values)

# for tweet in public_tweets:
#   analysis = TextBlob(tweet.text)
#   print(analysis.sentiment)
#   print("")

import os
import csv
import tweepy as tw
import pandas as pd

consumer_key='doe69bTLu927Xx3KqEXZhWvxv'
consumer_secret='OtU8raMzrLlqdonlvu3gTT4cWWBtbaGYyhsRblouy9q4hVTyVV'
access_token='701466385-ZcFqPfaP6pxE0bOsrbWAFNGBUFHvFrEm96n6jSKQ'
access_token_secret='Vuz7qm8rN7u62oQlfSWGbqNc6GwVmQRyfW5lgwxc4iMDo'

auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tw.API(auth,wait_on_rate_limit=True)


#api.update_status("Look, I'm tweeting from Python in my earthanalytics class! @EarthLabCU")
search_words = "#tourism"
date_since="2000-11-01"
tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since).items()

csvFile = open('hotel_review.csv', 'a')
csvWriter = csv.writer(csvFile)

for tweet in tweets:
    print(tweet.text)

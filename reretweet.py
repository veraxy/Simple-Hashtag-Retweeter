import tweepy
from time import sleep
from creds import *
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
def retweet():
    for tweet in tweepy.Cursor(api.search,q='#NetNeutrality').items():
        try:
            print('\nTweet by: @' + tweet.user.screen_name)
 
            tweet.retweet()
            print('Retweeted the tweet')
   
       
            tweet.favorite()
            print('Favorited the tweet')
 
           
            tweet.user.follow()
            print('Followed the user')
 
            sleep(700)
 
        except tweepy.TweepError as e:
            print(e.reason)
 
        except StopIteration:
            break
        if not tweet.user.following:
            tweet.user.follow()
            print('Followed the user')
 
retweet()

import twitter
import sys

if __name__ == "__main__":
    token = twitter.authenticate()
    search = sys.argv[1]
    
    tweets = twitter.get_tweets(search, token)
    for tweet in tweets.get('statuses'):
        print('{} : {}'.format(tweet.get('id'), tweet.get('text')))
        print('Hashtags : {}'.format(", ".join([tag['text'] for tag in tweet.get('entities').get('hashtags')])))

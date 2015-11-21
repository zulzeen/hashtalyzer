import twitter
import sys
from collections import Counter

def collect_hashtags(tweets):
    """ Retieve the hashtags of a list of tweets """

    hashtags = Counter()
    for tweet in tweets:
        hashtags.update([hashtag['text'] for hashtag in tweet.get('entities').get('hashtags')])

    return hashtags

if __name__ == "__main__":
    token = twitter.authenticate()
    search = sys.argv[1]
    count = int(sys.argv[2]) or 15
    
    search = twitter.get_tweets(search, token, count)
    tweets = search.get('statuses')
    for tweet in tweets:
        print('{} : {}'.format(tweet.get('id'), tweet.get('text')))
        print('Hashtags : {}'.format(", ".join([tag['text'] for tag in tweet.get('entities').get('hashtags')])))

    print(collect_hashtags(tweets))

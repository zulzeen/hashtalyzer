import base64
import requests
import urllib

from settings import *

def authenticate():
    str_token = ":".join([TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET])
    b64_token = base64.b64encode(bytes(str_token, 'ascii'))
    headers = {'Authorization': 'Basic {}'.format(b64_token.decode('ascii')), 
               'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
    data = "grant_type=client_credentials"
    url = "https://api.twitter.com/oauth2/token"
    auth_req = requests.post(url, data, headers = headers)
    if auth_req.status_code == 200:
        return auth_req.json()['access_token']
    else:
        return None

def get_tweets(hashtag, token, count=15, max_id='0'):
    tweets_list = []
    url = "https://api.twitter.com/1.1/search/tweets.json"
    query = hashtag
    headers = {'Authorization' : 'Bearer {}'.format(token),
               'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}

    count = count >= 1 and int(count) or 100
    payload = {'q': query, 'count': count}
    if max_id != '0':
        payload.update({'max_id': max_id})

    request = requests.get(url, params=payload, headers=headers).json()
    next = request.get('search_metadata').get('next_results')
    if next:
        max_id = urllib.parse.parse_qs(next).get('?max_id').pop()
    tweets_list += request.get('statuses')
    if max_id == '0' or count <= 100:
        return tweets_list
    else :
        count -= 100
        tweets_list += get_tweets(hashtag, token, count=count, max_id=max_id)
        return tweets_list

if __name__ == "__main__":
    pass

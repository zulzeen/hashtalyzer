import base64
import requests

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

def get_tweets(hashtag, token, count=15):
    url = "https://api.twitter.com/1.1/search/tweets.json"
    query = hashtag
    count = 1 < count < 100 and int(count) or 100
    payload = {'q': query, 'count': count}
    headers = {'Authorization' : 'Bearer {}'.format(token),
               'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
    request = requests.get(url, params=payload, headers=headers)
    return request.json()

if __name__ == "__main__":
    pass

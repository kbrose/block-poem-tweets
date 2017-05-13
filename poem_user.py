import sys
import random

import poem_tweets
import tweepy


def generate(handle, n=1):
    with open('auth.txt') as f:
        _ck = f.readline().strip()
        _cs = f.readline().strip()
        _ak = f.readline().strip()
        _as = f.readline().strip()

    auth = tweepy.OAuthHandler(_ck, _cs)
    auth.set_access_token(_ak, _as)

    api = tweepy.API(auth)

    user = api.get_user(handle)
    timeline = [tweet.text for tweet in user.timeline()]

    for _ in range(n):
        tweet = random.choice(timeline)
        print(tweet)
        print('')
        print(poem_tweets.make_poem(tweet))
        print('\n\n')

if __name__ == '__main__':
    generate(sys.argv[1])

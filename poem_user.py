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

    ret = []

    for _ in range(n):
        tweet = random.choice(timeline)
        ret.append((tweet, poem_tweets.make_poem(tweet)))
    return ret

if __name__ == '__main__':
    out = generate(sys.argv[1])
    for tweet, poem in out:
        print(tweet)
        print('')
        print(poem)
        print('\n\n')

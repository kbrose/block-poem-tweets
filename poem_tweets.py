from __future__ import division
from __future__ import print_function

import sys
import random

NUM_TRIES = 2000

def extract(tweet, target_word, verbose=False):
    tweet = tweet.lower()
    target_i = 0
    tweet_idxs = []
    for tweet_i, c in enumerate(tweet):
        if c == target_word[target_i]:
            tweet_idxs.append(tweet_i)
            target_i += 1
            if target_i == len(target_word): # done!
                if verbose:
                    print(target_word)
                return tweet_idxs
    return None


def make_poem(tweet, verbose=False):
    og_tweet = list(tweet)

    with open('words.txt') as f:
        wordlist = f.read().lower().split()

    wordlist = [word for word in wordlist if len(word) > 2 or word in ['i', 'a']]

    curr_pos = 0

    for _ in range(NUM_TRIES):
        tweet_idxs = extract(tweet[:40], random.choice(wordlist) + ' ', verbose)
        if tweet_idxs:
            break

    if not tweet_idxs:
        print("no insight to be gained.")
        return

    n = 1
    tweet = tweet[max(tweet_idxs):]
    while n < 5 and len(tweet) > 5:
        for _ in range(NUM_TRIES):
            tweet_idxs_curr = extract(tweet[:40],
                                      random.choice(wordlist) + (' ' if n < 4 else ''),
                                      verbose)
            if tweet_idxs_curr:
                break
        if not tweet_idxs_curr:
            break
        tweet_idxs += [i+max(tweet_idxs) for i in tweet_idxs_curr]
        tweet = tweet[max(tweet_idxs_curr):]
        n += 1

    for i in range(len(og_tweet)):
        if i in tweet_idxs:
            continue
        else:
            og_tweet[i] = '*'

    return ''.join(og_tweet)

if __name__ == '__main__':
    tweet = sys.argv[1]
    print(main(tweet))

import os
import json

cwd = os.path.dirname(__file__)
key_file = f'{cwd}/keys.json'


def get_twitter_tokens():
    with open(key_file, 'r') as j:
        key = json.load(j)
        keys = {
            'apiKey': key['twitter']['apiKey'],
            'apiSecret': key['twitter']['apiSecret'],
            'token': key['twitter']['token'],
            'tokenSecret': key['twitter']['tokenSecret'],
            'bearer': key['twitter']['bearer'],
        }
        return keys


def tweet(args):
    print(args)


def reply(args):
    print(args)


def favorite(args):
    print(args)

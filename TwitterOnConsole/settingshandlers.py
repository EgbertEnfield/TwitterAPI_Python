import os
import sys
import json
import argparse
import twitterhandlers

cwd = os.path.dirname(__file__)
settings_file = f'{cwd}/settings.json'
VERSION = "1.0.0.1"


def get_settings():
    d1 = load_settings()
    d2 = parse_args()
    return {**d1, **d2}


def load_settings():
    try:
        with open(settings_file, 'r') as reader:
            j_dic = json.load(reader)
    except FileNotFoundError:
        print(f'settings.json not found in {cwd}')
    finally:
        j_dic.setdefault('main', {})
        j_dic['main'].setdefault('verbose', True)
        j_dic['main'].setdefault('debug', False)

        j_dic.setdefault('log', {})
        j_dic['log'].setdefault('file', {})
        j_dic['log']['file'].setdefault('enable', True)
        j_dic['log']['file'].setdefault('level', 'info')
        j_dic['log']['file'].setdefault('directory', f'{cwd}/log')

        j_dic['log'].setdefault('stream', {})
        j_dic['log']['stream'].setdefault('enable', True)
        j_dic['log']['stream'].setdefault('level', 'info')

        return j_dic


def parse_args(arguments=sys.argv, logger=None):
    arg_values = {
        'args': {
            'text': '',
            'pictures': [],
            'debug': False,
            'verbose': False,
            'mode': 'bot'
        }
    }

    if (len(arguments) == 0):
        return {}
    elif (len(arguments) == 1):
        return arg_values

    parser = argparse.ArgumentParser(description='apitester')
    subparsers = parser.add_subparsers()

    # top-level arguments
    # switches
    parser.add_argument(
        '-d',
        '--debug',
        action='store_true',
        help='Test behave this program')
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Show log output in debug-level.')
    parser.add_argument(
        '--version',
        action='store_true',
        help='Show version of this application.')

    # Sub-commands
    p_tweet = subparsers.add_parser(
        'tweet',
        help='See \"tweet [-h|--help]\".')
    p_tweet.add_argument(
        'message',
        help='Messages to be tweeted.')
    p_tweet.add_argument(
        '-p', '--pictures',
        help='Path of the images to be tweeted. (Up to 4)')
    p_tweet.set_defaults(func=twitterhandlers.tweet)

    p_reply = subparsers.add_parser(
        'reply',
        help='See \"reply [-h|--help]\".')
    p_reply.add_argument(
        'message',
        help='Messages to be replied.')
    p_reply.add_argument(
        '-p', '--pictures',
        help='Path of the images to be replied. (Up to 4)')
    p_reply.set_defaults(func=twitterhandlers.reply)

    p_favorite = subparsers.add_parser(
        'favorite',
        help='See \"favprite\" [-h|--help].')
    p_favorite.add_argument(
        'tweetid',
        help='Id of the tweet which to be favorite.')
    p_favorite.add_argument(
        '-a', '--add',
        help='Add favorite to the tweet.')
    p_favorite.add_argument(
        '-d', '--del',
        help='Delete favorite from the tweet.')
    p_favorite.set_defaults(func=twitterhandlers.favorite)

    parsed = parser.parse_args()

    if parsed.func == twitterhandlers.tweet:
        twitterhandlers.tweet(vars(parsed))
    elif parsed.func == twitterhandlers.reply:
        twitterhandlers.reply(vars(parsed))
    elif parsed.func == twitterhandlers.favorite:
        twitterhandlers.favorite(vars(parsed))

    if (parsed.version):
        print(f'botcore.py version: {VERSION}')
        sys.exit()

    return arg_values

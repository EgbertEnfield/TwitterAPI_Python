import os
import tweepy
from enum import Enum

cwd = os.path.dirname(__file__)


class Modes(Enum):
    Tweet = 1,
    Reply = 3,
    Favorite = 7,


class Requires(Enum):
    Pictures = 1,
    Words = 3


class Switches(Enum):
    Add = 1,
    Del = 3


def setup_API_v11(
        api_key,
        api_secret,
        token,
        token_secret,
        logger=None):

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(token, token_secret)

    if logger is not None:
        logger.debug('API-v1.1 setup complete')

    return tweepy.API(auth)


def tweet(api, message, pictures, flags, logger):
    return


def reply(api, message, pictures, flags, logger):
    return


def favorite(api, id, flags, logger):
    return

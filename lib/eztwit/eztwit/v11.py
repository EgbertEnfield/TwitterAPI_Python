import os
import tweepy
from enum import Enum

cwd = os.path.dirname(__file__)


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


def _tweet(api, message, pictures, logger):
    return

import eztwit
import setuplogger
import settingshandlers
import twitterhandlers


def main():
    keys = twitterhandlers.get_twitter_tokens()
    api = eztwit.setup_API_v11(
        api_key=keys['apiKey'],
        api_secret=keys['apiSecret'],
        token=keys['token'],
        token_secret=keys['tokenSecret'],
        logger=setuplogger.create_logger()
    )
    foo = settingshandlers.get_settings()
    return api


if __name__ == '__main__':
    main()

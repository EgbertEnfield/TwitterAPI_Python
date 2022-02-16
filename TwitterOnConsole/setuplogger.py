import os
import glob
import logging
import settingshandlers
import datetime
from logging import handlers


def create_logger():
    level_file = logging.INFO
    level_stream = logging.INFO
    settings = settingshandlers.load_settings()

    log_dir = settings['log']['file']['directory']
    is_enable_file = settings['log']['file']['enable']
    is_enable_stream = settings['log']['stream']['enable']

    level_file_str = settings['log']['file']['level']
    level_stream_str = settings['log']['stream']['level']
    level_file = _get_log_level(level_file_str)
    level_stream = _get_log_level(level_stream_str)

    if not (os.path.exists(log_dir)):
        os.mkdir(log_dir)

    for log in glob.glob(log_dir + '/*.log'):
        if (log.endswith('.log')):
            log_file = log
            break
    else:
        # create new empty log file
        log_file = f'{log_dir}/{datetime.datetime.now().strftime("%y%m%d%H%M%S")}.log'
        with open(log_file, 'w') as f:
            f.write('')

    format = logging.Formatter(
        '{asctime} [{levelname}]  {message}',
        style='{',
        datefmt='%y/%m/%d %H:%M:%S'
    )

    if (is_enable_file):
        file_handler = handlers.TimedRotatingFileHandler(
            filename=log_file,
            encoding='UTF-8',
            when='MIDNIGHT',
            backupCount=7
        )
        file_handler.setFormatter(format)
        file_handler.setLevel(level_file)

    if (is_enable_stream):
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(format)
        stream_handler.setLevel(level_stream)

    internal_logger = logging.getLogger()
    internal_logger.setLevel(logging.NOTSET)
    if (is_enable_file):
        internal_logger.addHandler(file_handler)
    if (is_enable_stream):
        internal_logger.addHandler(stream_handler)

    internal_logger.info(
        f'file_handler log level is {level_file_str}')
    internal_logger.info(
        f'stream_handler log level is {level_stream_str}')
    internal_logger.info(
        f'log file path is {log_file}')

    return internal_logger


def _get_log_level(level: str):
    if (level == 'critical'):
        return logging.CRITICAL
    elif (level == 'error'):
        return logging.ERROR
    elif (level == 'info'):
        return logging.INFO
    elif (level == 'debug'):
        return logging.DEBUG
    elif (level == 'notset'):
        return logging.NOTSET
    else:
        return logging.INFO

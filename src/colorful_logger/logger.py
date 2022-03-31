import logging

# https://pod.hatenablog.com/entry/2020/03/01/221715


class ColorfulHander(logging.StreamHandler):
    default_head = {
        'TRACE': 'TRACE',
        'DEBUG': '\x1b[0;36mDEBUG\x1b[0m',
        'INFO': '\x1b[0;32mINFO\x1b[0m',
        'WARN': '\x1b[0;33mWARN\x1b[0m',
        'WARNING': '\x1b[0;33mWARN\x1b[0m',
        'ERROR': '\x1b[0;31mERROR\x1b[0m',
        'ALERT': '\x1b[0;37;41mALERT\x1b[0m',
        'CRITICAL': '\x1b[0;37;41mALERT\x1b[0m',
    }

    def emit(self, record: logging.LogRecord) -> None:
        record.levelname = self.default_head[record.levelname]
        super().emit(record)


def get_colorful_logger(
        name: str = __name__,
        level=logging.DEBUG,
        handler: logging.Handler = ColorfulHander(),
        formatter: logging.Formatter = logging.Formatter(
            '%(levelname)s\t%(asctime)s  %(message)s', '%Y-%m-%d %H:%M:%S'
        )) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler.setFormatter(formatter)
    handler.setLevel(level)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.propagate = False
    return logger


if __name__ == '__main__':
    logger = get_colorful_logger()
    logger.debug('hello debug')
    logger.info('hello info')
    logger.warning('hello warning')
    logger.error('hello error')
    logger.critical('hello critical')

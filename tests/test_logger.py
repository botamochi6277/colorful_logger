from asyncio.log import logger
import colorful_logger

def test_print():
    logger = colorful_logger.get_colorful_logger()
    logger.debug('debugging')
    logger.info('infomation')
    logger.warning('warning!')
    logger.critical('critical hit!')
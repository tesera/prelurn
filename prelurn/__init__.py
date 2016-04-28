# prelurn

import logging
import os

LOG_FILENAME = __name__ + '.log'
LOG_PATH = os.path.join(os.getcwd(), LOG_FILENAME)
LOG_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'


logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt='%y-%m-%d %H:%M:%S',
                    filename=LOG_PATH,
                    filemode='w')

log = logging.getLogger(__name__)


def has_legs():
    log.debug('In has_legs()')
    return False

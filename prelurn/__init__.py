"""Prelurn Package

   Machine learning data preprocessing utilities built on pandas.

"""

# Libs
import logging
import os

# package modules modules
from .core import describe, suggest


log_filename = __name__ + '.log'
log_path = os.path.join(os.getcwd(), log_filename)
log_format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.DEBUG,
                    format=log_format,
                    datefmt='%y-%m-%d %H:%M:%S',
                    filename=log_path,
                    filemode='w')
log = logging.getLogger(__name__)


def has_legs():
    log.debug('In has_legs()')
    return False


__all__ = ['suggest', 'describe']

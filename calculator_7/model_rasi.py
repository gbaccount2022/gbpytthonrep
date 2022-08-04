import logger as log
import re


def calculate(val):

    # check for string
    info = re.findall("[^0-9^\+^\-^\*^\/^\(^\)]+", val)

    if len(info) > 0:
        log.write(f'Bad input string, not match formula {info}')
        raise 'Bad input string'

    log.write(f'Calculate simple: {val}')

    return round(eval(val),2)
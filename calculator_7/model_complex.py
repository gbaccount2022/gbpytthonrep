import logger as log
import re

def calculate(val):

    # check for string
    info = re.findall("[^0-9^\+^\-^\(^\)^j]+", val)

    if len(info) > 0:
        log.write(f'Bad input string, not match formula {info}')
        raise 'Bad input string'

    log.write(f'Calculate complex: {val}')
    
    return eval(val)
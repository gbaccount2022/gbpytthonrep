import logger as log



# get value from the input
def get_value(txt=''):

    if (len(txt)):
        log.write(f'Input line is pre defined: {txt}')
        return txt

    log.write(f'Input line is: {txt}')
    return input(txt)



# set value to the view
def set_value(txt):
    log.write(f'Set value: {txt}')
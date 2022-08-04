
import view as v
import model_complex as complex
import model_rasi as rasi
import logger as log


def getResult(which, data):
    if (which == 1):
        return rasi.calculate(data)
    if (which == 2):
        return complex.calculate(data)

    raise 'Unknown mode'



def button_click():

    result = 'unknown result'

    while 1:
        print('[MENU]')
        print('  1. Simple calculator')
        print('  2. Complex calculator')
        print('  3. Quit')

        option = int(input())
        log.write(f'Option selected {option}')
        if (option < 1 or option > 3):
            log.write(f'Bad option {option}')
            continue

        if (option == 3):
            exit(0)


        log.write(f'Taking value from user')
        data = v.get_value()

        log.write(f'Value from user taken {data}')
        
        result = getResult(option, data)

        log.write(f'Result taken {result}')

        break

    return result
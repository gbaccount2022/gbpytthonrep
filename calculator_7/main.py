
#calc('2*2+8/4')
#calc('2*(((2+8)))/4')

#calc('2+2')
#calc('1+2*3')
#calc('1-2*3')
#calc('(1+2)*3')

#calc('2*(((2+8)/(6-4)-3)*(5+1))')
#calc('2*(5+100/((20-14*(10-9))*2))')

# (1+3j)+(3-1j)

import controller as control
import logger as log


log.init('logs.txt')

control.button_click()

log.deinit()
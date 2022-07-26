
import re

operations = {
    '+': lambda a,b: a+b,
    '-': lambda a,b: a-b,
    '*': lambda a,b: a*b,
    '/': lambda a,b: a/b,
}

def singleOperation(operation, a, b):
    return round(operations[operation](a, b),2)

def needUnwind(item):
    return len(re.split('\*|\/|\+|\-', item)) > 1

def unwindLine(line = "0"):

    a = b = ''

    #print(line)

    if line.find('(') != -1:
        st = line.rfind('(')
        en = line[st:].find(')')
        item = line[st+1:st+en]
        item = unwindLine(item)
        line = unwindLine(line[:st] + item + line[st+en+1:])

    for index, op in enumerate('-+*/'):

        if line.find(op) != -1:
            [a,b] = line.split(op, 1)

            if needUnwind(a):
                a = unwindLine(a)

            if needUnwind(b):
                b = unwindLine(b)

            return str(singleOperation(op, float(a), float(b)))

    return line

def calc(line):
    print(f'{line} => {unwindLine(line)}')

calc('2*2+8/4')
calc('2*(((2+8)))/4')

calc('2+2')
calc('1+2*3')
calc('1-2*3')
calc('(1+2)*3')

calc('2*(((2+8)/(6-4)-3)*(5+1))')
calc('2*(5+100/((20-14*(10-9))*2))')
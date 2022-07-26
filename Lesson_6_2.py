
import re

operations = {
    '+': lambda a,b: a+b,
    '-': lambda a,b: a-b,
    '*': lambda a,b: a*b,
    '/': lambda a,b: a/b,
}

def singleOperation(operation, a, b):
    return operations[operation](a, b)

def needUnwind(item):
    return len(re.split('\*|\/|\+|\-', item)) > 1

def unwindLine(line):

    a = b = ''

    for index, op in enumerate('-+*/'):

        if line.find(op) != -1:
            [a,b] = line.split(op, 1)

            if needUnwind(a):
                a = unwindLine(a)

            if needUnwind(b):
                b = unwindLine(b)

            return singleOperation(op, float(a), float(b))

    return float(line)

def calc(line):
    return round(unwindLine(line), 2)

print(calc('2*2+4/2'))
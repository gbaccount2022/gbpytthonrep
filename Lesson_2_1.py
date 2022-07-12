
def dosum(i):

    sum = 0
    i = int(i.replace('.', '').replace(',',''))

    while i > 0:
        sum += i % 10
        i = int(i/10)

    return sum


def doCalcsAndOutput(val):
    sum = dosum(val)
    print(f'- {val} -> {sum}')


doCalcsAndOutput("6782")
doCalcsAndOutput("0.56")

doCalcsAndOutput(input("Enter value (float,int):"))

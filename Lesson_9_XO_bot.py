
import random

# field
# . . .
# . . . 
# . . .

maxX = 3 # max X size of field
maxY = 3 # max Y size of field

owner = 'X' # who do move first

movesCount = 0 # current valid moves
maxMovesCount = maxX * maxY # maximum moves count on the field


# fill field with default values
field = [['.' for i in range(maxX)] for j in range(maxY)]


##################################################
# print battlefield
def showField():
    print(' -------------')
    for index,item in enumerate(field):
        print(item)
    print(' -------------')


##################################################
# set X or O on specify coordinates of battlefield
def setItem(owner,y,x):

    global movesCount

    if not (x >= 1 and x <= maxX and y >= 1 and y <= maxY):
        print(f'Bad position, min X=1, max X={maxX}, min Y=1, max Y={maxY}, you set X={x}, Y={y}')
        return False

    x -= 1
    y -= 1

    # we already used this field?
    if field[y][x] == owner:
        print('This position is already used by you')
        return False

    # check for default field
    if field[y][x] != '.':
        print('This position is already used by other player')
        return False


    # calculate moves count
    movesCount += 1

    # set move onto the field
    field[y][x] = owner

    return True



##################################################
# Wait coordinates from user
# recursion :-/
def doMove(owner, y=-1, x=-1):

    if y == -1 and x == -1:
        [y,x] = list(map(int, input(f'Enter coordinates Y X (example: 1 1) now is > {owner} < move:').split()))

    return setItem(owner,y,x)
    

def searchVertical(startX):
    first = field[0][startX]
    if first == '.':
        return 0

    for y in range(maxY):
        if field[y][startX] != first:
            return 0

    return first

def searchHorizontal(startY):
    first = field[startY][0]
    if first == '.':
        return 0
        
    for x in range(maxX):
        if field[startY][x] != first:
            return 0
            
    return first

# 1 2 3
# 4 5 6
# 7 8 9
# 1 2 3 4 5 6 7 8 9

def searchDiaglonalLeftRight(str):
    first = str[0]
    if first == '.':
        return False

    result = True
    for i in range(0, len(str), 4):
        if str[i] != first:
            result = 0
            break

    if result:
        return result

    return 0

def searchDiagonalRightLeft(str):
    first = str[maxX-1]

    if first == '.':
        return False

    result = True
    for i in range(maxX-1, len(str)-1, maxX-1):
        if str[i] != first:
            result = 0
            break

    if result:
        return result

    return 0

#
def searchDiagonal():
    str = "".join(list(("".join(i) for i in field)))
    return searchDiaglonalLeftRight(str) or searchDiagonalRightLeft(str)

# x x x x
# x x x x
# x x x x
# x x x x
###################################################
def checkWinLoose():
    #

    for x in range(maxX):
        if searchVertical(x):
            return True

    for y in range(maxY):
        if searchHorizontal(y):
            return True

    return searchDiagonal()


def debug(owner, moves):
    for i, coordinates in enumerate(moves):
        doMove(owner, coordinates[0], coordinates[1])
    showField()
    if checkWinLoose():
        print('[DEBUG] Success we have winner')

#debug('#', [[1,1],[2,2],[3,3]])
#debug('O', [[3,1],[2,2],[1,2]])

def do_bot_move(owner):

    return setItem(owner, random.randint(1, maxY), random.randint(1, maxX))

while True:
    #
    showField()

    #
    while not doMove('X'):
        continue

    while not do_bot_move('O'):
        continue

    #
    if checkWinLoose():
        print('We have winner')
        showField()
        movesCount = maxMovesCount

    #
    if movesCount >= maxMovesCount:
        print('The game is over, bye!')
        break
    
    

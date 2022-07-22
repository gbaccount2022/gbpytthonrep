
# 3*x^3 + 5*x^2 + 10*x + 11
#         7*x^2        + 55
# 3*x^3 +12*x^2 + 10*x + 66

def fileToArray(fname):
    with open(fname, 'r') as f:
        return list(map(lambda x: x, f.read().replace(' ', '').split('+')))

def maxarr(arr1,arr2):
    if len(arr1) < len(arr2):
        return [arr2, arr1]
    return [arr1, arr2]

def looksSame(x, rate):
    if (len(rate) == 0):
        return x.find('x') == -1

    if len(x) < len(rate):
        return False

    pos = x.find(rate)
    pos1= len(x) - len(rate)
    return pos == pos1


result = []
[arr1, arr2] = maxarr(fileToArray('2.txt'), fileToArray('1.txt'))


for index,item in enumerate(arr1):
    items1 = item.split('*')

    if (len(items1) > 1):
        rate = items1[1]
    else:
        #
        rate = ''

    newitem = list(filter(lambda x: looksSame(x, rate), arr2))

    if len(newitem) > 0:
        newitem = newitem[0]
        items2 = newitem.split('*')
        if len(items2) > 1:
            result.append(str(int(items1[0]) + int(items2[0])) + items1[1])
        else:
            result.append(str(int(items1[0]) + int(items2[0])))
    else:
        result.append(item)


print(f'result: {" + ".join(result)}')
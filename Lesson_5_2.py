

def getmin(arr):
    result = arr[0]
    for index, item in enumerate(arr):
        if (item < result):
            result = item

    return result


def run(arr):

    minItem = getmin(arr)
    maxItem = minItem

    while True:
        exit = True
        for index, item in enumerate(arr):
            if (maxItem + 1 == item):
                maxItem = item
                exit = False
                break
        if exit:
            break

    return [minItem, maxItem]


print(run([1, 5, 2, 3, 4, 6, 1, 7]))
print(run([1, 5, 2, 3, 4, 1, 7]))
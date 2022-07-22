

######################################
# 1.txt - 1 2 3
# 2.txt - 4 4 4
# result = 1 + 2 + 3 + 4 + 4 + 4 = 18


def fileToArray(fname):
    with open(fname, 'r') as f:
        return list(map(lambda x: x, f.read().split()))

arr1 = fileToArray('1.txt')
arr2 = fileToArray('2.txt')

arr1.extend(arr2)

sum = 0
for index, item in enumerate(arr1):
    sum += int(item)

print(f'result: {sum}')
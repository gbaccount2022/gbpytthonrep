

def lookingForString(lst, str):

    print(f'Array {lst} looking for "{str}"')

    try:
        i = lst.index(str)
    except:
        return 'No'

    return 'Yes'


print(lookingForString([1,2,3,4,5], 4))
print(lookingForString([1,2,3,4,5], 32))
print(lookingForString([1,243,3,4,5], 243))


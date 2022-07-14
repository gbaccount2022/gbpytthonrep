

def lookingForString(lst, str):

    print(f'Array {lst} looking for "{str}"')

    try:
        i = lst.index(str)
        if i >= 0:
            i = lst.index(str, i+1)
    except:
        return -1

    return i


print(lookingForString(["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"))
print(lookingForString(["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "йцу"))
print(lookingForString(["йцу", "фыв", "ячс", "цук", "йцукен"], "йцу"))
print(lookingForString(["123", "234", 123, "567"], "123"))
print(lookingForString([], "123"))




def docalcs(n):
    res = []
    for i in range(1, n+1):
        if (i == 1):
            res.append(i)
        else:
            res.append(res[len(res)-1] * i)
    return res


print(docalcs(4))
print(docalcs(int(input("Enter N (int):"))))
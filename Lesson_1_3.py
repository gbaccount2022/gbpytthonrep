
x = int(input())
y = int(input())


# 
#  2 | 1
# ---+---
#  3 | 4
#    

if x > 0 and y > 0:
    print(1)
if x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
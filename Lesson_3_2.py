


line = input('Enter words with spaces:')
#line = "a aa abC aa ac abc bcd a"

counter = {}
words = line.split(" ")

for i in words:
    key = i.lower()
    counter.setdefault(key, 0)
    counter[key] += 1

for i in counter:
    print(f'{i} {counter[i]}')
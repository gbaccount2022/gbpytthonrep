
def encodeString(instr):

    i = 0

    result = ''

    while i <= len(instr):
        
        count = 1
        ch = instr[i]

        for j in range(i+1, len(instr)):
            if ch == instr[j]:
                count += 1
            else:
                if count <= 1:
                    result += ch
                else:
                    result = result + str(count) + ch
                break

        i = j

        if i >= len(instr) - 1:
            result += instr[i]
            break

    return result




def decodeString(instr):
    result = ''
    for i in range(len(instr)):
        count = instr[i]
        if '0123456789'.find(count) != -1:
            count = int(count)
            ch = instr[i+1]
            result = result + "".join(ch for x in range(count-1))
        else:
            result += count

    return result




str1 = 'hhhelllllllloooo wooooorld'

encoded = encodeString(str1)
decoded = decodeString(encoded)

print(f'orig: {str1}')
print(f'enc : {encoded}')
print(f'dec : {decoded}')

fileDesc = 0

def init(fname):
    global fileDesc
    fileDesc = open(fname, "w")
    
def write(info):
    global fileDesc
    print(info)
    fileDesc.write(f'{info}\n')

def deinit():
    fileDesc.close()
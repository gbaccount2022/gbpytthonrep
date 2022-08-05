import json
from os import truncate


def init(filename, mode = "a+"):
    result = open(filename, mode)
    maxid = 0
    all = search({'db': result}, {})
    for i in all:
        if i['_id'] > maxid:
            maxid = i['_id']

    return {
        'db': result, 
        'path': filename,
        'mode': mode,
        '_id' : maxid,
        }



def insert(db, document, setNewId = True):
    
    if setNewId:
        db['_id'] += 1
        document['_id'] = db['_id']
    
    db['db'].write(f'{json.dumps(document)}\n')
    db['db'].flush()

    return



def search(db, query):
    db['db'].seek(0, 0)

    result = []

    for line in db['db']:
        dbRow = json.loads(line)
        acceptCount = len(query)

        if acceptCount == 0:
            result.append(dbRow)
            continue

        for queryNameIndex in query:

            lookingForAccept = 0

            for rowNameIndex in dbRow:
                if queryNameIndex == rowNameIndex:
                    if query[queryNameIndex] == dbRow[rowNameIndex]:
                        lookingForAccept += 1

            if (lookingForAccept == acceptCount):
                result.append(dbRow)

    return result



def remove(db, query):
    all = search(db, {})

    if len(query) == 0:
        db['db'].truncate(0)
        return

    q = search(db, query)[0]
    db['db'].truncate(0)

    for i in all:
        a,b = json.dumps(i, sort_keys=True), json.dumps(q, sort_keys=True)
        if a == b:
            continue
        db['db'].write(f'{json.dumps(i)}\n')
        db['db'].flush()
    return



def close(db):
    db['db'].close()


import mydatabase as database
import json
import os

#######################################################
jobs = 0
department = 0
workers = 0
base = 0


#######################################################
def open_db():
    global jobs
    global department
    global workers
    global base

    jobs = database.init(os.path.dirname(__file__) + '/jobs.txt')
    department = database.init(os.path.dirname(__file__) + '/departments.txt')
    workers = database.init(os.path.dirname(__file__) + '/workers.txt')
    base = database.init(os.path.dirname(__file__) + '/base.db.txt')

    return




#######################################################
def getOptionsResult(db, text, default = 0):

    result = default

    while True:
        all = database.search(db, {})

        for item in all:
            print(f'{item["_id"]} {item["name"]}')

        result = int(input(text) or default)

        item = database.search(db, {'_id': result})
        if len(item) != 0:
            break

    return result


#######################################################
def get_worker_info(defaults = {
    'fio': 'none',
    'phone': 'none',
    'id_post': 0,
    'id_otdel': 0,
    'post_name': 'none',
    'otdel_name': 'none',
}):

    man = {
        'fio': input(f'Введите фамилию ({defaults["fio"]}): ') or defaults["fio"],
        'phone': input(f'Введите номер телефона ({defaults["phone"]}): ') or defaults["phone"],
    }

    baserow = {
        'id_post': getOptionsResult(jobs, f'Введите должность ({defaults["post_name"]}): ', defaults['id_post']),
        'id_otdel': getOptionsResult(department, f'Введите отдел: ({defaults["otdel_name"]})', defaults['id_otdel']),
    }

    return man, baserow


#######################################################
def add_worker():

    man, baserow = get_worker_info()
    database.insert(workers, man)

    baserow['id_man'] = workers['_id']    
    database.insert(base, baserow)

    return


#######################################################
def change_worker(id=0):
    if id == 0:
        id = int(input('Введите номер сотрудника для изменения:'))

    worker = database.search(base, {'_id': id})[0]

    man = database.search(workers, {'_id': worker['id_man']})[0]
    post = database.search(jobs, {'_id': worker['id_post']})[0]
    otdel = database.search(department, {'_id': worker['id_otdel']})[0]

    manInfo, baserow = get_worker_info({
        'fio': man['fio'],
        'phone': man['phone'],
        'id_post': worker['id_post'],
        'id_otdel': worker['id_otdel'],
        'post_name': post['name'],
        'otdel_name': otdel['name']
    })

    man['fio'] = manInfo['fio']
    man['phone'] = manInfo['phone']

    worker['id_post'] = baserow['id_post']
    worker['id_otdel'] = baserow['id_otdel']

    database.remove(workers, {'_id': man['_id']})
    database.remove(base, {'_id': worker['_id']})
    database.insert(workers, man, False)
    database.insert(base, worker, False)

    return


#######################################################
def show_workers():
    print('\n------------------------------')
    allWorkers = database.search(base, {})

    allWorkers = sorted(allWorkers, key=lambda k: k['_id'])
#   allWorkers.sort(lambda x,y: x['_id'] > y['_id'])

    for i in allWorkers:
        job = database.search(jobs, {'_id': i['id_post']})[0]
        dep = database.search(department, {'_id': i['id_otdel']})[0]
        work= database.search(workers, {'_id': i['id_man']})[0]
        print(f'id={i["_id"]} {job["name"]}({dep["name"]}) {work["fio"]}, {work["phone"]}')

    print('------------------------------')
    return


#######################################################
def del_worker(id=0):
    if id == 0:
        id = int(input('Введите номер сотрудника для удаления:'))
    w = database.search(base, {'_id': id})[0]
    database.remove(workers, {'_id': w['id_man']})
    database.remove(base, {'_id': w['_id']})
    show_workers()
    return


#######################################################
def db_import():
    fname = input('Введите имя файла для импорта (output.bak.txt):') or 'output.bak.txt'

    with open(fname, 'r') as f:
        lines = f.readlines()[0]
        obj = json.loads(lines)

        database.remove(workers, {})
        database.remove(base, {})
        database.remove(jobs, {})
        database.remove(department, {})

        for i in obj['w']: 
            database.insert(workers, i, False)
        for i in obj['b']: 
            database.insert(base, i, False)
        for i in obj['j']: 
            database.insert(jobs, i, False)
        for i in obj['d']: 
            database.insert(department, i, False)

    return


#######################################################
def db_export():
    fname = input('Введите имя файла для экспорта: (output.bak.txt)') or 'output.bak.txt'

    w = database.search(workers, {})
    b = database.search(base, {})
    j = database.search(jobs, {})
    d = database.search(department, {})

    bak = {
        'w': w,
        'b': b,
        'j': j,
        'd': d,
    }

    with open(fname, 'w') as f:
        f.write(f'{json.dumps(bak)}')
        f.flush()

    
    return


#######################################################
def _exit():
    exit(0)


#######################################################
menu = {
    0: ["Показать список сотрудников", show_workers],
    1: ["Добавить сотрудника", add_worker],
    2: ["Удалить сотрудника", del_worker],
    3: ["Изменить данные сотрудника", change_worker],
    4: ["Импорт БД", db_import],
    5: ["Экспорт БД", db_export],
    6: ["Выход", _exit],
}

# debug
# show_workers()
#add_worker()
#del_worker()
#show_workers()
#change_worker(3)

open_db()

#######################################################
while True:
    print('\n\t#############################')
    for index in menu:
        print(f'\t{index} {menu[index][0]}')

    option = int(input('Выберите действие: '))
    if option > len(menu):
        continue

    menu[option][1]()



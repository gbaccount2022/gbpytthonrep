

import mydatabase as database
import os
import telebot
from telebot import types

#######################################################
jobs = 0
department = 0
workers = 0
base = 0
dbMode = 'none'


def checkKeys(sendmsg, indata, checkdata):
    for i in checkdata:
        if not i in indata:
            t = type (checkdata[i])
            if t.__name__ == 'list':
                sendmsg(checkdata[i][0])
                checkdata[i][1]()
            else:
                sendmsg(checkdata[i])
            return False
    return True

def fillKey(totaldata, checkdata, nextValue):
    for i in checkdata:
        if not i in totaldata:
            totaldata[i] = nextValue
            return False
    return True


dic = {
    "one": 1,
    "two": 2,
}



"""
print(checkKeys(print, dic, {
    "one": "Enter one",
}))
print(checkKeys(print, dic, {
    "one": "Enter one",
    "two": "Enter two",
}))

print(checkKeys(print, dic, {
    "one": "Enter one",
    "two": "Enter two",
    "three": "Enter three",
}))
"""

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
def showOptions(sendmsg, db):

    all = database.search(db, {})

    for item in all:
        sendmsg(f'{item["_id"]} {item["name"]}')


#######################################################
addWorkerInfo = {}
def add_worker(sendmsg):

    man = {
        "fio": addWorkerInfo["fio"],
        "phone": addWorkerInfo["phone"]
    }

    baserow = {
        "id_post": addWorkerInfo["id_post"],
        "id_otdel": addWorkerInfo["id_otdel"]
    }
    
    database.insert(workers, man)

    baserow['id_man'] = workers['_id']    
    database.insert(base, baserow)

    show_workers(sendmsg)

    return



#######################################################
def show_workers(sendmsg):
    allWorkers = database.search(base, {})

    allWorkers = sorted(allWorkers, key=lambda k: k['_id'])

    for i in allWorkers:
        job = database.search(jobs, {'_id': int(i['id_post'])})[0]
        dep = database.search(department, {'_id': int(i['id_otdel'])})[0]
        work= database.search(workers, {'_id': int(i['id_man'])})[0]
        sendmsg(f'id={i["_id"]} {job["name"]}({dep["name"]}) {work["fio"]}, {work["phone"]}')
    return


#######################################################
delWorkerInfo = {}
def del_worker(sendmsg, id=0):
    w = database.search(base, {'_id': id})[0]
    database.remove(workers, {'_id': w['id_man']})
    database.remove(base, {'_id': w['_id']})
    show_workers(sendmsg)
    return


open_db()


tgbot = telebot.TeleBot("TOKEN", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
@tgbot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Add worker'))
    markup.add(types.KeyboardButton('Delete worker'))
    markup.add(types.KeyboardButton('Show all'))
    tgbot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)

@tgbot.message_handler(content_types='text')
def message_reply(message):

    global dbMode
    global addWorkerInfo
    global delWorkerInfo
    
    snd = lambda x: tgbot.send_message(message.chat.id, x)

    addMask = {
        'fio': 'Введите фамилию',
        'phone': 'Введите телефон',
        'id_post': ['Введите должность', lambda : showOptions(snd, jobs)],
        'id_otdel': ['Введите отдел', lambda : showOptions(snd, department)],
    }

    delMask = {
        "_id": "Введите Id сотрудника"
    }

    if dbMode == 'add':
        fillKey(addWorkerInfo, addMask, message.text)
        if checkKeys(snd, addWorkerInfo, addMask):
            add_worker(snd)
            dbMode = 'none'
        return

    if dbMode == 'del':
        _id = int(message.text)
        del_worker(snd, _id)
        dbMode = 'none'
        return

    if message.text == 'Add worker':
        dbMode = 'add'
        addWorkerInfo = {}
        checkKeys(snd, addWorkerInfo, addMask)

    elif message.text == 'Delete worker':
        dbMode = 'del'
        delWorkerInfo = {}
        checkKeys(snd, delWorkerInfo, delMask)

    elif message.text == 'Show all':
        show_workers(snd)

tgbot.infinity_polling()


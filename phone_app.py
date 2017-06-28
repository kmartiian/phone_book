import json
''' Bug: txt file phone_book rewriting eachtime programm restarts'''
config = 'json' # temp var

def autosave(f):                             # decorator when changing phoneBook
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        print(phone_book)
        save(phone_book)
        return res
    return wrapper

def load_check(fun):
    try:
        return fun()
    except:
        return {}

def load_json():
    with open('phone_book.txt', 'rb') as f:
        jsonObj = json.load(f)
        return jsonObj


def save_json(obj):
    with open('phone_book.txt', 'wt') as f:

        json.dump(obj, f)

def save_load (config):
    if config == 'json':
        load = load_json
        save = save_json
    return load, save

def name_request():
    return input("Input the name: ")

def newname_rq():
    return input("Input newname: ")

def number_rq():
    return input('number: ')

def get_contact(name):
    return phone_book[name]

def is_contact(name):
    if name in phone_book:
        return get_contact(name)
    else:
        raise ValueError('No rq name in dict')

@autosave
def create_contact(name, number):
    phone_book[name] = number


@autosave
def update_by_newname(name,newname):
    phone_book[newname] = phone_book[name]
    del phone_book[name]

@autosave
def delete_contact(name):
    del phone_book[name]


def controller(command):
    name = name_request()
    if command == 'f':
        try:
            is_contact(name)
            print(get_contact(name))
        except:
            print('No such name')

    elif command == 'u':
        newname = newname_rq()
        update_by_newname(name, newname)
    elif command == 'n':
        number = number_rq()
        create_contact(name, number)
    elif command == 'd':
        delete_contact(name)


load, save = save_load (config)

phone_book = load_check(load)

command = input('Your command: ')
controller(command)

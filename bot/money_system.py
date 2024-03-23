import json                                                               #importing
from . import config



main_data = json.load(open("data/money_main.json", "r"))                  #jsons loading
helper_data = json.load(open("data/money_helper.json", "r"))


def save_changes_to_json(data, Json):                                     #functions
    json.dump(data, open(f"data/{Json}.json", "w"))


def find_index(id_type, id):
    for index, item in enumerate(main_data):
        if item[id_type] == id:
            return index
    return None


def getEnding(index):
    if main_data[gender] == "male":
        return "в"
    elif main_data[gender] == "female":
        return "ла"
    elif main_data[gender] == "neutral":
        return "ло"


def give_money(giver_id_type, giver, receiver, money_amount):
    return "Hello World!"


def show_balace(person):
    return "Hello World!"


def show_general_money_amount():
    return "Hello World!"


def show_inflation_rate():
    irt = str(format((config.inflation_rate - 1) * 100, ".1f"))
    if irt[-2:] == ".0":
        irt = irt[:-2]
    else:
        irt = irt.replace(".", ",")
    return f"Рівень інфляції: {irt}%"


print(show_inflation_rate())

import json                                                         #importing
import config



main_data = json.load(open("../data/money_main.json", "r"))         #jsons loading
helper_data = json.load(open("../data/money_helper.json", "r"))


def save_changes_to_json(data):                                     #functions
    json.dump(data, open("../data/my_dict.json", "w"))


def find_index(id_type, id):
    for index, item in enumerate(main_data):
        if item[id_type] == id:
            return index
    return None


def give_money(giver_id_type, giver, receiver, money_amount):
    return "Hello World!"


def show_balace(person):
    return "Hello World!"


def show_general_money_amount():
    return "Hello World!"


def show_inflation_rate():
    inflation_rate_transfomed = str(format((config.inflation_rate - 1) * 100, ".1f"))
    if inflation_rate_transfomed[-2:] == ".0":
        inflation_rate_transfomed = inflation_rate_transfomed[:-2]
    else:
        inflation_rate_transfomed = inflation_rate_transfomed.replace(".", ",")
    return f"Рівень інфляції: {inflation_rate_transfomed}%"


print(show_inflation_rate())

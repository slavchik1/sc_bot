import json                                                               #importing
from . import config



main_data = json.load(open("data/data_main.json", "r"))                   #jsons loading
helper_data = json.load(open("data/data_helper.json", "r"))


def save_changes_to_json(data, Json):                                     #functions
    json.dump(data, open(f"data/{Json}", "w"))


def float_to_string(float):
    string = str(format(float, ".1f"))
    if string[-2:] == ".0":
        return string[:-2]
    else:
        return string.replace(".", ",")


def string_to_float(string):
    try:
        answer = float(string.replace(",", "."))
    except:
        return None
    return answer


def find_index(id_type, id):
    for i in range(len(main_data)):
        if main_data[i][id_type] == id:
            return i


def give_money(giver_id_type, giver_id, args):
    if len(args) == 2:
        giver_index = find_index(giver_id_type, giver_id)
        receiver_index = find_index("name", args[0])
        given_money_amount = string_to_float(args[1])
        if given_money_amount is None:
            return "Помилка: сума яку ви хочите передати повина бути числом, а не чимось іншим."
        elif giver_index is None:
            return "Помилка: Ви не зараєстровані у грошовій системі. Для реєстрації напишіть /money_register."
        elif receiver_index is None:
            return f"Помилка: {args[0]} не зареєстрований у грошовій системі. Впевністся що Ви правильно написали нікнейм гравця та що він відповідає нікнейму з команди /members."
        elif args[0] == main_data[giver_index]["name"]:
            return "Помилка: Ви неможите дати гроші собі."
        elif given_money_amount > main_data[giver_index]["balance"]:
            return f"Помилка: не висточає {float_to_string(given_money_amount - main_data[giver_index]['balance'])} слк."
        elif given_money_amount < 0:
            return "Помилка: сума не може бути від'ємною."
        else:
            main_data[giver_index]["balance"] -= given_money_amount
            main_data[receiver_index]["balance"] += given_money_amount
            save_changes_to_json(main_data, "data_main.json")
            return f"Передано {float_to_string(given_money_amount)} слк на баланс {main_data[receiver_index]['name']}. Ваш баланс: {float_to_string(main_data[giver_index]['balance'])} слк."
    else:
        return "Помилка: кількість аргументів повина дорювнювати 2-ом."


def show_balance(args, id_type, id):
    if len(args) <= 1:
        if not args:
            index = find_index(id_type, id)
            if index is None:
                return "Помилка: Ви не зараєстровані у грошовій системі. Для реєстрації напишіть /money_register."
            else:
                return "Ваш баланс: " + float_to_string(main_data[index]["balance"])
        else:
            index = find_index("name", args[0])
            if index is None:
                return f"Помилка: {args[0]} не зареєстрований у грошовій системі. Впевністся що Ви правильно написали нікнейм гравця та що він відповідає нікнейму з команди /members."
            else:
                return f"Баланс {main_data[index]['name']}: {float_to_string(main_data[index]['balance'])} слк."
    else:
        return "Помилка: кількість аргументів повина бути менше або дорівнювати 1."


def show_inflation_rate():
    return f"Рівень інфляції: {float_to_string((config.inflation_rate - 1) * 100)}%"


def show_general_money_amount():
    general_money_amount = 0
    for i in main_data:
        general_money_amount += i["balance"]
    return f"Загальна кілкість славкоїнів: {float_to_string(general_money_amount)} слк."

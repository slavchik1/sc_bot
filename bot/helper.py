from decimal import Decimal                         #importing


def get_tg_args(message):                           #functions
    args = message.text.split()
    args.pop(0)
    return args

def decimal_addition(a, b):
    return float(Decimal(str(a)) + Decimal(str(b)))

def decimal_subtraction(a, b):
    return float(Decimal(str(a)) - Decimal(str(b)))

def decimal_multiplication(a, b):
    return float(Decimal(str(a)) * Decimal(str(b)))

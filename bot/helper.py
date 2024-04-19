def tg_get_args(message):
    args = message.text.split()
    args.pop(0)
    return args

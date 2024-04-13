def get_tg_args(message):
    args = message.text.split()
    args.pop(0)
    return args

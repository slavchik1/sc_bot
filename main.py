import telebot                                          #importing libraries
import discord
import logging
import multiprocessing
from discord.ext import commands
from multiprocessing import Process
import config
import texts


telebot.logger.setLevel(logging.DEBUG)                  #settings
tg = telebot.TeleBot(config.tgTOKEN)
intents = discord.Intents.default()
intents.message_content = True
ds = commands.Bot(command_prefix = "/", intents = intents)
ds.remove_command("help")


@tg.message_handler(commands = ["start"])                 #Discord and Telegram commands
def start(message):
    tg.send_message(message.chat.id, texts.start)

@ds.command()
async def start(ctx):
    await ctx.send(texts.start)



@tg.message_handler(commands = ["help"])
def start(message):
    tg.send_message(message.chat.id, texts.help)

@ds.command()
async def help(ctx):
    await ctx.send(texts.help)


@tg.message_handler(commands = ["help_help"])
def start(message):
    tg.send_message(message.chat.id, texts.help_help)

@ds.command()
async def help_help(ctx):
    await ctx.send(texts.help_help)


@tg.message_handler(commands = ["help_ip"])
def start(message):
    tg.send_message(message.chat.id, texts.help_ip)

@ds.command()
async def help_ip(ctx):
    await ctx.send(texts.help_ip)



@tg.message_handler(commands = ["about"])
def start(message):
    tg.send_message(message.chat.id, texts.about)

@ds.command()
async def about(ctx):
    await ctx.send(texts.about)



@tg.message_handler(commands = ["credits"])
def start(message):
    tg.send_message(message.chat.id, texts.credits)

@ds.command()
async def credits(ctx):
    await ctx.send(texts.credits)



@tg.message_handler(commands = ["rules"])
def start(message):
    tg.send_message(message.chat.id, texts.rules)

@ds.command()
async def rules(ctx):
    await ctx.send(texts.rules)



@tg.message_handler(commands = ["ip"])
def start(message):
    tg.send_message(message.chat.id, texts.ip)

@ds.command()
async def ip(ctx):
    await ctx.send(texts.ip)


@tg.message_handler(commands = ["ip_ip"])
def start(message):
    tg.send_message(message.chat.id, texts.ip_ip)

@ds.command()
async def ip_ip(ctx):
    await ctx.send(texts.ip_ip)



@tg.message_handler(commands = ["members"])
def start(message):
    tg.send_message(message.chat.id, texts.members)

@ds.command()
async def members(ctx):
    await ctx.send(texts.members)



@tg.message_handler(commands = ["version"])
def start(message):
    tg.send_message(message.chat.id, texts.version)

@ds.command()
async def version(ctx):
    await ctx.send(texts.version)


def start_tg():                                     #starting functions
    while True:
        try:
            tg.polling(non_stop = True)
        except Exception as e:
            print("tg R.I.P.: " + e)


def start_ds():
    while True:
        try:
            ds.run(config.dsTOKEN)
        except Exception as e:
            print("ds R.I.P.:" + e)


if __name__ == "__main__":                          #starting bots

    multiprocessing.set_start_method("spawn")

    process_tg = Process(target = start_tg)
    process_ds = Process(target = start_ds)

    process_tg.start()
    process_ds.start()

    process_tg.join()
    process_ds.join()

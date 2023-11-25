import telebot                                          #importing
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
ds = commands.Bot(command_prefix="/", intents=intents)
ds.remove_command("help")


@tg.message_handler(commands=["start"])                 #Discord and Telegram commands
def start(message):
    tg.send_message(message.chat.id, texts.start_)

@ds.command()
async def start(ctx):
    await ctx.send(texts.start_)


@tg.message_handler(commands=["help"])
def start(message):
    tg.send_message(message.chat.id, texts.help_)

@ds.command()
async def help(ctx):
    await ctx.send(texts.help_)


@tg.message_handler(commands=["about"])
def start(message):
    tg.send_message(message.chat.id, texts.about_)

@ds.command()
async def about(ctx):
    await ctx.send(texts.about_)


@tg.message_handler(commands=["credits"])
def start(message):
    tg.send_message(message.chat.id, texts.credits_)

@ds.command()
async def credits(ctx):
    await ctx.send(texts.credits_)


@tg.message_handler(commands=["rules"])
def start(message):
    tg.send_message(message.chat.id, texts.rules_)

@ds.command()
async def rules(ctx):
    await ctx.send(texts.rules_)


@tg.message_handler(commands=["ip"])
def start(message):
    tg.send_message(message.chat.id, texts.ip_)

@ds.command()
async def ip(ctx):
    await ctx.send(texts.ip_)


@tg.message_handler(commands=["members"])
def start(message):
    tg.send_message(message.chat.id, texts.members_)

@ds.command()
async def members(ctx):
    await ctx.send(texts.members_)


@tg.message_handler(commands=["version"])
def start(message):
    tg.send_message(message.chat.id, texts.version_)

@ds.command()
async def version(ctx):
    await ctx.send(texts.version_)


def start_tg():                                     #starting functions
    while True:
        try:
            tg.polling(non_stop=True)
        except Exception as e:
            print("tg R.I.P.: " + e)


def start_ds():
    while True:
        try:
            ds.run(config.dsTOKEN)
        except  Exception as e
            print("ds R.I.P." + e)


if __name__ == "__main__":                          #starting bots

    multiprocessing.set_start_method("spawn")

    process_tg = Process(target=start_tg)
    process_ds = Process(target=start_ds)

    process_tg.start()
    process_ds.start()

    process_tg.join()
    process_ds.join()

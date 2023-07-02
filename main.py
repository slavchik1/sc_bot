import telebot                                          #importing
import discord
import logging
from discord.ext import commands
from multiprocessing import Process
import config
import texts


telebot.logger.setLevel(logging.DEBUG)                  #settings
tg = telebot.TeleBot(config.tgTOKEN)
intents = discord.Intents.default()
intents.message_content = True
ds = commands.Bot(command_prefix="/", intents=intents)


@tg.message_handler(commands=["start"])                 #Discord and Telegram commands
def start(message):
    tg.send_message(message.chat.id, texts.start_)

@ds.command()
async def start(ctx):
    await ctx.send(texts.start__)


@tg.message_handler(commands=["help"])
def start(message):
    tg.send_message(message.chat.id, texts.help_)

@ds.command()
async def help_(ctx):
    await ctx.send(texts.help__)


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
    tg.polling(non_stop=True)


def start_ds():
    ds.run(config.dsTOKEN)


if __name__ == "__main__":                          #starting_bots
    process_tg = Process(target=start_tg)
    process_ds = Process(target=start_ds)

    process_tg.start()
    process_ds.start()

    process_tg.join()
    process_ds.join()

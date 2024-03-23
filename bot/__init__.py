import telebot                                          #importing
import discord
import logging
from discord.ext import commands
from multiprocessing import Process
from .private_config import *
from . import text_messages
from . import other_messages
from . import money_system
from . import money_system_text_messages


telebot.logger.setLevel(logging.DEBUG)                  #defeult settings
tg = telebot.TeleBot(tgTOKEN)
intents = discord.Intents.default()
intents.message_content = True
ds = commands.Bot(command_prefix="/", intents=intents)
ds.remove_command("help")


@tg.message_handler(commands=["start"])                 #Discord and Telegram commands
def start(message):
    tg.send_message(message.chat.id, text_messages.start)

@ds.command()
async def start(ctx):
    await ctx.send(text_messages.start)



@tg.message_handler(commands=["help"])
def start(message):
    tg.send_message(message.chat.id, text_messages.help)

@ds.command()
async def help(ctx):
    await ctx.send(text_messages.help)


@tg.message_handler(commands=["help_help"])
def start(message):
    tg.send_message(message.chat.id, text_messages.help_help)

@ds.command()
async def help_help(ctx):
    await ctx.send(text_messages.help_help)


@tg.message_handler(commands=["help_ip"])
def start(message):
    tg.send_message(message.chat.id, text_messages.help_ip)

@ds.command()
async def help_ip(ctx):
    await ctx.send(text_messages.help_ip)


@tg.message_handler(commands=["help_flag"])
def start(message):
    tg.send_message(message.chat.id, text_messages.help_flag)

@ds.command()
async def help_flag(ctx):
    await ctx.send(text_messages.help_flag)


@tg.message_handler(commands=["help_members"])
def start(message):
    tg.send_message(message.chat.id, text_messages.help_members)

@ds.command()
async def help_members(ctx):
    await ctx.send(text_messages.help_members)



@tg.message_handler(commands=["about"])
def start(message):
    tg.send_message(message.chat.id, text_messages.about)

@ds.command()
async def about(ctx):
    await ctx.send(text_messages.about)



@tg.message_handler(commands=["credits"])
def start(message):
    tg.send_message(message.chat.id, text_messages.credits)

@ds.command()
async def credits(ctx):
    await ctx.send(text_messages.credits)



@tg.message_handler(commands=["rules"])
def start(message):
    tg.send_message(message.chat.id, text_messages.rules)

@ds.command()
async def rules(ctx):
    await ctx.send(text_messages.rules)



@tg.message_handler(commands=["ip"])
def start(message):
    tg.send_message(message.chat.id, text_messages.ip)

@ds.command()
async def ip(ctx):
    await ctx.send(text_messages.ip)


@tg.message_handler(commands=["ip_ip"])
def start(message):
    tg.send_message(message.chat.id, text_messages.ip_ip)

@ds.command()
async def ip_ip(ctx):
    await ctx.send(text_messages.ip_ip)



@tg.message_handler(commands=["members"])
def start(message):
    tg.send_message(message.chat.id, text_messages.members)

@ds.command()
async def members(ctx):
    await ctx.send(text_messages.members)


@tg.message_handler(commands=["members_slavchik"])
def start(message):
    tg.send_message(message.chat.id, text_messages.members_slavchik)

@ds.command()
async def members_slavchik(ctx):
    await ctx.send(text_messages.members_slavchik)


@tg.message_handler(commands=["members_Savalio"])
def start(message):
    tg.send_message(message.chat.id, text_messages.members_Savalio)

@ds.command()
async def members_Savalio(ctx):
    await ctx.send(text_messages.members_Savalio)


@tg.message_handler(commands=["members_MarkoAntonio11"])
def start(message):
    tg.send_message(message.chat.id, text_messages.members_MarkoAntonio11)

@ds.command()
async def members_MarkoAntonio11(ctx):
    await ctx.send(text_messages.members_MarkoAntonio11)


@tg.message_handler(commands=["members_11_ArtemPR_23"])
def start(message):
    tg.send_message(message.chat.id, text_messages.members_11_ArtemPR_23)

@ds.command()
async def members_11_ArtemPR_23(ctx):
    await ctx.send(text_messages.members_11_ArtemPR_23)


@tg.message_handler(commands=["members_mr_bacoun"])
def start(message):
    tg.send_message(message.chat.id, text_messages.members_mr_bacoun)

@ds.command()
async def members_mr_bacoun(ctx):
    await ctx.send(text_messages.members_mr_bacoun)


@tg.message_handler(commands=["members_bear0re0"])
def start(message):
    tg.send_message(message.chat.id, text_messages.members_bear0re0)

@ds.command()
async def members_bear0re0(ctx):
    await ctx.send(text_messages.members_bear0re0)



@tg.message_handler(commands=["version"])
def start(message):
    tg.send_message(message.chat.id, text_messages.version)

@ds.command()
async def version(ctx):
    await ctx.send(text_messages.version)



@tg.message_handler(commands=["flag"])
def start(message):
    tg.send_message(message.chat.id, text_messages.flag)
    tg.send_photo(message.chat.id, open("images/flag.png", "rb"))

@ds.command()
async def flag(ctx):
    await ctx.send(text_messages.flag)
    await ctx.send(other_messages.ds_flag)


@tg.message_handler(commands=["flag_original"])
def start(message):
    tg.send_message(message.chat.id, text_messages.flag_original)
    tg.send_document(message.chat.id, open("images/server-icon.png", "rb"))

@ds.command()
async def flag_original(ctx):
    await ctx.send(text_messages.flag_original)
    await ctx.send(other_messages.ds_flag_original)



@tg.message_handler(commands=["timeinkyiv"])
def start(message):
    tg.send_message(message.chat.id, text_messages.timeinkyiv())

@ds.command()
async def timeinkyiv(ctx):
    await ctx.send(text_messages.timeinkyiv())



@tg.message_handler(commands=["money"])
def start(message):
    tg.send_message(message.chat.id, money_system_text_messages.money)

@ds.command()
async def money(ctx):
    await ctx.send(money_system_text_messages.money)


@tg.message_handler(commands=["money_register"])
def start(message):
    tg.send_message(message.chat.id, money_system_text_messages.money_register("Telegram", message.from_user.id))

@ds.command()
async def money_register(ctx):
    id = ctx.author.id
    await ctx.send(money_system_text_messages.money_register("Discord", id))





def start_tg():                                          #starting functions
    while True:
        try:
            tg.polling(non_stop=True)
        except Exception as e:
            print("tg R.I.P.: " + str(e))


def start_ds():
    while True:
        try:
            ds.run(dsTOKEN)
        except Exception as e:
            print("ds R.I.P.:" + str(e))

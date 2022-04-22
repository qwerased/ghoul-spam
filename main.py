from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

app = Client("my_account")


@app.on_message(filters.command("тп", prefixes=".") & filters.me)
def tp(_, msg):
    perc = 0
    intro ="Выступает Серёга Пират"
    msg.reply_text(intro)
    sleep(2)
    text = "🗙Моё тп отменено🗙"
    msg.edit(text)
    sleep(2)
    msg.edit("🎮‍Игра проебана давно🎮")
    sleep(2)
    msg.edit("🤦И это все моя вина🤦")
    sleep(2)
    msg.edit("🤦Моя вина🤦")
    sleep(2)
    msg.edit("🚧И если тот день не вернуть🚧")
    sleep(2)
    msg.edit("🛵Я все равно продолжу путь🛵")
    sleep(2)
    msg.edit("♾Просто забудтьте навсегда♾")
    sleep(2)
    msg.edit("♾Навсегда♾")
    sleep(2)

@app.on_message(filters.command("гуль", prefixes=".") & filters.me)

def ghoul(_, msg):
    perc = 0
    k = 1000
    x = 1000
    text = f'{x}-7={x - 7}'
    msg.edit(text)
    while k > 10:
        k -= 7
        x -= 7
        try:
            msg.edit(f'{x}-7={x - 7}')
            sleep(0.1)
        except FloodWait as e:
            sleep(e.x)
    msg.edit("Я гуль")

app.run()
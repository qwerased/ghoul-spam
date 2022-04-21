from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

app = Client("my_account")


@app.on_message(filters.command("tp", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0

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


app.run()
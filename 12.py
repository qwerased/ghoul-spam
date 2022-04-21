from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait


app = Client("my_account")

@app.on_message(filters.command("гуль", prefixes=".") & filters.me)

def ghoul(_, msg):
    perc = 0
    k = 1000
    x = 1000
    text = f'{x}-7={x - 7}'
    msg.edit(text)
    while k > 0:
        k -= 7
        x -= 7
        try:
            msg.edit(f'{x}-7={x - 7}')
            sleep(0.1)
        except FloodWait as e:
            sleep(e.x)
    msg.edit("Я гуль")







app.run()
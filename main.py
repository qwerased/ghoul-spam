from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

app = Client("my_account")


	
	
	
	
@app.on_message(filters.command("git", prefixes = ".") & filters.me)
def git(_,msg):
	
	text ="https://github.com/qwerased/ghoul-spam"
	msg.edit(text)
	while k<20:
		try:
			msg.reply_text(text)
			sleep(0.5)
			k+=1
		except FloodWait as e:
			sleep(e.x)

@app.on_message(filters.command("пнх", prefixes = ".") & filters.me)
def pnh(_,msg, k = 0):
	
	text ="Пошел нахуй"
	msg.edit(text)
	while k<20:
		try:
			msg.reply_text(text)
			sleep(0.5)
			k+=1
		except FloodWait as e:
			sleep(e.x)
			
@app.on_message(filters.command("Выступает Серёга Пират", prefixes = ".") & filters.me)
def tp(_, msg):
    perc = 0
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
  
 
 
# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)
	

app.run()
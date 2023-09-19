from javascript import require, On
import time
mf = require('mineflayer')
process = require('process')
process.env = require('dotenv').config()
def connect():
    servername = process.env.SERVER
    bot = mf.createBot({
        "host": process.env.SERVER,
        "port": process.env.PORT,
        "username": process.env.USERNAME,
        "password": process.env.PASSWORD,
        "auth": process.env.AUTH,
        "version": process.env.VERSION
    })

    @On(bot, "spawn")
    def onSpawn():
        print("Bot spawned")

    @On(bot, "chat")
    def onChat(username, message):
        with open(f"data/{servername}.csv", "a", encoding="UTF-8") as f:
            timestamp = int(time.time())
            message = replaceComma(message)
            f.write(f"{username},{message},timestamp\n")
        print(f"{username}: {message}")

def replaceComma(msg):
    return msg.replace(",", "⍣")
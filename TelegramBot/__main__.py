from TelegramBot import bot
from TelegramBot.logging import LOGGER
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

LOGGER(__name__).info("client successfully initiated....")
if __name__ == "__main__":
    bot.run()

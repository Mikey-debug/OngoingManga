from TelegramBot import bot
from TelegramBot.logging import LOGGER

LOGGER(__name__).info("client successfully initiated....")
if __name__ == "__main__":
    from pyrogram import types
    @bot.on_message(filters.command(["a", "b"]) & sudo_cmd)
        async def a():
        chat_id = -1728546352
        messages = await client.get_chat_history(chat_id, limit=1)
        latest_message = messages[0] if messages else None

        if latest_message:
            await bot.reply_text("Latest message:", latest_message.text)
        else:
            print("No messages found in the group.")

    bot.run()

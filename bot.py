import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Вставь сюда свой токен из BotFather между кавычек
BOT_TOKEN =8666097299:AAFVeZ8TOlvc0VnuAVPS6ShLExVxHcKVusA

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я твой бот для игры в Дурака. Сервер работает!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

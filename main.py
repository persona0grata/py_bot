import time
import logging
import random

from aiogram import Bot, Dispatcher, executor, types


TG_TOKEN = '5841858075:AAGG9s8xDHCOyTh4zYTmTHRQlsSaa3W5qcs'
MSG = 'SART:{}! ПОРА РАБОТАТЬ!!!'
MSG2 = 'SART:{}! ПЕРЕЗАПУСТИ БОТА!!!'

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'stop'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f'Привет, {user_full_name}!')
    
    while True:
        if(random.randint(1, 5) > 3):
            time.sleep(2 * random.randint(1, 100))
            await bot.send_message(user_id, MSG.format(user_name))
        else:
            if random.randint(1, 7) > 3:
                await bot.send_message(user_id, "Я черный узбек!)")
                await bot.send_message(user_id, "Надо класть кирпичи :(")
                if random.randint(1, 2) == 1:
                    await bot.send_message(user_id, "Прораб злой")
            else:
                await bot.send_message(user_id, "Sigaret chekishni va gorilla ichishni xohlaysiz")
    await bot.send_message(user_id, MSG2.format(user_name))
         
if __name__ == '__main__':
    executor.start_polling(dp)
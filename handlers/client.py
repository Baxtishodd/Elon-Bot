from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_bosh_menu, categories, States, Andijon_kb, Buxoro_kb
from aiogram.dispatcher.filters.state import State, StatesGroup

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    # try:
    await bot.send_message(message.from_user.id, "Xush kelibsiz bizning botga!", reply_markup=Buxoro_kb)
    await message.delete()
    # except:
    #     await message.reply("Murojaat uchun @adminga yozing!")

# class Form(StatesGroup):
#     babies = State()









def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])


# @dp.in



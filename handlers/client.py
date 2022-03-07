import logging
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode


class Form(StatesGroup):
    name = State()
    category = State()
    teritory = State()
    city = State()
    address = State()
    picture = State()
    phone = State()
    addinfo = State()


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Botimizga Xush kelibsiz!",
                           reply_markup=kb_bosh_menu)
    # await bot.delete_message(message.from_user.id, message.message_id)
    # await bot.delete_message(message.from_user.id, message.message_id-1)


@dp.message_handler()
async def ad_Start(message: types.Message):
    """
    📜E`lon berish
    """
    chat_id = message.chat.id
    if message.text == '📜E`lon berish':
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        await Form.name.set()
        await bot.send_message(chat_id, "E`lon nomini kiriting")


@dp.callback_query_handler()
async def ClearForm(call: types.CallbackQuery, state: FSMContext):
    # await bot.delete_message(call.from_user.id, call.message.message_id)

    if call.data == '❌ Bekor qilish':
        current_state = await state.get_state()
        if current_state is None:
            return
        logging.info('Elon  bekor qilindi!', current_state)
        await state.finish()
        await bot.send_message(
            call.from_user.id,
            "E'lon bekor qilindi. /start buyrug'idan foydalaning",
            reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=Form.name)
async def adName(message: types.Message, state: FSMContext):
    """
    process advertisement name
    """
    # await bot.delete_message(message.from_user.id, message.message_id)
    # await bot.delete_message(message.from_user.id, message.message_id-1)
    chat_id = message.chat.id
    async with state.proxy() as data:
        data['name'] = message.text
    await Form.next()
    await bot.send_message(chat_id,
                           f"✅ Qabul qilindi\n*{str(message.text).title()}*\n\n"
                           f"E\`lon turini tanlang❗",
                           reply_markup=categories, parse_mode=ParseMode.MARKDOWN_V2
                           )


@dp.callback_query_handler(state=Form.category)
async def adCategory(call: types.CallbackQuery, state: FSMContext):
    """
    process advertisement category
    """
    chat_id = call.from_user.id
    await bot.delete_message(call.from_user.id, call.message.message_id)
    # await bot.delete_message(call.from_user.id, call.message.message_id-1)

    async with state.proxy() as data:
        data['category'] = call.data
    await Form.next()
    await bot.send_message(chat_id,
                           f"✅ Qabul qilindi\n\n*{call.data}*\n\nViloyatni tanlang❗️",
                           reply_markup=States_kb, parse_mode=ParseMode.MARKDOWN_V2)


@dp.callback_query_handler(state=Form.teritory)
async def adTeritory(call: types.CallbackQuery, state: FSMContext):
    """
    process user teritory
    """
    chat_id = call.from_user.id
    await bot.delete_message(call.from_user.id, call.message.message_id)

    async with state.proxy() as data:
        data['teritory'] = call.data
    await Form.next()

    if call.data == 'Andijon':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Andijon_kb)
    elif call.data == 'Buxoro':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Buxoro_kb)
    elif call.data == 'Farg`ona':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Fargona_kb)
    elif call.data == 'Jizzax':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Jizzax_kb)
    elif call.data == 'Namangan':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Namangan_kb)
    elif call.data == 'Navoiy':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Navoiy_kb)
    elif call.data == 'Qashqadaryo':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Qashqadaryo_kb)
    elif call.data == 'Qoraqalpog`iston':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Qoraqalpogiston_kb)
    elif call.data == 'Samarqand':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Samarqand_kb)
    elif call.data == 'Sirdaryo':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Sirdaryo_kb)
    elif call.data == 'Surxandaryov':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Surxandaryo_kb)
    elif call.data == 'Toshkent':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Toshkent_kb)
    elif call.data == 'Xorazm':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Xorazm_kb)


@dp.callback_query_handler(state=Form.city)
async def adCity(call: types.CallbackQuery, state: FSMContext):
    """
    process advertisement address
    """
    chat_id = call.from_user.id
    # await bot.delete_message(call.from_user.id, call.message.message_id)

    async with state.proxy() as data:
        data['city'] = call.data
    await Form.next()
    await bot.send_message(chat_id,
                           f"✅ Qabul qilindi\n*shaxar nomi*\n\nManzilingizni kiriting❗️",
                           reply_markup=ReplyKeyboardRemove, parse_mode=ParseMode.MARKDOWN_V2)


@dp.message_handler(state=Form.address)
async def adAddress(message: types.Message, state: FSMContext):
    """
    process advertisement address
    """
    chat_id = message.from_user.id
    # await bot.delete_message(message.from_user.id, message.message_id)

    async with state.proxy() as data:
        data['address'] = message.text
    await Form.next()
    await bot.send_message(chat_id,
                           f"✅ Qabul qilindi\n*{message.text}*\n\nE\`longa tegishli rasmlarni yuboring beshtadan oshmasin❗️",
                           reply_markup=ReplyKeyboardRemove, parse_mode=ParseMode.MARKDOWN_V2)


@dp.message_handler(content_types=['photo'], state=Form.picture)
async def adPicture(message: types.Message, state: FSMContext):
    """
    process advertisement picture
    """
    chat_id = message.chat.id
    file_id = message.photo[-1].file_id
    async with state.proxy() as data:
        data['picture'] = file_id
    await Form.next()
    await bot.send_photo(chat_id, photo=file_id,
                         caption="✅ Qabul qilindi\n\n*Telefon Raqamingizni kiriting*", parse_mode=ParseMode.MARKDOWN_V2)


@dp.message_handler(state=Form.phone)
async def adPhone(message: types.Message, state: FSMContext):
    """
    process user phone number
    """
    chat_id = message.chat.id
    async with state.proxy() as data:
        data['phone'] = message.text
    await Form.next()
    bot.send_message(chat_id,
                     f"✅ Qabul qilindi\n\n"
                     f"*{message.text}*\n"
                     f"Qo`shimcha ma`lumotlari",
                     parse_mode=ParseMode.MARKDOWN_V2)


@dp.message_handler(state=Form.addinfo)
async def adAdInfo(message: types.Message, state: FSMContext):
    """
    process ad additional info
    """
    chat_id = message.chat.id
    await bot.send_photo(chat_id,
                         photo=Form.picture,
                         caption=f"*{str(Form.name).title()}*\n"
                                 f"🔍*Turi:* {Form.category}\n"
                                 f"*Viloyati:* {Form.teritory}]n"
                                 f"*Hududi:* {Form.city}\n"
                                 f"*Manzili:* {Form.address}\n"
                                 f"*📞 Telefon:* {Form.phone}\n"
                                 f"📎*Qo`shimcha:* {Form.addinfo}\n\n"
                                 f"#{Form.teritory} #{Form.city} #{Form.address}\n"
                                 f"#{Form.category}",
                         parse_mode=ParseMode.MARKDOWN_V2,
                         reply_markup=kb_send)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])

# @dp.in

import logging
# import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import state

from create_bot import dp, bot
from keyboards import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode

# Admin id
ADMIN = '555278365'

# Chanel id
CHANNEL_ID = '-1001233690072'


class Form(StatesGroup):
    name = State()
    category = State()
    teritory = State()
    city = State()
    address = State()
    picture = State()
    phone = State()
    info = State()
    send = State()


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(message.from_user.id, "Botimizga Xush kelibsiz!",
                           reply_markup=kb_bosh_menu)

    # await bot.forward_message(chat_id, chat_id, message_id=500)
    # await bot.delete_message(message.from_user.id, message.message_id)
    # await bot.delete_message(message.from_user.id, message.message_id-1)


# Main menu commands
@dp.message_handler()
async def adStart(message: types.Message):
    """
    📜E`lon berish
    """
    chat_id = message.chat.id
    if message.text == "📜E'lon berish":
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        await Form.name.set()
        await bot.send_message(chat_id, "E'lon nomini kiriting")
    else:
        await message.reply("Tushunarsiz buyruq.\nQayta ishga tushiring! /start")


@dp.callback_query_handler(text="discard", state="*")
async def Discard(query: types.CallbackQuery, state: FSMContext):
    await state.reset_state(with_data=True)
    await query.message.delete()
    await bot.send_message(query.from_user.id, "E'lon bekor qilindi", reply_markup=kb_bosh_menu)


# @dp.callback_query_handler(state="*")
# async def backadName(call: types.CallbackQuery, state: FSMContext):
#     chat_id = call.message.chat.id
#     if call.data == "last_kb1":
#         await bot.delete_message(call.from_user.id, call.message.message_id)
#         await Form.previous()
#         await bot.send_message(chat_id, "E'lon nomini kiriting")
#     elif call.data == "last_kb2":
#         await bot.delete_message(call.from_user.id, call.message.message_id)
#         await Form.previous()
#         await bot.send_message(chat_id, "E'lon turini kiriting!")

    # await Form.name.set()
    # await bot.send_message(chat_id, "E'lon nomini kiriting")


@dp.message_handler(state=Form.name)
async def adName(message: types.Message, state: FSMContext):
    """
    process advertisement name
    """
    # await bot.delete_message(message.from_user.id, message.message_id)
    chat_id = message.chat.id

    async with state.proxy() as data:
        data['name'] = message.text
    await Form.next()
    await bot.send_message(chat_id,
                           f"✅ Qabul qilindi\n*{str(message.text).title()}*\n\n"
                           f"E'lon turini tanlang❗",
                           reply_markup=categories, parse_mode=ParseMode.MARKDOWN_V2
                           )

#
# @dp.callback_query_handler(text="last_kb2", state="category")
# async def backadCategory(call: types.CallbackQuery, state: FSMContext):
#     chat_id = call.message.chat.id
#     await bot.delete_message(call.from_user.id, call.message.message_id)
#     await Form.previous()
#     async with state.proxy() as data:
#         await bot.send_message(chat_id,
#                                f"✅ 1 Qabul qilindi\n*{str(data['name']).title()}*\n\n"
#                                f"*{str(call.message.text).title()}*\n\n"
#                                f"1 E'lon turini tanlang❗",
#                                reply_markup=categories, parse_mode=ParseMode.MARKDOWN_V2
#                                )


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
                           f"✅ Qabul qilindi\n\n<b>{call.data}</b>\n\nViloyatni tanlang❗️",

                           reply_markup=States_kb, parse_mode=ParseMode.HTML)


# @dp.callback_query_handler(text="last_kb3", state="teritory")
# async def backadTeritory(call: types.CallbackQuery, state: FSMContext):
#     chat_id = call.message.chat.id
#     await bot.delete_message(call.from_user.id, call.message.message_id)
#     await Form.teritory.set()
#     await bot.send_message(chat_id,
#                            f"✅ Qabul qilindi\n\n<b>{call.data}</b>\n\nViloyatni tanlang❗️",
#
#                            reply_markup=States_kb, parse_mode=ParseMode.HTML)


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
    elif call.data == 'Surxandaryo':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Surxandaryo_kb)
    elif call.data == 'Toshkent':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Toshkent_kb)
    elif call.data == 'Xorazm':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Xorazm_kb)
    elif call.data == 'Toshkent_shaxar':
        await bot.send_message(chat_id, f"✅ Qabul qilindi\n\n#{call.data}\nHududingizni belgilang❗️",
                               reply_markup=Toshkent_shkb)


@dp.callback_query_handler(state=Form.city)
async def adCity(call: types.CallbackQuery, state: FSMContext):
    """
    process advertisement address
    """
    chat_id = call.from_user.id
    await bot.delete_message(call.from_user.id, call.message.message_id)

    async with state.proxy() as data:
        data['city'] = call.data
    await Form.next()
    await bot.send_message(chat_id,
                           f"✅ Qabul qilindi\n#{data['teritory']} #{call.data}\n\nManzilingizni kiriting❗️",
                           parse_mode=ParseMode.HTML)


@dp.message_handler(state=Form.address)
async def adAddress(message: types.Message, state: FSMContext):
    """
    process advertisement address
    """
    chat_id = message.from_user.id
    await bot.delete_message(message.from_user.id, message.message_id)

    async with state.proxy() as data:
        data['address'] = message.text
    await Form.next()

    await bot.send_message(chat_id, f"✅ Qabul qilindi\n"
                                    f"#{message.text} Rasm yuboring!")


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
    await bot.send_photo(chat_id,
                         photo=file_id,
                         caption="✅ Qabul qilindi\n\nTelefon Raqamingizni kiriting",
                         parse_mode=ParseMode.HTML)


@dp.message_handler(state=Form.phone)
async def adPhone(message: types.Message, state: FSMContext):
    """
    process user phone number
    """
    chat_id = message.chat.id
    async with state.proxy() as data:
        data['phone'] = message.text
    await Form.next()
    await bot.send_message(chat_id,
                           f"✅ Qabul qilindi\n\n"
                           f"{message.text}\n"
                           f"Qo'shimcha ma'lumotlari",
                           parse_mode=ParseMode.HTML)


@dp.message_handler(state=Form.info)
async def adAdInfo(message: types.Message, state: FSMContext):
    """
    process ad additional info
    """
    chat_id = message.chat.id
    async with state.proxy() as data:
        data['info'] = message.text
    await Form.next()

    await bot.send_photo(chat_id,
                         photo=data['picture'],
                         caption=f"<b>{str(data['name']).title()}</b>\n"
                                 f"🔍<b>Turi:</b>{data['category']}\n"
                                 f"<b>Viloyati:</b> {data['teritory']}\n"
                                 f"<b>Hududi:</b> {data['city']}\n"
                                 f"<b>Manzili:</b> {data['address']}\n"
                                 f"📞 <b>Telefon:</b> {data['phone']}\n"
                                 f"📎<b>Qo'shimcha:</b> {data['info']}\n"
                                 f"#{data['teritory']} 》 #{data['city']} 》 #{str(data['address']).title()}\n"
                                 f"#{data['category']}\n"
                                 f"Kanalimizga obuna bo'ling!",
                         parse_mode=ParseMode.HTML,
                         reply_markup=kb_send)

    await bot.send_message(chat_id, "Tastiqlang!")


@dp.callback_query_handler(state=Form.send)
async def SendAdmin(call: types.CallbackQuery, state: FSMContext):
    """
    Send post to admin
    """
    async with state.proxy() as data:
        data['send'] = call.data
    await Form.next()
    chat_id = call.from_user.id

    if call.data == 'print':
        await bot.send_photo(ADMIN,
                             photo=data['picture'],
                             caption=f"<b>{str(data['name']).title()}</b>\n"
                                     f"🔍<b>Turi:</b>{data['category']}\n"
                                     f"<b>Viloyati:</b> {data['teritory']}\n"
                                     f"<b>Hududi:</b> {data['city']}\n"
                                     f"<b>Manzili:</b> {data['address']}\n"
                                     f"📞 <b>Telefon:</b> {data['phone']}\n"
                                     f"📎<b>Qo'shimcha:</b> {data['phone']}\n"
                                     f"#{data['teritory']} 》 #{data['city']} 》 #{str(data['address']).title()}\n"
                                     f"#{data['category']}\n"
                                     f"Kanalimizga obuna bo'ling!",
                             parse_mode=ParseMode.HTML)

        await bot.send_message(ADMIN, f"Foydalanuvchi Username: @{call.from_user.username}")
        await bot.send_message(chat_id, "Tabriklaymiz siz e'lon qo'shishni muvaffaqiyatli bajardingiz. "
                                        "E'loningiz moderator tomonidan tasdiqlangandan so'ng kanalga "
                                        "e'lon qilinadi va sizga xabar beriladi.",
                               reply_markup=kb_bosh_menu)

    elif call.data == 'discard':
        await bot.delete_message(chat_id, call.message.message_id)
        await bot.send_message(chat_id, "E'lon bekor qilindi!", reply_markup=kb_bosh_menu)

    await state.finish()


@dp.message_handler()
async def Listener_messages(message: types.Message):
    await message.answer(f"Xush kelibsiz {message.from_user.first_name}</b>", parse_mode=ParseMode.HTML)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])

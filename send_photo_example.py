import asyncio

from aiogram import Bot, Dispatcher, executor, filters, types
from aiogram.types import ParseMode

API_TOKEN = '5099386865:AAHgg8Rug1s-CVi7dcdTqulbMfxSd9yviRQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# @dp.message_handler(filters.CommandStart())
# async def send_welcome(message: types.Message):
#     # So... At first I want to send something like this:
#     await message.reply("Do you want to see many pussies? Are you ready?")
#
#     # Wait a little...
#     await asyncio.sleep(1)
#
#     # Good bots should send chat actions...
#     await types.ChatActions.upload_photo()
#
#     # Create media group
#     media = types.MediaGroup()
#
#     # Attach local file
#     media.attach_photo(types.InputFile('data/img.png'), 'Cat! Caption here!!!')
#     # More local files and more cats!
#     media.attach_photo(types.InputFile('data/img_1.png'))
#
#     # You can also use URL's
#     # For example: get random puss:
#     media.attach_photo('http://lorempixel.com/400/200/cats/')
#
#     # And you can also use file ID:
#     # media.attach_photo('<file_id>', 'cat-cat-cat.')
#
#     # Done! Send media group
#     # await message.reply_media_group(media=media)
#     # await bot.send_message(message.chat.id, f"{media}")
#     await bot.send_media_group(message.chat.id, media=media)

medlist = []
media = types.MediaGroup()
@dp.message_handler(content_types=['photo'])
async def photo_handling(message: types.Message):
    # Good bots should send chat actions...
    await types.ChatActions.upload_photo()

    # Create media group
    # media.attach_photo(message.photo[-1].file_id, caption=message.caption)

    medlist.append(message.photo[-1].file_id)


    # await bot.send_media_group(message.chat.id, media=media)


@dp.message_handler()
async def echo_handler(message: types.Message):

    text = message.text

    if text == "show":
        media.attach_photo(medlist[0],
                           caption=f"<b>.title</b>\n"
                               f"🔍<b>Turi:</b>test\n"
                               f"<b>Viloyati:</b> test\n"
                               f"<b>Hududi:</b> test\n"
                               f"<b>Manzili:</b> test\n"
                               f"📞 <b>Telefon:</b> test\n"
                               f"📎<b>Qo'shimcha:</b> test\n"
                               f"#test 》 #test\n"
                               f"#test\n"
                               f"Kanalimizga obuna bo'ling!", parse_mode=ParseMode.HTML)
        for i in medlist[1::]:
            media.attach_photo(i)
        await bot.send_media_group(message.chat.id, media=media)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

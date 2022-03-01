from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton,\
    InlineKeyboardButton, InlineKeyboardMarkup

# *Bosh menyu
b1 = KeyboardButton('📜E`lon berish')
b2 = KeyboardButton('📫Mening e`lonlarim')
b3 = KeyboardButton('Bizning kanallar')
b4 = KeyboardButton('📩Fikr bildirish')
b5 = KeyboardButton('📎Ma`lumot')
b6 = KeyboardButton('💬Takliflar')
b7 = KeyboardButton('⚙️Sozlamalar')

kb_bosh_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bosh_menu.add(b1, b2, b3, b4, b5, b6, b7)


# categories

ib1 = InlineKeyboardButton('Bolalar kiyimlari', callback_data='c_baby')
ib2 = InlineKeyboardButton('Elektronika', callback_data='c_electronics')
ib3 = InlineKeyboardButton('Kitoblar', callback_data='c_book')
ib4 = InlineKeyboardButton('Moda', callback_data='c_moda')
ib5 = InlineKeyboardButton('Qurilish', callback_data='c_qurilish')
ib6 = InlineKeyboardButton('Uy jihozlari', callback_data='c_home')
ib7 = InlineKeyboardButton('Xayvonlar', callback_data='c_animals')
ib8 = InlineKeyboardButton('Boshqa', callback_data='c_other')

b_cancel = InlineKeyboardButton('⬅️ Orqaga', callback_data='b_cancel')
b_clear = InlineKeyboardButton('❌ Bekor qilish', callback_data='b_clear')

categories = InlineKeyboardMarkup().add(ib1, ib2, ib3, ib4, ib5, ib6, ib7, ib8)
categories.row(b_cancel, b_clear)


# Viloyatlar
vb1 = InlineKeyboardButton('Andijon', callback_data='Andijon')
vb2 = InlineKeyboardButton('Buxoro', callback_data='Buxoro')
vb3 = InlineKeyboardButton('Farg`ona', callback_data='Farg`ona')
vb4 = InlineKeyboardButton('Jizzax', callback_data='Jizzax')
vb5 = InlineKeyboardButton('Namangan', callback_data='Namangan')
vb6 = InlineKeyboardButton('Navoiy', callback_data='Navoiy')
vb7 = InlineKeyboardButton('Qashqadaryo', callback_data='Qashqadaryo')
vb8 = InlineKeyboardButton('Qoraqalpog`iston', callback_data='Qoraqalpog`iston')
vb9 = InlineKeyboardButton('Samarqand', callback_data='Samarqand')
vb10 = InlineKeyboardButton('Sirdaryo', callback_data='Sirdaryo')
vb11 = InlineKeyboardButton('Surxandaryo', callback_data='Surxandaryo')
vb12 = InlineKeyboardButton('Toshkent', callback_data='Toshkent')
vb13 = InlineKeyboardButton('Xorazm', callback_data='Xorazm')
vb14 = InlineKeyboardButton('Toshkent shaxar', callback_data='Toshkent shaxar')

States = InlineKeyboardMarkup()
States.row(vb1, vb2)
States.row(vb3, vb4)
States.row(vb5, vb6)
States.row(vb7, vb7)
States.row(vb9, vb10)
States.row(vb11, vb12)
States.row(vb13, vb14)
States.row(b_cancel, b_clear)

# ============Tumanlar========
# Andijon

anb1 = InlineKeyboardButton('Andijon', callback_data='Andijon')
anb2 = InlineKeyboardButton('Asaka', callback_data='Asaka')
anb3 = InlineKeyboardButton('Baliqchi', callback_data='Baliqchi')
anb4 = InlineKeyboardButton('Bo`z', callback_data='Bo`z')
anb5 = InlineKeyboardButton('Buloqboshi', callback_data='Buloqboshi')
anb6 = InlineKeyboardButton('Izbosgan', callback_data='Izbosgan')
anb7 = InlineKeyboardButton('Jalaquduq', callback_data='Jalaquduq')
anb8 = InlineKeyboardButton('Marhamat', callback_data='Marhamat')
anb9 = InlineKeyboardButton('Oltinko`l', callback_data='Oltinko`l')
anb10 = InlineKeyboardButton('Paxtaobod', callback_data='Paxtaobod')
anb11 = InlineKeyboardButton('Qo`rg`ontepa', callback_data='Qo`rg`ontepa')
anb12 = InlineKeyboardButton('Shaxrixon', callback_data='Shaxrixon')
anb13 = InlineKeyboardButton('Ulug`nor', callback_data='Ulug`nor')
anb14 = InlineKeyboardButton('Xo`jaobod', callback_data='Xo`jaobod')

Andijon_kb = InlineKeyboardMarkup()
Andijon_kb.row(anb1, anb2)
Andijon_kb.row(anb3, anb4)
Andijon_kb.row(anb5, anb6)
Andijon_kb.row(anb7, anb8)
Andijon_kb.row(anb9, anb10)
Andijon_kb.row(anb11, anb12)
Andijon_kb.row(anb13, anb14)
Andijon_kb.row(b_cancel, b_clear)


# Buxoro

bub1 = InlineKeyboardButton('Buxoro', callback_data='Buxoro')
bub2 = InlineKeyboardButton('Kogon', callback_data='Kogon')
bub3 = InlineKeyboardButton('G`ijduvon', callback_data='G`ijduvon')
bub4 = InlineKeyboardButton('Shofirkon', callback_data='Shofirkon')
bub5 = InlineKeyboardButton('Qorako`l', callback_data='Qorako`l')
bub6 = InlineKeyboardButton('Olot', callback_data='Olot')
bub7 = InlineKeyboardButton('Jondor', callback_data='Jondor')
bub8 = InlineKeyboardButton('Qorovulbozor', callback_data='Qorovulbozor')
bub9 = InlineKeyboardButton('Peshku', callback_data='Peshku')
bub10 = InlineKeyboardButton('Romitan', callback_data='Romitan')
bub11 = InlineKeyboardButton('Vobkent', callback_data='Vobkent')

Buxoro_kb = InlineKeyboardMarkup()
Buxoro_kb.row(bub1, bub2)
Buxoro_kb.row(bub3, bub4)
Buxoro_kb.row(bub5, bub6)
Buxoro_kb.row(bub7, bub8)
Buxoro_kb.row(bub9, bub10)
Buxoro_kb.row(bub11)
Buxoro_kb.row(b_cancel, b_clear)

# Farg`ona

# farg`ona
# so`x
# quva
# rishton
# toshloq
# oltiariq
# beshariq
# yaypan
# bag`dod
# buvayda
# dang`ara
# furqat
# qo`shtepa
# uchko`prk
# yozyovon

fab1 = InlineKeyboardButton('Farg`ona', callback_data='Farg`ona')
fab2 = InlineKeyboardButton('So`x', callback_data='So`x')
fab3 = InlineKeyboardButton('Quva', callback_data='Quva')
fab4 = InlineKeyboardButton('Rishton', callback_data='Rishton')
fab5 = InlineKeyboardButton('Toshloq', callback_data='Toshloq')
fab6 = InlineKeyboardButton('Oltiariq', callback_data='Oltiariq')
fab7 = InlineKeyboardButton('Beshariq', callback_data='Beshariq')
fab8 = InlineKeyboardButton('Yaypan', callback_data='Yaypan')
fab9 = InlineKeyboardButton('Bag`dod', callback_data='Bag`dod')
fab10 = InlineKeyboardButton('Buvayda', callback_data='Buvayda')
fab11 = InlineKeyboardButton('Dang`ara', callback_data='Dang`ara')
fab12 = InlineKeyboardButton('Furqat', callback_data='Furqat')
fab13 = InlineKeyboardButton('Qo`shtepa', callback_data='Qo`shtepa')
fab14 = InlineKeyboardButton('Uchko`prik', callback_data='Uchko`prik')
fab15 = InlineKeyboardButton('Yozyovon', callback_data='Yozyovon')

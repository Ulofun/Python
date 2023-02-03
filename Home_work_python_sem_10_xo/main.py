from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger
from config import TOKEN
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

kb = [
    [
        InlineKeyboardButton("1", callback_data="num:1"),
        InlineKeyboardButton("2", callback_data="num:2"),
        InlineKeyboardButton("3", callback_data="num:3"),
    ],
    [
        InlineKeyboardButton("4", callback_data="num:4"),
        InlineKeyboardButton("5", callback_data="num:5"),
        InlineKeyboardButton("6", callback_data="num:6"),
    ],
    [
        InlineKeyboardButton("7", callback_data="num:7"),
        InlineKeyboardButton("8", callback_data="num:8"),
        InlineKeyboardButton("9", callback_data="num:9"),
    ],
]

action_callback = CallbackData("num", "item_name")
free_choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
counter = 0


def check_win(choice):
    if choice[0] == choice[1] == choice[2] or \
            choice[3] == choice[4] == choice[5] or \
            choice[6] == choice[7] == choice[8] or \
            choice[0] == choice[3] == choice[6] or \
            choice[1] == choice[4] == choice[7] or \
            choice[2] == choice[5] == choice[8] or \
            choice[0] == choice[4] == choice[8] or \
            choice[2] == choice[4] == choice[6]:
        return 1
    else:
        return False


storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)
logger.add('log_info.log',
           format="{time} - {level} - {message}",
           level='DEBUG')

print("Bot activate")


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.reply("Вас приветствует Бот_крестики-нолики\n"
                        "Для начала игры выберите в меню start_game")


@dp.message_handler(commands=['start_game'])
async def show_field(message: Message):
    global kb
    kb = [
        [
            InlineKeyboardButton("1", callback_data="num:1"),
            InlineKeyboardButton("2", callback_data="num:2"),
            InlineKeyboardButton("3", callback_data="num:3"),
        ],
        [
            InlineKeyboardButton("4", callback_data="num:4"),
            InlineKeyboardButton("5", callback_data="num:5"),
            InlineKeyboardButton("6", callback_data="num:6"),
        ],
        [
            InlineKeyboardButton("7", callback_data="num:7"),
            InlineKeyboardButton("8", callback_data="num:8"),
            InlineKeyboardButton("9", callback_data="num:9"),
        ],
    ]

    board = InlineKeyboardMarkup(inline_keyboard=kb)
    await message.reply(f'Первыми ходят {chr(10060)}\n'
                        'Сделайте ход выбрав цифру на поле', reply_markup=board)


@dp.callback_query_handler(action_callback.filter())
async def nums_choice(callback: CallbackQuery, callback_data: dict):
    global free_choice
    global kb
    global counter
    await callback.answer(cache_time=1)
    data = callback_data["item_name"]
    if data in free_choice:
        if data == '1':
            if counter % 2:
                kb[0][0] = InlineKeyboardButton(chr(11093), callback_data="num:1")
                free_choice[0] = "O"
                move = chr(10060)
            else:
                kb[0][0] = InlineKeyboardButton(chr(10060), callback_data="num:1")
                free_choice[0] = "X"
                move = chr(11093)
        elif data == '2':
            if counter % 2:
                kb[0][1] = InlineKeyboardButton(chr(11093), callback_data="num:2")
                free_choice[1] = "O"
                move = chr(10060)
            else:
                kb[0][1] = InlineKeyboardButton(chr(10060), callback_data="num:2")
                free_choice[1] = "X"
                move = chr(11093)

        elif data == '3':
            if counter % 2:
                kb[0][2] = InlineKeyboardButton(chr(11093), callback_data="num:3")
                free_choice[2] = "O"
                move = chr(10060)
            else:
                kb[0][2] = InlineKeyboardButton(chr(10060), callback_data="num:3")
                free_choice[2] = "X"
                move = chr(11093)

        elif data == '4':
            if counter % 2:
                kb[1][0] = InlineKeyboardButton(chr(11093), callback_data="num:4")
                free_choice[3] = "O"
                move = chr(10060)
            else:
                kb[1][0] = InlineKeyboardButton(chr(10060), callback_data="num:4")
                free_choice[3] = "X"
                move = chr(11093)

        elif data == '5':
            if counter % 2:
                kb[1][1] = InlineKeyboardButton(chr(11093), callback_data="num:5")
                free_choice[4] = "O"
                move = chr(10060)
            else:
                kb[1][1] = InlineKeyboardButton(chr(10060), callback_data="num:5")
                free_choice[4] = "X"
                move = chr(11093)

        elif data == '6':
            if counter % 2:
                kb[1][2] = InlineKeyboardButton(chr(11093), callback_data="num:6")
                free_choice[5] = "O"
                move = chr(10060)
            else:
                kb[1][2] = InlineKeyboardButton(chr(10060), callback_data="num:6")
                free_choice[5] = "X"
                move = chr(11093)

        elif data == '7':
            if counter % 2:
                kb[2][0] = InlineKeyboardButton(chr(11093), callback_data="num:7")
                free_choice[6] = "O"
                move = chr(10060)
            else:
                kb[2][0] = InlineKeyboardButton(chr(10060), callback_data="num:7")
                free_choice[6] = "X"
                move = chr(11093)

        elif data == '8':
            if counter % 2:
                kb[2][1] = InlineKeyboardButton(chr(11093), callback_data="num:8")
                free_choice[7] = "O"
                move = chr(10060)
            else:
                kb[2][1] = InlineKeyboardButton(chr(10060), callback_data="num:8")
                free_choice[7] = "X"
                move = chr(11093)

        elif data == '9':
            if counter % 2:
                kb[2][2] = InlineKeyboardButton(chr(11093), callback_data="num:9")
                free_choice[8] = "O"
                move = chr(10060)
            else:
                kb[2][2] = InlineKeyboardButton(chr(10060), callback_data="num:9")
                free_choice[8] = "X"
                move = chr(11093)
        counter += 1

        if counter > 3:
            win = check_win(free_choice)
            if win == 1 and counter % 2 != 0:
                free_choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                counter = 0
                logger.info('Пользователь ввел "X"')
                await callback.message.answer(f"УРА!!! {chr(129395)} Победили {chr(10060)}")
                await callback.answer()

            elif win == 1 and counter % 2 == 0:
                free_choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                counter = 0
                logger.info('Пользователь ввел "O"')
                await callback.message.answer(f"УРА!!! {chr(129395)} Победили {chr(11093)}")
                await callback.answer()

        if counter == 8:
            free_choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            counter = 0
            await callback.message.answer(f"Ничья!!! Повезёт в следующий раз {chr(128521)}")
            await callback.answer()

        logger.info(f'Пользователь ввел {data}')
        board = InlineKeyboardMarkup(inline_keyboard=kb)
        await callback.message.edit_text(f"Теперь ходят {move}", reply_markup=board)
        await callback.answer()
    else:
        logger.debug('Пользователь выбрал занятую клетку')
        board = InlineKeyboardMarkup(inline_keyboard=kb)
        await callback.message.edit_text(f"Клетка занята {chr(129402)} выберите другую", reply_markup=board)
        await callback.answer()


@dp.message_handler(commands=['stop_game'])
async def stop_game(message: Message):
    await message.answer(f'{message.from_user.first_name}, '
                         f"До встречи {chr(128075)}!")
    global free_choice
    global counter
    logger.info(f'Пользователь остановил игру')
    free_choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    counter = 0


@dp.message_handler()
async def echo(message: Message):
    global kb
    logger.debug('Не верный ввод пользователем')
    board = InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer(f'{message.from_user.first_name}, '
                         f'Пожалуйста, кликайте кнопки поля! {chr(128545)}', reply_markup=board)


executor.start_polling(dp)

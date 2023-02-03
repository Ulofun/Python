from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from loguru import logger
from calc import *
from config import TOKEN

storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)
logger.add('log_info.log',
           format="{time} - {level} - {message}",
           level='DEBUG')


class FSMData(StatesGroup):
    num_1 = State()
    action = State()
    num_2 = State()


print("Bot activate")


@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton('/calculation')
    keyboard.add(btn)
    await message.reply("Вас приветствует Бот_калькулятор\n"
                        "Для начала нажмите calculation", reply_markup=keyboard)


@dp.message_handler(commands=['calculation'])  # , state=None)
async def calculation(message: Message):
    await message.reply("Наберите первое число.")
    await FSMData.num_1.set()


@dp.message_handler(state=FSMData.num_1)
async def get_num1(message: Message, state: FSMContext):
    await state.update_data(num_1=message.text)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["+", "-", "*", "/", "%", "^"]
    keyboard.add(*buttons)
    await message.reply("Выберите необходимое действие", reply_markup=keyboard)
    await FSMData.next()


@dp.message_handler(state=FSMData.action)
async def get_action(message: Message, state: FSMContext):
    await state.update_data(action=message.text)
    await message.reply("Наберите второе число.")
    await FSMData.next()


@dp.message_handler(state=FSMData.num_2)
async def get_num_2(message: Message, state: FSMContext):
    await state.update_data(num_2=message.text)
    data = await state.get_data()

    res = obrabotka(data)
    if res == None:
        logger.debug('Введены некорректные значения')
        await message.answer('Одно или несколько введённых значений некорректны')
    elif res == 'error':
        logger.debug('Деление на ноль запрещено')
        await message.answer('Ай-ай-ай!!! На ноль делить нельзя!!!')
    else:
        await message.answer(f"{data['num_1']} "
                             f"{data['action']} "
                             f"{data['num_2']} = "
                             f"{res}")
    await state.finish()


executor.start_polling(dp)
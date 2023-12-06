import asyncio
import logging
from asyncio import Lock
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6748065445:AAGPfdlcjJBlqIijc51oxKZHKvl2cvmrW-g")
dp = Dispatcher(bot=bot, storage=MemoryStorage())

Base = declarative_base()
lock = Lock()

class Users(Base):
    __tablename__ = 'news_userform2'

    email = Column(String, nullable=True)
    password = Column(String, nullable=True)
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)


    def __init__(self, n, s):
        self.email = n
        self.password = s

engine = create_engine("sqlite:///db.sqlite3")

session = scoped_session(sessionmaker(bind=engine))



class RegisterMessages(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()


class DB:
    answer_data = {}


@dp.message_handler(text='/start', state=None)
async def start(message: types.Message):
    await RegisterMessages.step1.set()
    await bot.send_message(message.from_user.id, text='Здравствуйте!\nМеня зовут AnnaBot\nДавайте зарегистрируемся.\nВведите ваш email.')


@dp.message_handler(content_types='text', state=RegisterMessages.step1)
async def reg_step1(message: types.Message):
    async with lock:
        DB.answer_data['email'] = message.text
    await bot.send_message(message.from_user.id, text='Придумайте пароль!')
    await RegisterMessages.next()


@dp.message_handler(content_types='text', state=RegisterMessages.step2)
async def reg_step2(message: types.Message):
    async with lock:
        DB.answer_data['password'] = message.text
    await bot.send_message(message.from_user.id, text='Ваш email зарегестрирован!')
    await RegisterMessages.next()


#@dp.message_handler(content_types='text', state=RegisterMessages.step3)
#async def reg_step3(message: types.Message, state: FSMContext):
#    async with lock:
#        DB.answer_data['password2'] = message.text
#    await bot.send_message(message.from_user.id, text='Отлично! Вы зарегистрированы!')
#    await state.finish()
#    session.add(Users(DB.answer_data['email'], DB.answer_data['password']))
#    session.commit()


async def main():
    Base.metadata.create_all(engine)
    await dp.start_polling(bot)


# if __name__ == "__main__":
#     Base.metadata.create_all(engine)
#     asyncio.run(main())

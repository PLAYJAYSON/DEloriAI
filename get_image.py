import os
import requests
from bs4 import BeautifulSoup
from aiogram import executor
import asyncio
import random as rnd
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import imageio
# Устанавливаем уровень логов на уровень INFO
logging.basicConfig(level=logging.INFO)

# Токен бота
BOT_TOKEN = '6291980620:AAEvhP7fmt6TTQVJ07tG01VagVbRMlX_Ais'

# ID группы, в которую будут отправляться картинки
GROUP_ID = '@catscatsmorecatss'

# Создаем экземпляр бота
bot = Bot(token=BOT_TOKEN)

# Создаем экземпляр диспетчера
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Счетчик для переименования картинок
counter = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
# Список уже загруженных картинок
loaded_images = []
loaded_images_1 = []
loaded_images_2 = []
loaded_images_3 = []
# Состояния для FSM
class Form(StatesGroup):
    waiting = State()

# Функция для загрузки картинки и отправки ее в группу
async def send_image_11():
    global counter_3
    global loaded_images_3

    # Загружаем страницу сайта
    response_3 = requests.get('https://m.joyreactor.cc/tag/%D0%BA%D0%BE%D1%82%D1%8D', headers={'User-Agent': 'Mozilla/5.0'})
    html = response_3.text

    # Парсим HTML-код страницы
    soup_3 = BeautifulSoup(html, 'html.parser')

    # Ищем ссылки на картинки в коде страницы
    links_3 = 'https:' + soup_3.find('div', {'class': 'image'}).find('img')['src']

    # Скачиваем новую картинку, если она обновилась
    if links_3:
        filename_3 = links_3.split('/')[-1].split('?')[0]
        if filename_3 not in loaded_images_3:
            loaded_images_3.append(filename_3)
            counter_3 += 1
            filepath_3 = f'images/{counter_3}.jpg'
            response_3 = requests.get(links_3, headers={'User-Agent': 'Mozilla/5.0'})
            with open(filepath_3, 'wb') as f:
                f.write(response_3.content)
            if counter_3 > 1:
                os.remove(os.path.join('images', f'1.jpg'))
            os.rename(filepath_3, os.path.join('images', f'1.jpg'))
            logging.info(f'Картинка {filename_3} загружена в папку images')
            # Открываем картинку и обрезаем ее
            img = imageio.imread_v2(os.path.join('images', f'1.jpg'))
            img = img[:-15, :]
            imageio.imwrite(os.path.join('images', f'1.jpg'), img)
            with open(os.path.join('images', f'1.jpg'), 'rb') as photo:
                await bot.send_photo(chat_id=GROUP_ID, photo=photo, caption='[котики](t.me/catscatsmorecatss)', parse_mode='MarkdownV2')
async def send_image():
    global counter
    global loaded_images

    # Загружаем страницу сайта
    response = requests.get('https://www.reddit.com/r/cats/new/', headers={'User-Agent': 'Mozilla/5.0'})
    html = response.text

    # Парсим HTML-код страницы
    soup = BeautifulSoup(html, 'html.parser')

    # Ищем ссылки на картинки в коде страницы
    links = soup.find_all('img', {'alt': 'Post image'})

    # Скачиваем новую картинку, если она обновилась
    if links:
        url = links[0]['src']
        filename = url.split('/')[-1].split('?')[0]
        if filename not in loaded_images:
            loaded_images.append(filename)
            counter += 1
            filepath = f'images/{counter}.jpg'
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            with open(filepath, 'wb') as f:
                f.write(response.content)
            if counter > 1:
                os.remove(os.path.join('images', f'1.jpg'))
            os.rename(filepath, os.path.join('images', f'1.jpg'))
            logging.info(f'Картинка {filename} загружена в папку images')
            with open(os.path.join('images', f'1.jpg'), 'rb') as photo:
                await bot.send_photo(chat_id=GROUP_ID, photo=photo, caption='[котики](t.me/catscatsmorecatss)', parse_mode='MarkdownV2')

async def send_image_meme():
    global counter_1
    global loaded_images_1

    # Загружаем страницу сайта
    response_1 = requests.get('https://www.reddit.com/r/Catmemes/new/', headers={'User-Agent': 'Mozilla/5.0'})
    html = response_1.text

    # Парсим HTML-код страницы
    soup_1 = BeautifulSoup(html, 'html.parser')

    # Ищем ссылки на картинки в коде страницы
    links_1 = soup_1.find_all('img', {'alt': 'Post image'})

    # Скачиваем новую картинку, если она обновилась
    if links_1:
        url_1 = links_1[0]['src']
        filename_1 = url_1.split('/')[-1].split('?')[0]
        if filename_1 not in loaded_images_1:
            loaded_images_1.append(filename_1)
            counter_1 += 1
            filepath_1 = f'images/{counter_1}.jpg'
            response_1 = requests.get(url_1, headers={'User-Agent': 'Mozilla/5.0'})
            with open(filepath_1, 'wb') as f:
                f.write(response_1.content)
            if counter_1 > 1:
                os.remove(os.path.join('images', f'1.jpg'))
            os.rename(filepath_1, os.path.join('images', f'1.jpg'))
            logging.info(f'Картинка {filename_1} загружена в папку images')
            with open(os.path.join('images', f'1.jpg'), 'rb') as photo:
                await bot.send_photo(chat_id=GROUP_ID, photo=photo, caption='[котики](t.me/catscatsmorecatss)',parse_mode='MarkdownV2')
async def send_image_2():
    global counter_2
    global loaded_images_2

    # Загружаем страницу сайта
    response_2 = requests.get('https://www.reddit.com/r/Cat/new/', headers={'User-Agent': 'Mozilla/5.0'})
    html = response_2.text

    # Парсим HTML-код страницы
    soup_2 = BeautifulSoup(html, 'html.parser')

    # Ищем ссылки на картинки в коде страницы
    links_2 = soup_2.find_all('img', {'alt': 'Post image'})

    # Скачиваем новую картинку, если она обновилась
    if links_2:
        url_2 = links_2[0]['src']
        filename_2 = url_2.split('/')[-1].split('?')[0]
        if filename_2 not in loaded_images_2:
            loaded_images_2.append(filename_2)
            counter_2 += 1
            filepath_2 = f'images/{counter_2}.jpg'
            response_2 = requests.get(url_2, headers={'User-Agent': 'Mozilla/5.0'})
            with open(filepath_2, 'wb') as f:
                f.write(response_2.content)
            if counter_2 > 1:
                os.remove(os.path.join('images', f'1.jpg'))
            os.rename(filepath_2, os.path.join('images', f'1.jpg'))
            logging.info(f'Картинка {filename_2} загружена в папку images')
            with open(os.path.join('images', f'1.jpg'), 'rb') as photo:
                await bot.send_photo(chat_id=GROUP_ID, photo=photo, caption='[котики](t.me/catscatsmorecatss)',parse_mode='MarkdownV2')


async def scheduler():
    while True:
        await send_image_11()
        await asyncio.sleep(rnd.randint(2000, 3000))
        await send_image_2()
        await asyncio.sleep(rnd.randint(2000,3000 ))
        await send_image()
        await asyncio.sleep(rnd.randint(2000,3000))
        await send_image_meme()
        await asyncio.sleep(rnd.randint(2000, 3000))


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот, который будет отправлять новые фотографии котиков в группу @test_retranslate каждые 60 секунд. Для остановки бота нажмите /stop.")
    await Form.waiting.set()

# Обработчик команды /stop
@dp.message_handler(commands=['stop'])
async def cmd_stop(message: types.Message):
    await message.answer("Бот остановлен.")
    await asyncio.sleep(1)
    await bot.close()

# Запускаем бота
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())
    executor.start_polling(dp, skip_updates=True)
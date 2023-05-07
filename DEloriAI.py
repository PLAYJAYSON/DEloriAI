import aiogram as aio
import random as rnd
from module.Wiki.Wikipedia import getwiki
from module.RPS import RPS
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from module.YT.YT import yt_video_return,yt_video_search
from module.MultiUse import multiUseMod
phrase_tuple = ('Что бы это значило...', 'Извини, я тебя не понимаю...', 'Это что-то на непонятном, сори чел...', 'Умные мысли догоняли его, но он был быстрее...')
textTupleEcho1 = ('Райан Гослинг говорит:','Картман говорит:','Джамал сказал:','Никита Джигурда со стоном произносит:','Амогусы кричат:','Сол Гудман высказался:','Армяне кричат:')
textTupleEcho2 = ('а ты кусочек нежности','а ты купи покушать','а ты милашик','а ты вообще котик, а тебе вот это все не нужно ^3^','а ты взгляни на себя...Такой дурашка~','а ты такой пусичка')
textTupleClose = ('Не играем, получается...','Эхь...','Ну раз так...','Ладно, отдыхай~','Не хочешь, как хочешь!!! :Р','Прости, что я такая бесполезная...','Приходи снова)')
textTupleHelp = ('Помощь в студию!','Готова обеспечить всем необходимым)','Зачем несколько раз тыкать на эту кнопочку...','ПЕРЕСТАНЬ, здесь все есть','Молодой человек, ну сколько можно...','Тебе нравится тыкать кнопочки?','Выбери что-нибудь другое','Это уже абсурд какой-то...','Ты издеваешься, да?','Вот ещё ТОЧНО такая же информация~')

with open('privacy/TockenFile.txt','r') as tokenDEloriAI_file:
    thisDEloriAItoken  = tokenDEloriAI_file.read()

DEloriAI = aio.Bot(thisDEloriAItoken)
dp = aio.Dispatcher(DEloriAI)

rock = RPS.GameItem('Камень 🪨', 0, 2, 1)
paper = RPS.GameItem('Бумага 🧻', 1, 0, 2)
scissors = RPS.GameItem('Ножницы ✂️', 2, 1, 0)
handGame = RPS.handItem(rock, scissors, paper)


BTN_ROCK = InlineKeyboardButton('Камень 🪨',callback_data='Rock')
BTN_PAPER = InlineKeyboardButton('Бумага 🧻',callback_data='Paper')
BTN_SCISSORS = InlineKeyboardButton('Ножницы ✂️',callback_data='Scissors')
BTN_CLOSE = InlineKeyboardButton('Я усталь...', callback_data='RPSstop')
BTN_COMMANDS = InlineKeyboardButton('Летс гоу', callback_data='start')
BTN_COMMANDS_HELPER = InlineKeyboardButton('Помогите...', callback_data='help')
BTN_ECHO = InlineKeyboardButton('Игра \"Эхо\"',callback_data='echo')
BTN_ECHO_STOP = InlineKeyboardButton('Закончить этот цирк...', callback_data='echostop')
BTN_RPS = InlineKeyboardButton('Игра 🪨-✂️-🧻', callback_data='RPS')
BTN_WIKI = InlineKeyboardButton('Wikipedia', callback_data='wiki')
BTN_WIKI_STOP=InlineKeyboardButton('Я много узнал, на сегодня хватит...', callback_data='wikistop')
BTN_YT = InlineKeyboardButton('YouTube', callback_data='YT')
BTN_YT_STOP=InlineKeyboardButton('Я устал смотреть видосики, на сегодня хватит...', callback_data='YTstop')

RPS_KB = InlineKeyboardMarkup().add(BTN_ROCK,BTN_SCISSORS,BTN_PAPER,BTN_CLOSE)
GAME_KB = InlineKeyboardMarkup().add(BTN_COMMANDS_HELPER,BTN_ECHO,BTN_RPS,BTN_WIKI,BTN_YT)
START_KB = InlineKeyboardMarkup().add(BTN_COMMANDS)
ECHO_KB = InlineKeyboardMarkup().add(BTN_ECHO_STOP)
WIKI_KB = InlineKeyboardMarkup().add(BTN_WIKI_STOP)
YT_KB = InlineKeyboardMarkup().add(BTN_YT_STOP)

@dp.message_handler(commands=['start'])
async def process_start_command(message: aio.types.Message):
    multiUseMod.dirUser(message.from_user.id)
    await message.reply('Привет? Ты здесь? Я ДэлорИ, со мной не скучно)', reply_markup=START_KB)

@dp.message_handler(commands=['help'])
async def process_help_command(message: aio.types.Message):
    await message.reply('/help - команды\n/echo - ЭхоБот\n/RPS - 🪨-✂️-🧻')
@dp.callback_query_handler(text='start')
async def process_start_command(callback_query: aio.types.CallbackQuery):
    await DEloriAI.answer_callback_query(callback_query.id)
    await DEloriAI.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text='Вот полезные команды:',
        reply_markup=GAME_KB
    )
    '''await DEloriAI.send_message(callback_query.from_user.id,text='Вот полезные команды:',reply_markup=GAME_KB)
'''
@dp.callback_query_handler(text='help')
async def process_help_command(callback_query: aio.types.CallbackQuery):
    await DEloriAI.answer_callback_query(callback_query.id)
    await DEloriAI.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=rnd.choice(textTupleHelp),
        reply_markup=GAME_KB
    )
    '''await DEloriAI.send_message(callback_query.from_user.id,text='Помощь в студию:',reply_markup=GAME_KB)
'''
@dp.message_handler(commands=['echo'])
async def echo_bot(message:aio.types.Message):
    await message.reply('Играем в Эхо! Нажми /echostop если хочешь закончить)')
    with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_echo.txt', 'w') as flagEcho_file:
        flagEcho_file.write('True')
@dp.callback_query_handler(text='echo')
async def echo_bot(callback_query:aio.types.CallbackQuery):
    await DEloriAI.answer_callback_query(callback_query.id)
    await DEloriAI.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text='Играем в Эхо! Напиши что-нибудь',
        reply_markup=ECHO_KB
        )
    with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_echo.txt', 'w') as flagEcho_file:
        flagEcho_file.write('True')
@dp.message_handler(commands=['RPS'])
async def RPS_bot(message: aio.types.Message):
    await message.reply('Играем в Камень-Ножницы-Бумага!\n/Rock - 🪨\n/Paper - 🧻\n/Scissors - ✂️\nНажми /RPSstop если хочешь закончить)',reply_markup=RPS_KB)
    with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_RPS.txt', 'w') as flagRPS_file:
        flagRPS_file.write('True')
@dp.callback_query_handler(text='RPS')
async def RPS_bot(callback_query: aio.types.CallbackQuery):
    await DEloriAI.answer_callback_query(callback_query.id)
    await DEloriAI.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text='Играем в Камень-Ножницы-Бумагу',
        reply_markup=RPS_KB
    )
    with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_RPS.txt', 'w') as flagRPS_file:
        flagRPS_file.write('True')

@dp.message_handler(commands=['Rock'])
async def thisRock(message: aio.types.Message):
    with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_RPS.txt', 'r') as flagRPS_file:
        if flagRPS_file.read() == 'True':
            playerTurn = handGame.choise(thisPlayer=True, thisChoise=1)
            PCTurn = handGame.choise(thisPlayer=False, thisChoise=1)
            resultMSG = RPS.compareHand(playerTurn['Game_Item'],PCTurn['Game_Item'])
            await DEloriAI.send_message(
                message.from_user.id,
                text=f"{playerTurn['msg']}\n{PCTurn['msg']}\n{resultMSG}\n\n/Rock - 🪨\n/Paper - 🧻\n/Scissors - ✂️\nНажми /RPSstop если хочешь закончить",
                reply_markup=RPS_KB
            )

@dp.message_handler(commands=['Paper'])
async def thisPaper(message: aio.types.Message):
    with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_RPS.txt', 'r') as flagRPS_file:
        if flagRPS_file.read() == 'True':
            playerTurn = handGame.choise(thisPlayer=True, thisChoise=3)
            PCTurn = handGame.choise(thisPlayer=False, thisChoise=3)
            resultMSG = RPS.compareHand(playerTurn['Game_Item'], PCTurn['Game_Item'])
            await DEloriAI.send_message(
                message.from_user.id,
                text=f"{playerTurn['msg']}\n{PCTurn['msg']}\n{resultMSG}\n\n/Rock - 🪨\n/Paper - 🧻\n/Scissors - ✂️\nНажми /RPSstop если хочешь закончить",
                reply_markup=RPS_KB
            )


@dp.message_handler(commands=['Scissors'])
async def thisScisors(message: aio.types.Message):
    with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_RPS.txt', 'r') as flagRPS_file:
        if flagRPS_file.read() == 'True':
            playerTurn = handGame.choise(thisPlayer=True, thisChoise=2)
            PCTurn = handGame.choise(thisPlayer=False, thisChoise=2)
            resultMSG = RPS.compareHand(playerTurn['Game_Item'], PCTurn['Game_Item'])
            await DEloriAI.send_message(
                message.from_user.id,
                text=f"{playerTurn['msg']}\n{PCTurn['msg']}\n{resultMSG}\n\n/Rock - 🪨\n/Paper - 🧻\n/Scissors - ✂️\nНажми /RPSstop если хочешь закончить",
                reply_markup=RPS_KB
            )

@dp.callback_query_handler(text='Rock')
async def thisRock(callback_query: aio.types.CallbackQuery):
    with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_RPS.txt', 'r') as flagRPS_file:
        if flagRPS_file.read() == 'True':
            playerTurn = handGame.choise(thisPlayer=True, thisChoise=1)
            PCTurn = handGame.choise(thisPlayer=False, thisChoise=1)
            resultMSG = RPS.compareHand(playerTurn['Game_Item'],PCTurn['Game_Item'])
            await DEloriAI.answer_callback_query(callback_query.id)
            await DEloriAI.edit_message_text(
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                text=f"{playerTurn['msg']}\n{PCTurn['msg']}\n{resultMSG}\n",
                reply_markup=RPS_KB
            )

@dp.callback_query_handler(text='Paper')
async def thisPaper(callback_query: aio.types.CallbackQuery):
    with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_RPS.txt', 'r') as flagRPS_file:
        if flagRPS_file.read() == 'True':
            playerTurn = handGame.choise(thisPlayer=True, thisChoise=3)
            PCTurn = handGame.choise(thisPlayer=False, thisChoise=3)
            resultMSG = RPS.compareHand(playerTurn['Game_Item'],PCTurn['Game_Item'])
            await DEloriAI.answer_callback_query(callback_query.id)
            await DEloriAI.edit_message_text(
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                text=f"{playerTurn['msg']}\n{PCTurn['msg']}\n{resultMSG}\n",
                reply_markup=RPS_KB
            )


@dp.callback_query_handler(text='Scissors')
async def thisScissors(callback_query: aio.types.CallbackQuery):
    with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_RPS.txt', 'r') as flagRPS_file:
        if flagRPS_file.read() == 'True':
            playerTurn = handGame.choise(thisPlayer=True, thisChoise=2)
            PCTurn = handGame.choise(thisPlayer=False, thisChoise=2)
            resultMSG = RPS.compareHand(playerTurn['Game_Item'],PCTurn['Game_Item'])
            await DEloriAI.answer_callback_query(callback_query.id)
            await DEloriAI.edit_message_text(
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                text=f"{playerTurn['msg']}\n{PCTurn['msg']}\n{resultMSG}",
                reply_markup=RPS_KB
            )
@dp.callback_query_handler(text='RPSstop')
async def Stopper(callback_query: aio.types.CallbackQuery):
    with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_RPS.txt', 'r') as flagRPS_file:
        if flagRPS_file.read() == 'True':
            await DEloriAI.answer_callback_query(callback_query.id)
            await DEloriAI.edit_message_text(
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                text=rnd.choice(textTupleClose),
                reply_markup=GAME_KB
            )
            with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_RPS.txt', 'w') as flagRPS_file:
                flagRPS_file.write('False')
        elif flagRPS_file.read() == 'False':
            await DEloriAI.answer_callback_query(callback_query.id)
            await DEloriAI.send_message(callback_query.from_user.id, text=rnd.choice(phrase_tuple))
@dp.callback_query_handler(text='echostop')
async def Stopper(callback_query: aio.types.CallbackQuery):
    with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_echo.txt', 'r') as flagEcho_file:
        if flagEcho_file.read() == 'True':
            await DEloriAI.answer_callback_query(callback_query.id)
            await DEloriAI.edit_message_text(
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                text=rnd.choice(textTupleClose),
                reply_markup=GAME_KB
            )

            with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_echo.txt', 'w') as flagEcho_file:
                flagEcho_file.write('False')
        elif flagEcho_file.read() == 'False':
            await DEloriAI.answer_callback_query(callback_query.id)
            await DEloriAI.send_message(callback_query.from_user.id, text=rnd.choice(phrase_tuple))
@dp.callback_query_handler(text='YT')
async def YT_bot(callback_query:aio.types.CallbackQuery):
    await DEloriAI.answer_callback_query(callback_query.id)
    await DEloriAI.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text='Мини-ютубчик\nНапиши, что хочешь посмотреть)',
        reply_markup=YT_KB
        )
    with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_YT.txt', 'w') as flagYT_file:
        flagYT_file.write('True')

@dp.callback_query_handler(text='YTstop')
async def YTStopper(callback_query: aio.types.CallbackQuery):
    with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_YT.txt', 'r') as flagYT_file:
        if flagYT_file.read() == 'True':

            await DEloriAI.answer_callback_query(callback_query.id)
            await DEloriAI.edit_message_text(
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                text=rnd.choice(textTupleClose),
                reply_markup=GAME_KB
            )

            with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_YT.txt',
                      'w') as flagYT_file:
                flagYT_file.write('False')
        elif flagYT_file.read() == 'False':
            await DEloriAI.answer_callback_query(callback_query.id)
            await DEloriAI.send_message(callback_query.from_user.id, text=rnd.choice(phrase_tuple))


@dp.callback_query_handler(text='wiki')
async def echo_bot(callback_query:aio.types.CallbackQuery):
    await DEloriAI.answer_callback_query(callback_query.id)
    await DEloriAI.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text='Мини-википедия\nНапиши, что хочешь узнать.',
        reply_markup=WIKI_KB
        )
    with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_wiki.txt','w') as flagWiki_file:
        flagWiki_file.write('True')
@dp.callback_query_handler(text='wikistop')
async def Stopper(callback_query: aio.types.CallbackQuery):
    with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_wiki.txt', 'r') as flagWiki_file:
        if flagWiki_file.read() == 'True':
            await DEloriAI.answer_callback_query(callback_query.id)
            await DEloriAI.edit_message_text(
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                text=rnd.choice(textTupleClose),
                reply_markup=GAME_KB
            )
            with open(f'cache/multiUse/Users/{str(callback_query.from_user.id)}/cache/flag_wiki.txt', 'w') as flagWiki_file:
                flagWiki_file.write('False')
        elif flagWiki_file.read() == 'False':
            await DEloriAI.answer_callback_query(callback_query.id)
            await DEloriAI.send_message(callback_query.from_user.id, text=rnd.choice(phrase_tuple))



@dp.message_handler()
async def get_text_from_messages(message: aio.types.Message):
    with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_echo.txt', 'r') as flagEcho_file:
        with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_RPS.txt', 'r') as flagRPS_file:
            with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_YT.txt', 'r') as flagYT_file:
                with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_wiki.txt', 'r') as flagWiki_file:
                    if flagRPS_file.read() == 'False' and flagWiki_file.read() == 'False' and flagYT_file.read() == 'False':
                        if flagEcho_file.read() == 'True':
                            if message.text != '/echostop':
                                await DEloriAI.send_message(
                                    message.from_user.id,
                                    f'{rnd.choice(textTupleEcho1)} \"{message.text}\",'
                                    f' {rnd.choice(textTupleEcho2)}',
                                    reply_markup=ECHO_KB
                                )

                            elif message.text == '/echostop':
                                await DEloriAI.send_message(
                                    message.from_user.id,
                                    f'{rnd.choice(phrase_tuple)}'
                                )

                        elif flagEcho_file.read() == 'True':

                            await message.reply(rnd.choice(phrase_tuple))
                            with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_echo.txt',
                                      'w') as flagEcho_file:
                                flagEcho_file.write('False')
                    elif flagRPS_file.read() == 'False' and flagEcho_file.read() == 'False' and flagYT_file.read()== 'False':
                        if flagWiki_file.read() == 'True':
                            if message.text != '/wikistop':
                                await DEloriAI.send_message(
                                    message.from_user.id,
                                    getwiki(message),
                                    reply_markup=WIKI_KB
                                )

                            elif message.text == '/wikistop':
                                await DEloriAI.send_message(
                                    message.from_user.id,
                                    f'{rnd.choice(phrase_tuple)}'
                                )

                        elif flagWiki_file.read() == 'False':

                            await message.reply(rnd.choice(phrase_tuple))
                            with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_wiki.txt',
                                  'w') as flagWiki_file:
                                flagWiki_file.write('False')
                    elif flagRPS_file.read() == 'False' and flagEcho_file.read() == 'False' and flagWiki_file.read() == 'False':
                        if flagYT_file.read() == 'True':
                            if message.text != '/YTstop':
                                myKW = message.text
                                myIdList = yt_video_search(myKW)
                                myLinkList = yt_video_return(myIdList)
                                for i in myLinkList:
                                    await DEloriAI.send_message(message.from_user.id, text=i, reply_markup=YT_KB)

                            elif message.text == '/YTstop':
                                await DEloriAI.send_message(
                                    message.from_user.id,
                                    f'{rnd.choice(phrase_tuple)}'
                                )

                        elif flagYT_file.read() == 'False':

                            await message.reply(rnd.choice(phrase_tuple))
                            with open(f'cache/multiUse/Users/{str(message.from_user.id)}/cache/flag_YT.txt',
                                      'w') as flagYT_file:
                                flagYT_file.write('False')
aio.executor.start_polling(dp)

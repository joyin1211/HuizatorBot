from aiogram import Bot, Dispatcher, executor, types
import config
from huizing import huizator

# Initialize bot and dispatcher

bot = Bot(token=config.TOKEN)

dp = Dispatcher(bot)

doAnswer = True

helpText = "/start - начать работу\n" \
           "/help - ты конч??? Как попал сюда вообще по твоему\n" \
           "/mode + 0/1 - убрать/установить спам мод (ответ на все сообщения)\n" \
           "/huizator + аргумент - хуизировать фразу в ответ которой идёт сообщение. Аргумент - " \
           "шанс хуизирования слова во всей фразе (можно не указывать, по умолчанию - 100)\n" \
           "Приятного хуизирования!"


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('хуи)))\n'
                        '/help - ГДЕ ПООООООООООМОЩЬ; ВОТ ПОООООООООМОЩЬ')


@dp.message_handler(commands=['help'])
async def cats(message: types.Message):
    global helpText
    await message.reply(helpText)


@dp.message_handler(commands=['mode'])
async def setmode(message: types.Message):
    global doAnswer
    msg = message
    txt = ' '.join((msg.text.split())[1:])
    if txt == '0':
        doAnswer = False
        await msg.reply("Теперь этот хуесос перестанет спамить!")
    elif txt == '1':
        doAnswer = True
        await msg.reply("Вам пизда парни))))))))))")
    else:
        await msg.reply("И чё ты высрал?")


@dp.message_handler(commands=['huizator'])
async def realAnsw(message=types.Message):
    msg = message
    txt = ' '.join((msg.text.split())[1:])
    replyToMessage = msg.reply_to_message
    if replyToMessage:
        print(txt)
        chance = 100
        if txt:
            if txt.isdigit():
                if 100 >= int(txt) >= 0:
                    chance = int(txt)
        print(chance)
        result = huizator(replyToMessage.text, chance)
        await msg.reply(result)
    else:
        await msg.reply("Насрал бро")


@dp.message_handler()
async def answer(message: types.Message):
    if doAnswer:
        msg = message
        result = huizator(msg.text)
        await msg.reply(result)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

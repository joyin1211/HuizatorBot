import logging

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import config
from huizing import huizator

# Enable logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    level=logging.INFO)

# logger = logging.getLogger(__name__)

doAnswer = True

helpText = "/start - начать работу\n" \
           "/help - ты конч??? Как попал сюда вообще по твоему\n" \
           "/mode + 0/1 - убрать/установить спам мод (ответ на все сообщения)\n" \
           "/huizator + аргумент - хуизировать фразу в ответ которой идёт сообщение. Аргумент - " \
           "шанс хуизирования слова во всей фразе (можно не указывать, по умолчанию - 100)\n" \
           "Приятного хуизирования!"


def start(update: telegram.Update, context):
    update.message.reply_text('хуи)))\n'
                              '/help - ГДЕ ПООООООООООМОЩЬ; ВОТ ПОООООООООМОЩЬ')


def help(update: telegram.Update, context):
    global helpText
    update.message.reply_text(helpText)


def setmode(update: telegram.Update, context):
    global doAnswer
    msg = update.message
    txt = ' '.join((msg.text.split())[1:])
    if txt == '0':
        doAnswer = False
        msg.reply_text("Теперь этот хуесос перестанет спамить!")
    elif txt == '1':
        doAnswer = True
        msg.reply_text("Вам пизда парни))))))))))")
    else:
        msg.reply_text("И чё ты высрал?")


def answer(update: telegram.Update, context):
    if doAnswer:
        msg: telegram.Message = update.message
        result = huizator(msg.text)
        msg.reply_text(result)


def realAnsw(update: telegram.Update, context):
    msg = update.message
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
        msg.reply_text(result)
    else:
        msg.reply_text("Насрал бро")


def main():
    updater = Updater(config.TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("mode", setmode))
    dp.add_handler(CommandHandler("huizator", realAnsw))

    dp.add_handler(MessageHandler(Filters.text, answer))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

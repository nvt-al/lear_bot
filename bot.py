import logging    # логирование. сохранение ошибок
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import setting

# более подробные логи
# logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)

logging.basicConfig(filename='bot.log', level=logging.INFO)    # место сохранения, уровень важности 


def greet_user(update, context):
    print('Вызван /start')    # ответ пользователю на команду /start
    
    
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')    
    # print(update)    

def talk_to_me(update, context):    #функция, отвечающая пользователю 
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(setting.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))    # обработчик информации(онли текст)

    logging.info("Бот стартовал")
    mybot.start_polling()    # регулярные обновления и запросы на сервер 
    mybot.idle()             # бесконечный цикл запросов
if __name__ == "__main__":    
    main()
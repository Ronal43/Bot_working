#coding:utf-8
import telebot, config
from telebot import types
import time
import os

knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
              'start': 'Get used to the bot',
              'help': 'Gives you information about the available commands',
              'sendLongText': 'A test using the \'send_chat_action\' command',
              'getImage': 'A test using multi-stage messages, custom keyboard, and media sending'
}


bot=telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def handle_text(message): 
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Получить мамбу Киев') 
    user_markup.row('Получить вк Киев')
    user_markup.row('Получить мамбу МСК') 
    user_markup.row('Получить вк МСК')
    bot.send_message(message.from_user.id, 'Нажми на кнопку', reply_markup=user_markup)

@bot.message_handler(commands=["help"]) 
def start(message):
    bot.send_message(message.chat.id, 'Попросите у меня Вк, и я дам его вам, попросите Мамбу, и я тоже ее вам дам.\nНо не просите у меня кушать:)(все, кто попросит - покушают пиздюлей)')

@bot.message_handler(commands=["dai_mambu"])
def start(message):
    bot.send_message(message.chat.id, "Держи {-Variable.MAMBA-}")



@bot.message_handler(func=lambda message: message.text == "Получить мамбу МСК")
def handle_text(message):
    user_markup.row('1')
    user_markup.row('2')
    user_markup.row('3')
    user_markup.row('4')
    user_markup.row('5')
    bot.send_message(message.chat.id, "Сколько?")
      @bot.message_handler(func=lambda message: message.text == "1"
      def command_text_hi(m):
          f = open('mamba.txt', 'r+')
          s = (f.read())
          a = s.split('\n')
          print (a)
          f.close()
          mamba = a.pop (0)
          bot.send_message(m.chat.id, 'Держи: \n '+mamba)
          bot.send_message(m.chat.id, 'Работай хорошо, тогда у тебя всегда будут свежие и красивые аккаунты;)')
          del a[-1]
          print (mamba)
          print (a)
          f = open('mamba.txt', 'w')
          for index in a:
              f.write(index + '\n')
          f.close
          f = open('mamba.txt', 'r+')
          s = (f.read())
          a = s.split('\n')
          print (a)
          f.close()
    
@bot.message_handler(func=lambda message: message.text == "Получить вк") 
def command_text_hi(m):
    f = open('vk.txt', 'r+')
    s = (f.read())
    a = s.split('\n')
    print (a)
    f.close()
    vk = a.pop (0)
    del a[-1]
    bot.send_message(m.chat.id, 'Лови:) \n' +vk)
    bot.send_message(m.chat.id, 'Работай хорошо, тогда у тебя всегда будут свежие и красивые аккаунты;)')
    print (vk)
    print (a)
    f = open('vk.txt', 'w')
    for index in a:
        f.write(index + '\n')
    f.close
    f = open('vk.txt', 'r+')
    s = (f.read())
    a = s.split('\n')
    print (a)
    f.close()

if __name__=="__main__":
    bot.polling()

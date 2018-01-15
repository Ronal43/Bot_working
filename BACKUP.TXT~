#coding:utf-8
import telebot, config
from telebot import types
import datetime
from datetime import datetime 
import os
import sys
import subprocess
import string
import re

knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts


def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        return 0



def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            date = datetime.now(tz=None)
            print ("{" + str(date) +"} " + str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)
            spisok = ["{" + str(date) +"} " + str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text]
            filename=m.chat.first_name + m.chat.last_name +'.txt'
            spisok2 = open(filename, 'a')
            for index in spisok:
                spisok2.write(index + '\n')
            spisok2.close


bot=telebot.TeleBot(config.TOKEN)
bot.set_update_listener(listener)

def main():
    @bot.message_handler(commands=["start"])
    def handle_text(message): 
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        #user_markup.row('Получить мамбу Киев') 
        #user_markup.row('Получить вк Киев')
        user_markup.row('Получить мамбу МСК') 
        user_markup.row('Получить вк МСК')
        user_markup.row('Тебе скучно и одиноко?')
        bot.send_message(message.from_user.id, 'Что привело тебя в столь темное место, красавица?', reply_markup=user_markup)


    @bot.message_handler(func=lambda message: message.text == "Тебе скучно и одиноко?")
    def handle_text(message): 
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('На главную')
        bot.send_message(message.from_user.id, 'Иди ко мне, сладкая...')
        bot.send_photo(message.from_user.id, open('1408564055_895357073.jpg', 'rb'))
        

    @bot.message_handler(commands=["help"]) 
    def start(message):
        bot.send_message(message.chat.id, 'Попросите у меня Вк, и я дам его вам, попросите Мамбу, и я тоже ее вам дам.\nНо не просите у меня кушать:)(все, кто попросит - покушают пиздюлей)')

    @bot.message_handler(func=lambda message: message.text == "На главную")
    def handle_text(message): 
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        #user_markup.row('Получить мамбу Киев') 
        #user_markup.row('Получить вк Киев')
        user_markup.row('Получить мамбу МСК') 
        user_markup.row('Получить вк МСК')
        user_markup.row('Тебе скучно и одиноко?')
        bot.send_message(message.from_user.id, 'Чего надобно, старче?', reply_markup=user_markup)

    @bot.message_handler(func=lambda message: message.text == "Получить мамбу МСК")
    def handle_text(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Одну')
        user_markup.row('Две')
        user_markup.row('Три')
        user_markup.row('Четыре')
        user_markup.row('Пять')
        user_markup.row('На главную')
        bot.send_message(message.chat.id, "Сколько?", reply_markup=user_markup)
        @bot.message_handler(func=lambda message: message.text == "Одну")
        def command_text_hi(m):
                f = open('mamba.txt', 'r+')
                s = (f.read())
                a = s.split('\n')
                print (a)
                f.close()
                mamba = a.pop (0)
                del a[0]
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('На главную')
                bot.send_message(m.chat.id, 'Держи: \n '+mamba, reply_markup=user_markup)
                bot.send_message(m.chat.id, 'Работай хорошо, тогда у тебя всегда будут свежие и красивые аккаунты;)')
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
        @bot.message_handler(func=lambda message: message.text == "Две")
        def command_text_hi(m):
                f = open('mamba.txt', 'r+')
                s = (f.read())
                a = s.split('\n')
                print (a)
                f.close()
                mamba = a.pop (0)
                del a[0]
                mamba1 = a.pop (0)
                del a[0]
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('На главную')
                bot.send_message(m.chat.id, 'Держи: \n '+mamba)
                bot.send_message(m.chat.id, mamba1, reply_markup=user_markup)
                print (mamba)
                print (mamba1)
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
        @bot.message_handler(func=lambda message: message.text == "Три")
        def command_text_hi(m):
                f = open('mamba.txt', 'r+')
                s = (f.read())
                a = s.split('\n')
                print (a)
                f.close()
                mamba = a.pop (0)
                del a[0]
                mamba1 = a.pop (0)
                del a[0]
                mamba2 = a.pop (0)
                del a[0]
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('На главную')
                bot.send_message(m.chat.id, 'Это уже дело)) \n '+mamba)
                bot.send_message(m.chat.id, mamba1)
                bot.send_message(m.chat.id, mamba2, reply_markup=user_markup)
                print (mamba)
                print (mamba1)
                print (mamba2)
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
        @bot.message_handler(func=lambda message: message.text == "Четыре")
        def command_text_hi(m):
                f = open('mamba.txt', 'r+')
                s = (f.read())
                a = s.split('\n')
                print (a)
                f.close()
                mamba = a.pop (0)
                del a[0]  
                mamba1 = a.pop (0)
                del a[0]
                mamba2 = a.pop (0)
                del a[0]
                mamba3 = a.pop (0)
                del a[0]
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('На главную')
                bot.send_message(m.chat.id, 'Это сильно)) \n '+mamba)
                bot.send_message(m.chat.id, mamba1)
                bot.send_message(m.chat.id, mamba2)
                bot.send_message(m.chat.id, mamba3, reply_markup=user_markup)
                print (mamba)
                print (mamba1)
                print (mamba2)
                print (mamba3)
                print (a)
                f = open('mamba.txt', 'w')
                for index in a:
                      f.write(index + '\n')
                f.close
                f = open('mamba.txt', 'r+')
                s = (f.read())
                A = s.split('\n')
                print (a)
                f.close()
        @bot.message_handler(func=lambda message: message.text == "Пять")
        def command_text_hi(m):
                f = open('mamba.txt', 'r+')
                s = (f.read())
                a = s.split('\n')
                print (a)
                f.close()
                mamba = a.pop (0)
                del a[0]  
                mamba1 = a.pop (0)
                del a[0]
                mamba2 = a.pop (0)
                del a[0]
                mamba3 = a.pop (0)
                del a[0]
                mamba4 = a.pop (0)
                del a[0]
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('На главную')
                bot.send_message(m.chat.id, 'Ну, если ты справишься с ними... \n '+mamba)
                bot.send_message(m.chat.id, mamba1)
                bot.send_message(m.chat.id, mamba2)
                bot.send_message(m.chat.id, mamba3)
                bot.send_message(m.chat.id, mamba4, reply_markup=user_markup)
                print (mamba)
                print (mamba1)
                print (mamba2)
                print (mamba3)
                print (mamba4)
                print (a)
                f = open('mamba.txt', 'w')
                for index in a:
                      f.write(index + '\n')
                f.close
                f = open('mamba.txt', 'r+')
                s = (f.read())
                A = s.split('\n')
                print (a)
                f.close()


    @bot.message_handler(func=lambda message: message.text == "Получить вк МСК") 
    def handle_text(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('1')
        user_markup.row('2')
        user_markup.row('3')
        user_markup.row('4')
        user_markup.row('5')
        user_markup.row('На главную')
        bot.send_message(message.chat.id, "Сколько?", reply_markup=user_markup)
        @bot.message_handler(func=lambda message: message.text == "1")
        def command_text_hi(m):
              vkmsk = open('vk.txt', 'r+')
              svkmsk = (vkmsk.read())
              vkmsk_list = svkmsk.split('\n')
              print (vkmsk_list)
              vkmsk.close()
              vk = vkmsk_list.pop (0)
              del vkmsk_list[0]
              user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
              user_markup.row('На главную')
              bot.send_message(m.chat.id, 'Лови:) \n' +vk)
              bot.send_message(m.chat.id, 'Нужно будет еще что-нибудь - приходи.', reply_markup=user_markup)
              print (vk)
              print (vkmsk_list)
              vkmsk = open('vk.txt', 'w')
              for index in vkmsk_list:
                    vkmsk.write(index + '\n')
              vkmsk.close
              vkmsk = open('vk.txt', 'r+')
              svkmsk = (vkmsk.read())
              vkmsk_list = svkmsk.split('\n')
              print (vkmsk_list)
              vkmsk.close()
        @bot.message_handler(func=lambda message: message.text == "2")
        def command_text_hi(m):
              vkmsk = open('vk.txt', 'r+')
              svkmsk = (vkmsk.read())
              vkmsk_list = svkmsk.split('\n')
              print (vkmsk_list)
              vkmsk.close()
              vk = vkmsk_list.pop (0)
              del vkmsk_list[0]
              vk1 = vkmsk_list.pop (0)
              del vkmsk_list[0]
              user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
              user_markup.row('На главную')
              bot.send_message(m.chat.id, 'Ну, два так два. Мне не жалко...\n' +vk)
              bot.send_message(m.chat.id, vk1,reply_markup=user_markup)
              print (vk+' '+vk1)
              print (vkmsk_list)
              vkmsk = open('vk.txt', 'w')
              for index in vkmsk_list:
                    vkmsk.write(index + '\n')
              vkmsk.close
              vkmsk = open('vk.txt', 'r+')
              svkmsk = (vkmsk.read())
              vkmsk_list = svkmsk.split('\n')
              print (vkmsk_list)
              vkmsk.close()
        @bot.message_handler(func=lambda message: message.text == "3")
        def command_text_hi(m):
              vkmsk = open('vk.txt', 'r+')
              svkmsk = (vkmsk.read())
              vkmsk_list = svkmsk.split('\n')
              print (vkmsk_list)
              vkmsk.close()
              vk = vkmsk_list.pop (0)
              del vkmsk_list[0]
              vk1 = vkmsk_list.pop (0)
              del vkmsk_list[0]
              vk2 = vkmsk_list.pop (0)
              del vkmsk_list[0]
              user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
              user_markup.row('На главную')
              bot.send_message(m.chat.id, 'О, мастер своего дела?;) \n' +vk)
              bot.send_message(m.chat.id, vk1)
              bot.send_message(m.chat.id, vk2, reply_markup=user_markup)
              print (vk+' '+vk1+' '+vk2)
              print (vkmsk_list)
              vkmsk = open('vk.txt', 'w')
              for index in vkmsk_list:
                    vkmsk.write(index + '\n')
              vkmsk.close
              vkmsk = open('vk.txt', 'r+')
              svkmsk = (vkmsk.read())
              vkmsk_list = svkmsk.split('\n')
              print (vkmsk_list)
              vkmsk.close()
        @bot.message_handler(func=lambda message: message.text == "4")
        def command_text_hi(m):
              vkmsk = open('vk.txt', 'r+')
              svkmsk = (vkmsk.read())
              vkmsk_list = svkmsk.split('\n')
              print (vkmsk_list)
              vkmsk.close()
              vk = vkmsk_list.pop (0)
              del vkmsk_list[0]
              vk1 = vkmsk_list.pop (0)
              del vkmsk_list[0]
              vk2 = vkmsk_list.pop (0)
              del vkmsk_list[0]
              vk3 = vkmsk_list.pop (0)
              del vkmsk_list[0]
              user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
              user_markup.row('На главную')
              bot.send_message(m.chat.id, 'Ну, раз так хочешь... \n' +vk)
              bot.send_message(m.chat.id, vk1)
              bot.send_message(m.chat.id, vk2)
              bot.send_message(m.chat.id, vk3, reply_markup=user_markup)
              print (vk+" "+vk1+" "+vk2+" "+vk3)
              print (vkmsk_list)
              vkmsk = open('vk.txt', 'w')
              for index in vkmsk_list:
                    vkmsk.write(index + '\n')
              vkmsk.close
              vkmsk = open('vk.txt', 'r+')
              svkmsk = (vkmsk.read())
              vkmsk_list = svkmsk.split('\n')
              print (vkmsk_list)
              vkmsk.close()
        @bot.message_handler(func=lambda message: message.text == "5")
        def command_text_hi(m):
              vkmsk = open('vk.txt', 'r+')
              svkmsk = (vkmsk.read())
              vkmsk_list = svkmsk.split('\n')
              print (vkmsk_list)
              vkmsk.close()
              vk = vkmsk_list.pop (0)
              del vkmsk_list[0]
              vk1 = vkmsk_list.pop (0)
              del vkmsk_list[0]
              vk2 = vkmsk_list.pop (0)
              del vkmsk_list[0]
              vk3 = vkmsk_list.pop (0)
              del vkmsk_list[0]
              vk4 = vkmsk_list.pop (0)
              del vkmsk_list[0]
              user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
              user_markup.row('На главную')
              bot.send_message(m.chat.id, 'Ого, а сравишься?) \n' +vk)
              bot.send_message(m.chat.id, vk1)
              bot.send_message(m.chat.id, vk2)
              bot.send_message(m.chat.id, vk3)
              bot.send_message(m.chat.id, vk4, reply_markup=user_markup)
              print (vk+' '+vk1+' '+vk2+' '+vk3+' '+vk4)
              print (vkmsk_list)
              vkmsk = open('vk.txt', 'w')
              for index in vkmsk_list:
                    vkmsk.write(index + '\n')
              vkmsk.close
              vkmsk = open('vk.txt', 'r+')
              svkmsk = (vkmsk.read())
              vkmsk_list = svkmsk.split('\n')
              print (vkmsk_list)
              vkmsk.close()


    if __name__=="__main__":
        bot.polling()

if __name__=="__main__":
        main()

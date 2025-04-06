import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json
import os
from localization import Localization

TOKEN = '7504532103:AAGHjCUVbe6wktF7Ym2zCMKJz1fdMOKISrQ'
bot = telebot.TeleBot(TOKEN)

LANG_FILE = 'user_lang.json'
ORDER_FILE = 'orders.json'

# 🧠 User languages
def load_user_lang():
    if os.path.exists(LANG_FILE):
        with open(LANG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_user_lang(data):
    with open(LANG_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f)

user_langs = load_user_lang()

# 🌐 Localized loader
def get_localized(user_id):
    lang = user_langs.get(str(user_id), 'uz')
    return Localization(lang)

# 🚀 START
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("🇺🇿 O'zbekcha", "🇷🇺 Русский", "🇬🇧 English")
    bot.send_message(message.chat.id, "Tilni tanlang / Choose language / Выберите язык:", reply_markup=markup)

# 🌐 Language selection
@bot.message_handler(func=lambda m: m.text in ["🇺🇿 O'zbekcha", "🇷🇺 Русский", "🇬🇧 English"])
def language_selected(message):
    user_id = str(message.from_user.id)
    user_langs[user_id] = (
        "uz" if "O'zbekcha" in message.text else
        "ru" if "Русский" in message.text else
        "en"
    )
    save_user_lang(user_langs)
    l10n = get_localized(user_id)
    bot.send_message(message.chat.id, l10n.t("welcome"))
    bot.send_message(message.chat.id, l10n.t("order_now"))

# 📦 Buyurtma bosqichlari
user_steps = {}

@bot.message_handler(commands=['order'])
def start_order(message):
    user_id = str(message.from_user.id)
    l10n = get_localized(user_id)
    user_steps[user_id] = {'step': 'name', 'data': {}}
    bot.send_message(message.chat.id, l10n.t("enter_name"))

@bot.message_handler(func=lambda m: True)
def handle_order_steps(message):
    user_id = str(message.from_user.id)
    if user_id not in user_steps:
        return

    l10n = get_localized(user_id)
    step_info = user_steps[user_id]

    if step_info['step'] == 'name':
        step_info['data']['name'] = message.text
        step_info['step'] = 'phone'
        bot.send_message(message.chat.id, l10n.t("enter_phone"))

    elif step_info['step'] == 'phone':
        step_info['data']['phone'] = message.text
        step_info['step'] = 'service'
        bot.send_message(message.chat.id, l10n.t("enter_service"))

    elif step_info['step'] == 'service':
        step_info['data']['service'] = message.text
        order = step_info['data']
        save_order(user_id, order)
        bot.send_message(
            message.chat.id,
            l10n.t("order_saved").format(
                name=order['name'], phone=order['phone'], service=order['service']
            )
        )
        del user_steps[user_id]

# 📁 Buyurtmalarni saqlash
def save_order(user_id, order):
    if os.path.exists(ORDER_FILE):
        with open(ORDER_FILE, 'r', encoding='utf-8') as f:
            orders = json.load(f)
    else:
        orders = {}

    orders[user_id] = order
    with open(ORDER_FILE, 'w', encoding='utf-8') as f:
        json.dump(orders, f, indent=2)

bot.polling()

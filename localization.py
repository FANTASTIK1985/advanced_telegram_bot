# localization.py

class Localization:
    def __init__(self, lang):
        self.lang = lang
        self.translations = {
            'uz': {
                'welcome': "Xush kelibsiz!",
                'order_now': "Buyurtma berishni boshlash uchun /order ni bosing.",
                'enter_name': "Ismingizni kiriting:",
                'enter_phone': "Telefon raqamingizni kiriting:",
                'enter_service': "Qaysi xizmatdan foydalanmoqchisiz?",
                'order_saved': "Buyurtmangiz saqlandi:\nIsm: {name}\nTel: {phone}\nXizmat: {service}",
            },
            'ru': {
                'welcome': "Добро пожаловать!",
                'order_now': "Чтобы начать заказ, нажмите /order.",
                'enter_name': "Введите ваше имя:",
                'enter_phone': "Введите номер телефона:",
                'enter_service': "Какие услуги вы хотите?",
                'order_saved': "Ваш заказ сохранён:\nИмя: {name}\nТел: {phone}\nУслуга: {service}",
            },
            'en': {
                'welcome': "Welcome!",
                'order_now': "To place an order, type /order.",
                'enter_name': "Please enter your name:",
                'enter_phone': "Please enter your phone number:",
                'enter_service': "Which service do you want?",
                'order_saved': "Your order has been saved:\nName: {name}\nPhone: {phone}\nService: {service}",
            }
        }

    def t(self, key):
        return self.translations.get(self.lang, {}).get(key, key)

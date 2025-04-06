import json
import os

class Localization:
    def __init__(self, lang='uz'):
        self.lang = lang
        self.translations = self.load_language(lang)

    def load_language(self, lang):
        """Til faylini yuklash."""
        try:
            # Til faylini yuklash
            with open(os.path.join('locales', f'{lang}.json'), 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # Fayl topilmasa, xatolik xabarini chiqarish
            print(f"Til fayli {lang}.json topilmadi! Standart tilga o'ting.")
            # Standart tilga o'tish (masalan, o'zbekcha)
            return self.load_language('uz')
        except json.JSONDecodeError:
            # Fayl noto'g'ri formatda bo'lsa
            print(f"{lang}.json fayli formatda xatolik bor!")
            return {}

    def set_language(self, lang):
        """Yangi tilni o'rnatish."""
        self.lang = lang
        self.translations = self.load_language(lang)

    def t(self, key):
        """Xabarni tarjima qilish."""
        return self.translations.get(key, key)

# Test qilish uchun, misol:
localizer = Localization('en')  # Default til - inglizcha

print(localizer.t('welcome'))  # welcome xabarini chiqaradi

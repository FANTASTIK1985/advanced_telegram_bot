import json
import os

# Lokalizatsiyalarni o'qish
class Localization:
    def __init__(self, lang='uz'):
        self.lang = lang
        self.translations = self.load_language(lang)

    def load_language(self, lang):
        try:
            with open(os.path.join('locales', f'{lang}.json'), 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Language file {lang}.json not found!")
            return {}

    def set_language(self, lang):
        self.lang = lang
        self.translations = self.load_language(lang)

    def t(self, key):
        return self.translations.get(key, key)

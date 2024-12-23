from translate import Translator
import requests
from collections import defaultdict

# Задание №5
qwestions = {'как тебя зовут' : "Я супер-крутой-бот и мое ппредназначение помогать тебе!",
             "сколько тебе лет" : "Это слишком философский вопрос"}
class TextAnalysis():   
    
    # Задание №1
    memory = defaultdict(list)
    def __init__(self, text, owner):

        # Задание №2
        TextAnalysis.memory[owner].append(self)
        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

        # Задание №6
        self.response = self.get_answer()
        
    
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            # Задание №4
            translator = Translator(from_lang='en', to_lang='ru')
            translation = translator.translate(text)
        except:
            return "Перевод не удался"



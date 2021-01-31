from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

english_bot = ChatBot("ChatterBot", storage_adapter= "chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

while True:
    request = input("You: ")
    response = english_bot.get_response(request)
    print('Bot: ', response)

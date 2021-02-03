from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

english_bot = ChatBot("ChatterBot", storage_adapter= "chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

"""
    Sample Chat Bot that takes in an input through the console and prints a random answer back.
    In order to not be stuck in an infinate loop, a simple counter is added to break after ten
    replies.
"""

def main():
    start_counter = 0
    running_program = True
    while running_program:
        request = input("You: ")
        response = english_bot.get_response(request)
        print('Bot: ', response)
        start_counter += 1
        if (start_counter > 10):
            running_program = False

if __name__ == '__main__':
    main()

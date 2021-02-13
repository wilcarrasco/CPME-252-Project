from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import sys


path = "c:/Users/VenEn/OneDrive/Desktop/python/.vscode/workspace_cmpe252/chatterbot/txt"
bot = ChatBot('FRiDAY', logic_adapter = ["chatterbot.logic.BestMatch"])
trainer = ListTrainer(bot)

for _file in os.listdir(path):
    chats = open(path+"/" + _file, 'r').readlines()
    trainer.train(chats)


def string_contain(str1):
    multiple_inputs_dict = ['and','And','also','Also']
    for word in multiple_inputs_dict:
        if word in str1:
            return str1.split(word)
    return str1

while True:
    try:
        request = input("You: ")
        query = string_contain(request)
        for userInput in query:
            userInput = userInput.strip()
            response = bot.get_response(userInput)
            print('Bot: ', response)
    # press ctrl-c or ctrl-d on keyboard to exit
    except(KeyboardInterrupt, EOFError, SystemExit):
        break

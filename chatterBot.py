from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import sys


#Path pulls current directory and adds txt folder
path = os.getcwd()+"/txt"
bot = ChatBot('FRiDAY', logic_adapter = ["chatterbot.logic.BestMatch"])
trainer = ListTrainer(bot)

for _file in os.listdir(path):
    chats = open(path+"/" + _file, 'r').readlines()
    trainer.train(chats)

print("Bot: To process your request. Just press enter with no characters after inputting your request")
while True:
    try:
        userTurn = 1
        query = []
        while (userTurn == 1):
            line = input("You: ")
            if line:
                query.append(line)
            else:
                userTurn = 0
        for userInput in query:
            response = bot.get_response(userInput)
            print('Bot: ',response)
        userTurn = 1
    except(KeyboardInterrupt, EOFError, SystemExit):
        break


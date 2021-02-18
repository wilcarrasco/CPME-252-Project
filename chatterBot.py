from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import sys


#Path pulls current directory and adds txt folder
pwd = os.getcwd()
path = os.path.join(pwd, "txt")
bot = ChatBot('Help Desk', read_only=True, logic_adapter = ["chatterbot.logic.BestMatch"])
trainer = ListTrainer(bot)

for file in os.listdir(path):
    with open(os.path.join(path, file), 'r') as f:
        chats = f.read().splitlines() 
    trainer.train(chats)

print("Help Desk: To process your request. Just press enter with no characters after inputting your request")
print('Help Desk: If you need help reseting your password type "I need help resetting my password"')
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
            print('Help Desk: ',response)
        userTurn = 1
    except(KeyboardInterrupt, EOFError, SystemExit):
        break


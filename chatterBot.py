from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import sys

ISSUES = ['computer','laptop','slow','virus','bug','overheating','password','reset','update','updating','software', 'blue screen']

#Path pulls current directory and adds txt folder
pwd = os.getcwd()
path = os.path.join(pwd, "txt")
bot = ChatBot('Help Desk', read_only=True, logic_adapter = ["chatterbot.logic.BestMatch"])
trainer = ListTrainer(bot)

for file in os.listdir(path):
    with open(os.path.join(path, file), 'r') as f:
        chats = f.read().splitlines() 
    trainer.train(chats)
 
###### Initialize File ###########
### This file should be located where your python exe file is. This will save the conversation that occurs
SAVE_FILE = open("saveInfo.txt","w")
SAVE_FILE.truncate(0)

def printTicket():
    print("")
    print("-----------------------------------------------------------------")
    print("*****************************************************************")
    print('Here is yout ticket with the following issues we helped you with')
    # Open saved conversation from past 
    SAVE_FILE = open("saveInfo.txt","r")
    for line in SAVE_FILE: # go though each line from the conversation
        num = 1 
        printnewLine = 0
        if "You:" in line: # only sorts through user inputs, bot responses not needed. 
            for issue in ISSUES: # issues are in the list to sort though the user input to see which issues occurred. 
                if issue in line:
                    if num == 1: # variable is used to make intiialize the "Issue: " msg and then it starts to gather key words to print
                        print("Issue: ", end = ' ')
                        print(str(issue), end = ' ')
                        num = 2
                        printnewLine = 1
                    else:
                        print(str(issue), end = ' ')
            if printnewLine == 1: # when we are done with the user input, we make a new line make 
                # new line for an issue to printed on the ticket
                print('')
    print("*****************************************************************")
    print("-----------------------------------------------------------------")
    return


print("Help Desk: To process your request. Just press enter with no characters after inputting your request")
print("Help Desk: To end the conversation press CTRL+C")
print('Help Desk: If you need help reseting your password type "I need help resetting my password"')

while True:
    try:
        userTurn = 1
        query = []
        while (userTurn == 1):
            line = input("You: ")
            if line:
                SAVE_FILE.write('You: ' + line+'\n')
                query.append(line)
            else:
                userTurn = 0
        for userInput in query:
            response = bot.get_response(userInput)
            SAVE_FILE.write('Bot: ' + str(response)+'\n')
            print('Help Desk: ',response)

        userTurn = 1
    except(KeyboardInterrupt, EOFError, SystemExit):
        SAVE_FILE.close()
        printTicket()
        break


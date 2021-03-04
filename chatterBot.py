from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import time
import sendEmail

ISSUES = [
    'computer',
    'laptop',
    'slow',
    'virus',
    'bug',
    'overheating',
    'password',
    'reset',
    'update',
    'updating',
    'software',
    'blue screen',
    'cyber',
    'mouse',
    'keyboard',
    'delete',
    'deleted',
    'print',
    'printer',
    'storage',
    'restart',
    'wifi',
    'wi-fi',
    'coffee',
    'spilt',
    'share',
    'share drive',
    'website',
    'cd']

END_RESPONSE = [
    "Ok an automatically generating ticket will be printed, have a great day!",
    "Sorry to hear that, call the helpdesk then you psycho!"]

'''
    Creates and trains a chatbot
'''
def train_bot():
    #Path pulls current directory and adds txt folder
    pwd = os.getcwd()
    path = os.path.join(pwd, "txt")
    bot = ChatBot(
        'Help Desk',
        read_only=True, 
        preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
        ],
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters = [
            {
                'import_path': 'custom_logic.HelpResponse',
            },
            {
                'import_path':'chatterbot.logic.BestMatch',
                "statement_comparison_function": 'chatterbot.comparisons.LevenshteinDistance',
                'default_response': 'I am sorry, I do not understand. For items I am most helpful with, enter: help',
                'maximum_similarity_threshold': 0.80
            }
        ]
    )
    trainer = ListTrainer(bot)

    for file in os.listdir(path):
        with open(os.path.join(path, file), 'r') as f:
            #converts all training files to lower case
            chats = f.read().lower().splitlines()
        trainer.train(chats)
    return bot

def print_ticket():
    print("\n-----------------------------------------------------------------")
    print("*****************************************************************")
    print('Here is your ticket with the following issues we helped you with')
    # Open saved conversation from past 
    SAVE_FILE = open("saveInfo.txt","r")
    for line in SAVE_FILE: # go though each line from the conversation
        num = 1 
        printnewLine = 0
        if "You:" in line: # only sorts through user inputs, bot responses not needed. 
            for issue in ISSUES: # issues are in the list to sort though the user input to see which issues occurred. 
                if issue in line:
                    if num == 1: # variable is used to make initialize the "Issue: " msg and then it starts to gather key words to print
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

def main():
    bot = train_bot()
    helping = True
    ###### Initialize File ###########
    ### This file should be located where your python exe file is. This will save the conversation that occurs
    SAVE_FILE = open("saveInfo.txt","w")
    SAVE_FILE.truncate(0)
    userEmail = input("Please provide your email: ")
    print("Help Desk: To process your request. Just press enter with no characters after inputting your request")
    print("Help Desk: To end the conversation press CTRL+C")
    print('Help Desk: For a list of top items, enter: help')
    while helping:
        try:
            user_turn = 1
            query = []
            while (user_turn == 1):
                #converts user input to lower
                line = input("You: ").lower()
                if line:
                    SAVE_FILE.write('You: {}\n'.format(line))
                    query.append(line)
                else:
                    user_turn = 0
            for userInput in query:
                response = bot.get_response(userInput)
                SAVE_FILE.write('Help Desk: {}\n'.format(str(response)))
                print('Help Desk: {}'.format(response))
                if (str(response) in END_RESPONSE):
                    helping = False
                    time.sleep(2)
                    SAVE_FILE.close()
                    print_ticket()
                    sendEmail.transcriptSend(str(userEmail))
            user_turn = 1
        except(KeyboardInterrupt, EOFError, SystemExit):
            SAVE_FILE.close()
            print_ticket()
            sendEmail.transcriptSend(str(userEmail))
            break

if __name__ == '__main__':
    main()

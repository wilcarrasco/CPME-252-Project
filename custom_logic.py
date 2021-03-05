from os import stat
from chatterbot.logic import LogicAdapter

class HelpResponse(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        tmp = statement.text.lower()
        if tmp == "help":
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        
        confidence = 1

        ISSUES = [
            'Slow computer',
            'Virus check',
            'Software bug',
            'Resetting my password',
            'Update',
            'New software',
            'Bluescreen',
            'Connecting to bluetooth',
            'I\'ve been hacked',
            'Broken mouse',
            'Broken keyboard',
            'Delete files',
            'Find a printer',
            'Storage',
            'Unexpected restart',
            'Wi-Fi is slow',
            'Spilt coffee',
            'Share drive',
            'Blocked website',
            'CD burner',
            'CD reader', 
            'Tell me a funny joke']
        
        selected_statement = Statement(text='Here are some items I can help with: {}\n'.format(str(ISSUES).strip('[]')))
        selected_statement.confidence = confidence

        return selected_statement




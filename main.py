"""
@author: Taycir Yahmed
"""

from Chatbot import Chatbot


if __name__ == "__main__":

    chatbot = Chatbot()
    chatbot.train()
    print "Lets discuss with the TBBT"
    while True:
        print '>',
        request = raw_input()
        print '> ' + chatbot.test(request),

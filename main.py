""" A simple chatbot using cosine similarity
Created by Taycir Yahmed as the starter code for a machine learning bot.

This file contains the code to run the model.
See readme.md for instruction on how to run the starter code.
"""

from Chatbot import Chatbot
import argparse

if __name__ == "__main__":

    chatbot = Chatbot()

    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices={'train', 'chat'},
                        default='train', help="mode. Default is the train mode")

    args = parser.parse_args()

    if args.mode == 'train':
        chatbot.train()
    elif args.mode == 'chat':
        chatbot.chat()

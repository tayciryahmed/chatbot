""" A chatbot using cosine similarity
Created by Taycir Yahmed as the starter code for a machine learning bot.

This file contains the hyperparameters for the model.
See readme.md for instruction on how to run the starter code.
"""

# parameters for processing the dataset/running the chatbot

DATA_PATH = "data"
characters = ["Howard", "Penny", "Raj", "Sheldon", "Leonard"]
common_questions = [
    "What is your name?",
    "How old are you?"
]

common_answers = [
    "One of the TBBT characters is chating with you. Who are you?\n",
    "Why do you want to know my age?!\n"
]

non_sense = "I don't get it.\n"

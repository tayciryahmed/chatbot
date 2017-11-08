""" A chatbot using cosine similarity
Created by Taycir Yahmed as the starter code for a machine learning bot.

This file contains the code to train and test the model.
See readme.md for instruction on how to run the starter code.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import config
import os
from unidecode import unidecode
import operator
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle


class Chatbot:

    def load_data(self):
        files = os.listdir(config.DATA_PATH)
        data = []
        for file in files:
            data_episode = []
            data_scene = []
            lines = tuple(open(config.DATA_PATH + "/" + file, 'r'))
            for line in lines:
                utt = ""
                for character in config.characters:
                    if line.startswith(character):
                        utt = unidecode(str(line).decode('utf8'))
                if len(utt) != 0:
                    data_scene.append(utt)
                elif line == '\n':
                    pass
                else:
                    data_episode.append(data_scene)
                    data_scene = []

            data.append(data_episode)

        return data

    def train(self):
        data = self.load_data()
        self.data_flat = [
            utt for episode in data for scene in episode for utt in scene]
        self.data_flat.extend(config.common_questions)

        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.data_vectorized = self.vectorizer.fit_transform(self.data_flat)

        with open("data/model", "wb") as f:
            pickle.dump(self, f)

        print("Model trained and saved.")

    def get_answer(self, request):

        with open("data/model", 'r') as f:
            self = pickle.load(f)

        request_vector = self.vectorizer.transform([request])

        sim = []

        for vector in self.data_vectorized:
            sim.append(cosine_similarity(vector, request_vector)[0][0])

        a = np.argmax(sim)

        if a >= len(sim) - len(config.common_answers):
            return config.common_answers[-len(sim) + np.argmax(sim)]

        elif a == 0:
            return config.non_sense

        else:
            return self.data_flat[a + 1][self.data_flat[a + 1].index(":") + 2:]

    def chat(self):
        print "Lets discuss with the TBBT characters"
        while True:
            print '>',
            request = raw_input()
            print '> ' + self.get_answer(request),

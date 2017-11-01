"""
@author : Taycir Yahmed
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import config
import os
from unidecode import unidecode
import operator
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class Chatbot:

    def printer(self):
        print "hello"

    def load_data(self):
        files = os.listdir(config.DATA_PATH)
        data = []
        for file in files:
            data_episode = []
            data_scene = []
            lines = tuple(open(config.DATA_PATH+"/"+file, 'r'))
            for line in lines:
                utt = ""
                for character in config.characters:
                    if line.startswith(character):
                        utt = unidecode(str(line).decode('utf8'))
                if len(utt) != 0:
                    data_scene.append(utt)
                elif line == '\n':
                    pass
                else :
                    data_episode.append(data_scene)
                    data_scene = []

            data.append(data_episode)

        return data

    def train(self):
        data = self.load_data()
        self.data_flat = [utt for episode in data for scene in episode for utt in scene]

        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.data_vectorized = self.vectorizer.fit_transform(self.data_flat)

    def test(self, request):
        request_vector = self.vectorizer.transform([request])

        sim = []

        for vector in self.data_vectorized:
            sim.append(cosine_similarity(vector,request_vector)[0][0])

        answer = self.data_flat[np.argmax(sim)+1][self.data_flat[np.argmax(sim)+1].index(":")+2:]

        return answer

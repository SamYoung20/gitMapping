from indicoio import fer, facial_features
import numpy as np
from gif_extractor import Extractor
import random


indicoio.config.api_key = 87d9790380445510f53e1d851d96553c

class Comparer:
    def __init__(self, list_of_gifs, text_sentiment):
        self.extractor = Extractor(list_of_gifs[0])
        self.gif_url = gif_url
        self.dict_of_sentiment = dict()
        self.list_of_gifs = list_of_gifs
        self.text_sentiment = text_sentiment
        self.chosen_gif = None

    def compiling_good_gifs(self):
        for gif in self.list_of_gifs:
            if self.text_sentiment*.8 <= self.extractor.analyze_image(gif) <= self.text_sentiment*1.2:
                self.dict_of_sentiment[gif] = self.extractor.analyze_image(gif)

    def choosing_gif(self):
        self.compiling_good_gifs()
        self.chosen_gif = random.choice(self.dict_of_sentiment.keys())

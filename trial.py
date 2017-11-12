import os
import operator
from PIL import Image
from indicoio import fer, facial_features, sentiment_hq

indicoio.config.api_key = 87d9790380445510f53e1d851d96553c


class Extractor:
    def __init__(self, list_of_gifs, text_sentiment):
        self.list_of_gifs = list_of_gifs
        self.gif_max_object = None
        self.list_objects = []
        self.text_sentiment = text_sentiment
        self.sentiment_output = None

    def analyze_image(self):
        gif_output = []
        gif_output = indicoio.analyze_image(self.gif_url, apis=["image_recognition", "fer"])
        self.list_objects = [name for name, prob in gif_output[0].items() if prob => .2]
        self.sentiment_output = indicoio.sentiment_hq(self.list_objects)
        return self.sentiment_output

    def compiling_good_gifs(self):
        for gif in self.list_of_gifs:
            if self.text_sentiment*.8 <= self.analyze_image(gif) <= self.text_sentiment*1.2:
                self.dict_of_sentiment[gif] = self.analyze_image(gif)
        return self.dict_of_sentiment

    def choosing_gif(self):
        return self.chosen_gif = random.choice(self.compiling_good_gifs.keys())

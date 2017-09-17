import os
import operator
from PIL import Image
import random
import urllib
from urllib.parse import urlencode
from urllib.request import urlopen
import json
import math
import pprint
import indicoio
from indicoio import political, sentiment, language, text_tags, keywords, fer, facial_features, image_features
from get_gif import Get_Gif
import numpy as np

indicoio.config.api_key = '87d9790380445510f53e1d851d96553c'


class Extractor:
    def __init__(self, list_of_gifs, text_sentiment):
        self.list_of_gifs = list_of_gifs
        self.gif_max_object = None
        self.list_objects = []
        self.text_sentiment = text_sentiment
        self.sentiment_output = None
        self.list_of_sentiment =[]


    def analyze_image(self,gif_url):
        gif_output = []
        gif_output = indicoio.image_recognition(gif_url)
        self.list_objects = [name for name, prob in gif_output.items() if prob > .1]
        if len(self.list_objects) == 1:
            self.sentiment_output = indicoio.sentiment_hq(self.list_objects[0])
        else:
            self.sentiment_output = indicoio.sentiment_hq(self.list_objects)
            self.sentiment_output = np.mean(self.sentiment_output)
        return self.sentiment_output

    def compiling_good_gifs(self):
        for gif in self.list_of_gifs:
            if self.text_sentiment*.8 <= self.analyze_image(gif) <= self.text_sentiment*1.2:
                self.list_of_sentiment.append(gif)
        return self.list_of_sentiment

    def choosing_gif(self):
        return random.choice(self.compiling_good_gifs())

if __name__ == '__main__':
    search_list = Get_Gif(["cat","dog"])
    Gif_list = Get_Gif.get_json(search_list)
    giffy = Extractor(Gif_list,.8)
    Gif = Extractor.choosing_gif(giffy)


    #gif_list = Get_Gif.encode_search(search_list)
    #search_list = Get_Gif(["cat","dog"],"")

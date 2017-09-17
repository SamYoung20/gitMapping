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
from get_gif import Get_Giffer
import numpy as np

indicoio.config.api_key = '87d9790380445510f53e1d851d96553c'


class Extractor:
    def __init__(self, list_of_gifs, text_sentiment):
        self.list_of_list_of_gifs = list_of_gifs
        self.list_of_gifs = None
        self.gif_max_object = None
        self.list_objects = []
        self.text_sentiment = text_sentiment
        self.sentiment_output = None
        self.list_of_sentiment =[]
        self.list_of_random_gifs = []


    def analyze_image(self,gif_url):
        """
        Checks to see if there are any recognizable objects in the gifs, and if there are performs sentiment analysis on the objects. Then it outputs the average of the sentiment analysis of all the objects
        """
        gif_output = []
        gif_output = indicoio.image_recognition(gif_url)
        self.list_objects = [name for name, prob in gif_output.items() if prob > .05]
        if len(self.list_objects) == 1:
            self.sentiment_output = indicoio.sentiment_hq(self.list_objects[0])
        elif len(self.list_objects) == 0:
            return self.text_sentiment
        else:
            self.sentiment_output = indicoio.sentiment_hq(self.list_objects)
            self.sentiment_output = np.mean(self.sentiment_output)
        return self.sentiment_output

    def compiling_good_gifs(self):
        """
        Checks that the sentiments of the gifs are within range of the sentiment analysis of the article
        """
        for gif in self.list_of_gifs:
            if self.text_sentiment*.8 <= self.analyze_image(gif) <= self.text_sentiment*1.2:
                self.list_of_sentiment.append(gif)
        return self.list_of_sentiment

    def choosing_gif(self):
        """
        Resets the sentiment values for each list of gifs and randomly choses one of the optimal gifs
        """
        self.list_of_sentiment = []
        return random.choice(self.compiling_good_gifs())

    def running_gifs(self):
        """
        Takes each of the list of list of possible gifs and runs through all the gif lists and calls choosing_gif in order to select what gif to chose
        """
        for list_of_gif in self.list_of_list_of_gifs:
            self.list_of_gifs = list_of_gif
            self.list_of_random_gifs.append(self.choosing_gif())
        return self.list_of_random_gifs

if __name__ == '__main__':
    search_list = Get_Giffer('https://www.washingtonpost.com/powerpost/to-make-their-tax-plan-work-republicans-eye-a-favorite-blue-state-break/2017/09/16/c726d506-9a26-11e7-b569-3360011663b4_story.html?hpid=hp_hp-top-table-main_taxpolitics-3pm%3Ahomepage%2Fstory&utm_term=.4a4beb64240d')
    Gif_list = Get_Giffer.get_json(search_list)
    sentiment = Get_Giffer.output_sentiment(search_list)
    giffy = Extractor(Gif_list,sentiment)
    Gif = Extractor.running_gifs(giffy)
    print(Gif)

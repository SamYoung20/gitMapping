import os
import operator
from PIL import Image
from indicoio import fer, facial_features, sentiment_hq

indicoio.config.api_key = 87d9790380445510f53e1d851d96553c


class Extractor:
    def __init__(self, gif_url):
        self.gif_url = gif_url
        self.gif_max_object = None
        self.gif_max_emotion
        self.list_objects=[]
        self.sentiment_output = None

    def analyze_image(self):
        gif_output = []
        gif_output = indicoio.analyze_image(self.gif_url, apis=["image_recognition", "fer"])
        self.list_objects = [name for name, prob in gif_output[0].items() if prob => .2]
        self.sentiment_output = indicoio.sentiment_hq(self.list_objects)
        return self.sentiment_output

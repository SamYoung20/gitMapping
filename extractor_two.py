import os
import operator
from PIL import Image
from indicoio import fer, facial_features, sentiment_hq
from get_gif import Get_Gif

indicoio.config.api_key = '87d9790380445510f53e1d851d96553c'


class Extractor:
    def __init__(self, text_sentiment):
        self.list_of_gifs = get_gif.get_json(search_list)
        self.gif_max_object = None
        self.list_objects = []
        self.text_sentiment = text_sentiment
        self.sentiment_output = None


    def analyze_image(self):
        gif_output = []
        gif_output = indicoio.analyze_image(self.gif_url, apis=["image_recognition", "fer"])
        self.list_objects = [name for name, prob in gif_output[0].items() if prob > .2]
        self.sentiment_output = indicoio.sentiment_hq(self.list_objects)
        return self.sentiment_output

    def compiling_good_gifs(self):
        for gif in self.list_of_gifs:
            if self.text_sentiment*.8 <= self.analyze_image(gif) <= self.text_sentiment*1.2:
                self.dict_of_sentiment[gif] = self.analyze_image(gif)
        return self.dict_of_sentiment

    def choosing_gif(self):
        self.chosen_gif = random.choice(self.compiling_good_gifs.keys())
        return self.chosen_gif

if __name__ == '__main__':
    search_list= ["cat", "dog"]
    my_get_gif = Get_Gif.get_json(search_list)
    pprint.pprint(my_get_gif)


    #gif_list = Get_Gif.encode_search(search_list)
    #search_list = Get_Gif(["cat","dog"],"")

    """import os
    import operator
    from PIL import Image
    from indicoio import fer, facial_features, sentiment_hq

    indicoio.config.api_key = '87d9790380445510f53e1d851d96553c'


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
            return self.chosen_gif = random.choice(self.compiling_good_gifs.keys())"""

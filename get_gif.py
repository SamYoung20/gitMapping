import urllib
from urllib.parse import urlencode
from urllib.request import urlopen
import json
import math
import pprint
import sys
sys.dont_write_bytecode = True
from newsreader import Newsreader
import indicoio

sys.dont_write_bytecode = True
GIPHY_BASE_URL = "http://api.giphy.com/v1/gifs/search?q="
api_key = "&api_key=ArJf7WEbSsinMVRarXZoXn97gZhvsAau"
limit_format = "&limit=5"
limit = 5
sys.dont_write_bytecode = True

class Get_Giffer:

    def __init__(self, urlNews):
        reading = Newsreader(urlNews)
        self.search = reading.top_5()
        self.sentiment = reading.analyze_Sentiment_indico()
        self.url = []

    def output_sentiment(self):
        return self.sentiment
        self.url = None


    def make_GIPHY_url(self):
        print(self.search)
        for word in self.search:
            self.url.append(GIPHY_BASE_URL + word + api_key + limit_format)
        #return slist of url's
        return self.url

    def get_json(self):
        """
        formats a url to take an address from the user and properly formats URL
        for a JSON web API request, return
        a Python JSON object containing the response to that request.
        """
        url_list = self.make_GIPHY_url()
        all_urls = []
        for url in url_list:
            f = urlopen(url)
            response_text = f.read()
            response_data = str(response_text, "utf-8")
            response_data = json.loads(response_data)
            gif_urls = []
            for result in range(limit):
                result = response_data['data'][result]
                data = result['images']['fixed_height']['url']
                gif_urls.append(data)
            all_urls.append(gif_urls)
        return all_urls


if __name__ == '__main__':
    sys.dont_write_bytecode = True
    urlForNews = Get_Giffer('http://www.foxnews.com/sports/2017/09/18/nascar-driver-pilot-killed-in-connecticut-plane-crash.html')
    Gif = Get_Giffer.get_json(urlForNews)
    pprint.pprint(Gif)

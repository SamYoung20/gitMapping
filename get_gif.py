import urllib
from urllib.parse import urlencode
from urllib.request import urlopen
import json
import math
import pprint

GIPHY_BASE_URL = "http://api.giphy.com/v1/gifs/search?q="
api_key = "&api_key=ArJf7WEbSsinMVRarXZoXn97gZhvsAau"
limit_format = "&limit=5"
limit = 5

class Get_Gif:

    def __init__(self, search, url):
        self.search = search
        self.url = url

    def make_GIPHY_url(self):
        #print(self.search)
        self.url = GIPHY_BASE_URL + self.search + api_key + limit_format
        #print(self.url)
        return self.url

    def get_json(self):
        """
        formats a url to take an address from the user and properly formats URL
        for a JSON web API request, return
        a Python JSON object containing the response to that request.
        """
        self.encode_search()
        f = urlopen(self.url)
        response_text = f.read()
        response_data = str(response_text, "utf-8")
        response_data = json.loads(response_data)
        #pprint.pprint(response_data)

        gif_urls = []
        for result in range(limit):
            result = response_data['data'][result]
            data = result['images']['fixed_height']['url']
            gif_urls.append(data)
        return gif_urls

    def encode_search(self):
        '''
        make the search in the correct format
        '''
        new_search = ""
        for word in self.search:
            new_search = new_search + word + "+"
        self.search = new_search[:-1]
        self.url = self.make_GIPHY_url()
        return self.url

    #def compile(self):



if __name__ == '__main__':
    search_list = Get_Gif(["cat","dog"],"")
    #gif_list = Get_Gif.encode_search(search_list)

    Gif = Get_Gif.get_json(search_list)
    pprint.pprint(Gif)

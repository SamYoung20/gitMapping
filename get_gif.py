import urllib
from urllib.parse import urlencode
from urllib.request import urlopen
import json
import math
import pprint
import indicoio
from newsreader import Newsreader

GIPHY_BASE_URL = "http://api.giphy.com/v1/gifs/search?q="
api_key = "&api_key=ArJf7WEbSsinMVRarXZoXn97gZhvsAau"
limit_format = "&limit=5"
limit = 5

class Get_Giffer:

    def __init__(self, urlNews):
        reading = Newsreader(urlNews)
        self.search = reading.top_5()
        #print(self.search)
        self.url = None

    #def encode_search(self):


    def make_GIPHY_url(self):
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
        #pprint.pprint(response_data)
            gif_urls = []
            for result in range(limit):
                result = response_data['data'][result]
                data = result['images']['fixed_height']['url']
                gif_urls.append(data)
            all_urls.append(gif_urls)
        print(all_urls)
        return all_urls


if __name__ == '__main__':
    urlForNews = Get_Giffer('https://www.washingtonpost.com/powerpost/to-make-their-tax-plan-work-republicans-eye-a-favorite-blue-state-break/2017/09/16/c726d506-9a26-11e7-b569-3360011663b4_story.html?hpid=hp_hp-top-table-main_taxpolitics-3pm%3Ahomepage%2Fstory&utm_term=.4a4beb64240d')
    Gif = Get_Giffer.get_json(urlForNews)
    pprint.pprint(Gif)

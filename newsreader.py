import requests
import re
import string
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import newspaper
from newspaper import Article


class Newsreader:

    def __init__(self, url1):
        self.article = Article(url=url1)

    def loadArticleToText(self):
        articlelo = self.article
        articlelo.download()
        articlelo.parse()
        art = articlelo.text
        return art

    def cleanText(self):
        art = self.loadArticleToText()
        exclude = set(string.punctuation)  # makes set of punctuation characters
        s = ''.join(ch for ch in art if ch not in exclude)  # for each character of the story creates a new string without any of the pucntiation
        s = s.lower()
        artList = s.split() #breaks up string at the spaces creates a list of elements
        artList = [element for element in artList if (len(element) > 4)]  # only inlcudes words longer than 4 characters and not in the title
        return artList

    def analyze_Sentiment(self):
        # needs a str or a file no lists
        #makes dictionary of sentiment
        art = self.cleanText()
        analyzer = SentimentIntensityAnalyzer()
        return analyzer.polarity_scores(art)

    def word_Frequency(self):
        art = self.cleanText()
        word_freq = dict()
        for c in art:
            word_freq[c] = word_freq.get(c, 0) + 1  # counts the number of times eeach word appears and keeps track in dictioary
        print(word_freq)
        return word_freq

    def top_5(self):
        #finds top 10 words used
        art_words = self.word_Frequency()
        artsorted = sorted(art_words, key=art_words.__getitem__, reverse=True) # sorts dictionary by value (by frequency of word in story) highest value first
        print(artsorted)
        artsorted = artsorted[:5] # returns the first 10 words
        print artsorted
        print('hello')
        print(artsorted)



if __name__ == '__main__':
    reader = Newsreader('http://www.npr.org/sections/thetwo-way/2017/09/16/551502217/a-mostly-typical-saturday-in-washington-d-c-political-rallies-plus-juggalos')
    print(reader.top_5())

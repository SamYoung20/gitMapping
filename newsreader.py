import requests
import re
import string
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import newspaper
from newspaper import Article
import nltk
import indicoio
from indicoio import sentiment_hq
from nltk import word_tokenize
from nltk.corpus import stopwords

indicoio.config.api_key = '87d9790380445510f53e1d851d96553c'


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
        stop = set(stopwords.words('english'))
        words = ['would', "should", "could", "said"]
        nonCommon = [i for i in s.lower().split() if ((i not in stop) and (i not in words))]
        #print(nonCommon) #breaks up string at the spaces creates a list of elements
        artList = [element for element in nonCommon if (len(element) > 4)] # only inlcudes words longer than 4 characters and not in the title
        #print(type(artList))
        return nonCommon


    def analyze_Sentiment(self):
        # needs a str or a file no lists
        #makes dictionary of sentiment
        art = self.cleanText()
        s = ' '.join(ch for ch in art)
        analyzer = SentimentIntensityAnalyzer()
        return analyzer.polarity_scores(s)

    def analyze_Sentiment_indico(self):
        art = self.cleanText()
        s = ''.join(ch for ch in art)
        sentiment = indicoio.sentiment_hq(s)
        return sentiment

    def word_Frequency(self):
        art = self.cleanText()
        word_freq = dict()
        for c in art:
            word_freq[c] = word_freq.get(c, 0) + 1  # counts the number of times eeach word appears and keeps track in dictioary
        return word_freq

    def top_5(self):
        #finds top 10 words used
        print('chicharito!')
        art_words = self.word_Frequency()
        artsorted = sorted(art_words, key=art_words.__getitem__, reverse=True) # sorts dictionary by value (by frequency of word in story) highest value first
        artsorted = artsorted[:5] # returns the first 10 words
        return(artsorted)


if __name__ == '__main__':
    reader = Newsreader('https://www.washingtonpost.com/powerpost/to-make-their-tax-plan-work-republicans-eye-a-favorite-blue-state-break/2017/09/16/c726d506-9a26-11e7-b569-3360011663b4_story.html?hpid=hp_hp-top-table-main_taxpolitics-3pm%3Ahomepage%2Fstory&utm_term=.4a4beb64240d')
    #print(reader.loadArticleToText())
    topWords = reader.top_5()
    sentiment = reader.analyze_Sentiment_indico()

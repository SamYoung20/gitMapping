import newspaper

nyt_paper = newspaper.build('https://www.nytimes.com/')
for article in nyt_paper.articles:
    print(article.url)

from newsdataapi import NewsDataApiClient
from newsdataapi import newsdataapi_exception
import secrets
import json

api = NewsDataApiClient(apikey=secrets.keys.newsAPI)

def getNews(query:str=None):
    try:
        articles = []
        response = api.news_api(q=query, country="us")
        results = response.get("results", [])
        for article in results:
            if "title" in article and "link" in article:
                articles.append([article["title"], article["link"]])
                
        for article in articles:
            print("title -", article[0])
            print("link -", article[1])
    except newsdataapi_exception as e:
        print("API error:", e)


getNews("Crypto")
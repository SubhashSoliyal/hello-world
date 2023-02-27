# akhbar padh ke sunao
# first news is 
# top 10 news of the day

# json, request
# Your API key is: 290f3f5aad8e414586093fc29c4acb99

# https://newsapi.org/register/success

import json
import requests

from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='290f3f5aad8e414586093fc29c4acb99')

# # # /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2023-01-05',
                                      to='2023-01-05',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()

def Speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")
    print(str)
    speak.Speak(str)
    
    # speak.Speak("hello subhash bhai")




url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2023-02-05&'
       'to=2023-02-05&'
       'sortBy=popularity&'
       'apiKey=290f3f5aad8e414586093fc29c4acb99')

# https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey=290f3f5aad8e414586093fc29c4acb99
# relevancy, popularity, publishedAt.
# relevancy = articles more closely related to q come first.
# popularity = articles from popular sources and publishers come first.
# publishedAt = newest articles come first.

# Default: publishedAt

# pageSize
# int
# The number of results to return per page.

# Default: 100. Maximum: 100.
# page
# int
# Use this to page through the results.

# Default: 1

# Sub-categories
# business entertainment health science sports technology

response = requests.get(url)
response.json()
print(type(response))


import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=290f3f5aad8e414586093fc29c4acb99')
response = requests.get(url)
# print( response.json())
news = response.json()
result_found = news['totalResults']
for i in range(result_found - 3):
    print(news['status'])
    print(news['totalResults'])
    # print(news['articles'][i]['author'])
    # print(news['articles'][i]['title'])
    # print(news['articles'][i]['description'])
    # print(news['articles'][1]['url'])
    # print(news['articles'][1]['urlToImage'])
    # print(news['articles'][1]['publishedAt'])
    # print(news['articles'][1]['content'])
    # print(news['articles'][i]['source']['id'])
    print(news['articles'][i]['source']['name'])
    print("\n\n")




import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=290f3f5aad8e414586093fc29c4acb99')
response = requests.get(url)
print(response.json())

# print("Decoded JSON Data From File")
# for key, value in news.items():
#         print(key, ":", value)
# print("Done reading json file")

# news = json.loads(response)
# print(news)




if __name__ == '__main__':
    Speak("hello subhash bhai")
    # Speak(top_headlines)
    # Speak(all_articles)
    # Speak(sources)



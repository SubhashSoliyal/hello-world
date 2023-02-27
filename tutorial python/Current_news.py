import json
import requests
from win32com.client import Dispatch
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='290f3f5aad8e414586093fc29c4acb99')


def Speak_News(str):
    Speak_N = Dispatch("SAPI.SpVoice")
    print(str)
    Speak_N.Speak(str)

def news_everything(q='i love',
                    sources='bbc-news,the-verge',
                    domains='bbc.co.uk,techcrunch.com',
                    from_param='2023-01-05',
                    to='2023-01-05',
                    language='en',
                    sort_by='relevancy',
                    page=2):

    # /v2/everything
    all_articles = newsapi.get_everything(q=q,
                                          sources=sources,
                                          domains=domains,
                                        from_param=from_param,
                                        to=to,
                                        language=language,
                                        sort_by=sort_by,
                                        page=page)


    return all_articles



def top_headlines(q='india',
                  
                  category='science',
                  language='en',
                  country='in'):
    # # # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(q= q,
                                          
                                          category=category,
                                          language=language,
                                          country=country)
    return top_headlines


if __name__ == '__main__':
    Speak_News("hello subhash bhai")
    q= top_headlines('car','business')
    # print(q)
    Speak_News(q['status'])
    Speak_News(q['totalResults'])
    for i in range(q['totalResults']):
        Speak_News(q['articles'][i]['title'])
        Speak_News(q['articles'][i]['description'])
    

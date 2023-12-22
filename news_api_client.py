import os

from newsapi.newsapi_client import NewsApiClient

API_KEY = os.environ['NEWS_API_KEY']

# Init
newsapi = NewsApiClient(api_key=API_KEY)

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='tesla',
                                          #sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

print("top_headlines \n", top_headlines)

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2023-11-22',
                                      to='2023-12-22',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)

print("\n all_articles \n", all_articles)

# /v2/top-headlines/sources
sources = newsapi.get_sources()

print("\n sources \n", sources.get('sources'))

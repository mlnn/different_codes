import json

def listmerge(lstlst):
    all=[]
    for lst in lstlst:
        for el in lst:
            all.append(el)
    return all

def get_list_news(country):
    list_news = []
    if country == 'afr':
        with open('newsafr.json', encoding = 'UTF-8') as f:
            news = json.load(f)
    elif country == 'cy':
        with open('newscy.json', encoding = 'KOI8-R') as f:
            news = json.load(f)
    elif country == 'fr':
        with open('newsfr.json', encoding='ISO8859-5') as f:
            news = json.load(f)
    elif country == 'it':
        with open('newsit.json') as f:
            news = json.load(f)
    for new in news['rss']['channel']['items']:
        list_news.append(new['description'].split())
    list_news = listmerge(list_news)
    return list_news

def get_list_news_long(list_news):
    list_news_long = []
    for item in list_news:
        if len(item) > 6:
            list_news_long.append(item)
    return list_news_long

def get_counter(list_news_long):
    counter = {}
    set_news = set(list_news_long)
    for name in set_news:
        counter.update({name: list_news_long.count(name)})
    return counter

def print_sort_news(country):

    list_news = get_list_news(country)
    list_news_long = get_list_news_long(list_news)
    list_news_long.sort()
    counter = get_counter(list_news_long)
    sort_news = sorted(counter.items(), key=lambda x: x[1])
    for i in range(10):
        print(sort_news.pop())

print_sort_news('it')
print("---------------------------")
print_sort_news('afr')
print("---------------------------")
print_sort_news('cy')
print("---------------------------")
print_sort_news('fr')
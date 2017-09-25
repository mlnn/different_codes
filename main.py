import json

def json_open(name, code):
    with open(name, encoding = code) as f:
        news = json.load(f)
    return news

def listmerge(lstlst):
    all=[]
    for lst in lstlst:
        for el in lst:
            all.append(el)
    return all

def get_list_news(country):
    list_news = []
    if country == 'afr':
        news = json_open('newsafr.json', 'UTF-8')
    elif country == 'cy':
        news = json_open('newscy.json', 'KOI8-R')
    elif country == 'fr':
        news = json_open('newsfr.json', 'ISO8859-5')
    elif country == 'it':
        news = json_open('newsit.json', 'CP1251')
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
    for item in sort_news[-10:]:
        print(item)

print_sort_news('it')
print("---------------------------")
print_sort_news('afr')
print("---------------------------")
print_sort_news('cy')
print("---------------------------")
print_sort_news('fr')
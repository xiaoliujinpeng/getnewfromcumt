import requests
from bs4 import BeautifulSoup


def getHtml(url):
    user_agent = "Mozilla/5.0"
    headers = {"User-Agent": user_agent}
    r = requests.get(url, headers=headers)
    
    if r.status_code == 200:
        r.encoding=r.apparent_encoding
        soup = BeautifulSoup(r.text, features="html.parser")
        return soup

def get_focus_news(soup):        
    news = soup.find(id="wp_news_w111")
    lis = news.find_all(class_="news_right")
    news=list()
    for each in lis:
        titleTag = each.find(class_="news_title")
        timeTag = each.find(class_="news_time")
        time=timeTag.string
        a = titleTag.find("a")
        title = titleTag.string
        link = a["href"]
        new = dict(title=title, link=link, time=time)
        news.append(new)
        
    return news

def get_focus_news_list():
    url="http://www.cumt.edu.cn"
    soup = getHtml(url)
    focus_news = get_focus_news(soup)
    return focus_news



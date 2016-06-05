import requests
from bs4 import BeautifulSoup


def activity_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://thenewboston.com/forum/recent_activity.php?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        #now we need to convert this data in beautiful soup object
        #only then can we run cool methods on it
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'title'}):
            href = link.get('href')
            title = link.string
            #print(href)
            #print(title)
            single_item_data(href)
        page +=1


def single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    #for item_name in soup.findAll('div',{'class':'post-content'}):
        #print(item_name.string)
    for link in soup.findAll('a'):
        href = link.get('href', {'class': 'user-name'})
        print(href)

activity_spider(1)

from bs4 import BeautifulSoup
import urllib.request
import requests

url = 'https://dantri.com.vn/the-thao/bong-da-trong-nuoc.htm#dt_source=Cate_TheThao&dt_campaign=MenuCate&dt_medium=1'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,'html.parser')

new_feed = soup.find_all('a',class_='news-item__avatar')


#print('Title: {} - Link: {}'.format(title,link))

for result in new_feed:
    title = result.get('title')
    link = result.get('href')
    print('Title: {} - Link: https://dantri.com.vn{}\n'.format(title,link))
    url2 = "https://dantri.com.vn"+link
    page2 = urllib.request.urlopen(url2)
    soup2 = BeautifulSoup(page2,'html.parser')
    titles = soup2.find('div',class_='dt-news__content').find_all('p')
    print(titles)
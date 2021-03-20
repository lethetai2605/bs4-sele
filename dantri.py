from bs4 import BeautifulSoup
import urllib.request

number_page = 2
i =1
while( i<=number_page):
    print ("TRANG THU:"+str(i))
    
    url = 'https://dantri.com.vn/the-gioi/bau-cu-tong-thong-my-2020/trang-{}.htm'.format(i)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page,'html.parser')


    new_feed = soup.find_all('a',class_='news-item__avatar')
    f = open("dantri_page{}.txt".format(i),'w',encoding = 'utf-8')
    for result in new_feed:
        sub_url =  "https://dantri.com.vn"+result.get('href')
        print ("Title:"+result.get('title')+"\n"+"Link:"+sub_url)
        sub_page = urllib.request.urlopen(sub_url)
        sub_soup =BeautifulSoup(sub_page,'html.parser')
        sub_new_feed = sub_soup.find('div',class_='dt-news__content').find_all('p')
        print ("Noi dung:")
        f.write("Title:"+result.get('title')+"\n"+"Link:"+sub_url+"\n")
        f.write("Noi dung:")
        for subnf in sub_new_feed:
            print (subnf.get_text())
            f.write(subnf.get_text())
        print ("\n")
        f.write("\n\n")
        
    f.close()
        
    
    i = i + 1
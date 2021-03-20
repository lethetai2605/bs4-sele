import requests
from bs4 import BeautifulSoup
from secrets import username,password
from time import sleep
from robobrowser import RoboBrowser
from werkzeug.utils import cached_property

browser = RoboBrowser(
        history=True,
        user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'
    )
browser.open('https://m.facebook.com')
form = browser.get_form(id='login_form')

form['email'].value = username
form['pass'].value = password

browser.submit_form(form)

# POST_LOGIN_URL = "https://www.facebook.com/login"

# with requests.Session() as session:

#     sleep(5)
#     page = requests.get("https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit=20&shown_ids=100057212151011%2C100056552215448%2C100056127935351%2C100053789405388%2C100053609945466%2C100051387796520%2C100050407750028%2C100049740621835%2C100049248944423%2C100045831321224&total_count=530&ft_ent_identifier=10158503274236785")
#     page.raise_for_status()
#     # print(page.text)
# soup = BeautifulSoup(page.content,'html.parser')

# names = soup.find_all('h3',class_='bj')
# print("tai pro")

# for name in names:
#     print(name.get_text())
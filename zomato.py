# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup

# url = 'https://www.zomato.com/jakarta/top-restaurants'

# req = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()
# page_soup = soup(webpage, "html.parser")
# print(page_soup)

import requests
from bs4 import BeautifulSoup

#api
headers = {'user-key': '5472bb5f64b2814b1173b59e4b8635e3'}


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}
page = requests.get("https://www.zomato.com/jakarta/sedjuk-bakmi-kopi-scbd/reviews?page=1&sort=dd&filter=reviews-dd", headers=headers)

print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')
revs = soup.find_all('p')
rev_list = revs[0].find_all("p",attrs={"class": "sc-1hez2tp-0 sc-kIWQTW jeOzvZ"})
print(rev_list)



import requests
from bs4 import BeautifulSoup

page = requests.get("http://quotes.toscrape.com/")

# print(page.status_code)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
quotes = soup.find_all('div', class_='quote')
print(quotes)

for q in quotes:
    quote = q.find('span', class_='text').text
    author = q.find('small', class_='author').text
    tags = [tag.text for tag in q.find('div', class_='tags').find_all('a', class_='tag')]
    
    print(quote)
    print(author)
    print(tags)
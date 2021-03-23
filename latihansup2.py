import requests
from bs4 import BeautifulSoup

page = requests.get("http://quotes.toscrape.com/")

# print(page.status_code)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
quote = soup.find('span', class_='text').text
print("\n\n\n\n\n\n\n", quote)
author = soup.find('small', class_='author').text
print(author, "\n\n\n\n\n\n\n\n\n")
tags = [tag.text for tag in soup.find('div', class_='tags').find_all('a', class_='tag')]
print(tags)
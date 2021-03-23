import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.goodreads.com/author/quotes/3354.Haruki_Murakami")

print(page.status_code)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
quotes = soup.find('div', class_='quoteText')
print(quotes)

# author = soup.find('small', class_='author').text
# print(author, "\n\n\n\n\n\n\n\n\n")
# tags = [tag.text for tag in soup.find('div', class_='tags').find_all('a', class_='tag')]
# print(tags)
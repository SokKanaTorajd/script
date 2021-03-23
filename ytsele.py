# tutorial selenium youtube

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")

result = []
stack = ['https://inet.detik.com/']

driver = webdriver.Chrome(options=chrome_options)
while len(stack) > 0 and len (result) < 5:
    driver.get(stack.pop())
    result.append({driver.title})
    elements = driver.find_elements_by_tag_name("a")
    for e in elements:
        url = e.get_attribute('href')
        if url not in stack and url not in result and '#' not in url and 'https://inet.detik.com/' in url:
            stack.append(url)
print(result)
driver.close()
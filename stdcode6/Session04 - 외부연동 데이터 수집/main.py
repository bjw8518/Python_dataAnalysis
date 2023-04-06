import requests
from bs4 import BeautifulSoup

url ="https://finance.naver.com/item/main.naver?code=000660"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price = soup.select_one("#_nowVal")
print(price)
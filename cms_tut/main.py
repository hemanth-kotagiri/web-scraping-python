import requests
from bs4 import BeautifulSoup

data = requests.get("https://coreyms.com/")

soup = BeautifulSoup(data.text, "lxml")

print(soup.title.text)
print(soup.find("h1"))
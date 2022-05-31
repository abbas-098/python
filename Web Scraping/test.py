import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.gov.uk/bank-holidays")
c = r.content
soup = BeautifulSoup(c,"html.parser")
print(soup)
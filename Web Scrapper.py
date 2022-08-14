import requests
from bs4 import BeautifulSoup
Print("Enter the link")
req = requests.get(input())
soup = BeautifulSoup(req.content, "html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://chennai.vit.ac.in/computer-science-engineering-chennai/faculty/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
for name in soup.find_all("h3","item-title"):
    print(name.text)

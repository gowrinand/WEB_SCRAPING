from bs4 import BeautifulSoup
from urllib.request import urlopen
for i in range(35): 
    url = "https://www.iitm.ac.in/faculty?field_faculty_name_value=&field_faculty_department_value=&page="+str(i)
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    for name in soup.find_all("h3"):
        print(name.text)

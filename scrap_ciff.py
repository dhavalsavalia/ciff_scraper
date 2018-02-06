import requests
from bs4 import BeautifulSoup

url = "https://www.clevelandfilm.org/festival/festival-guide/films-a-z"
file = open('links.html', 'a')

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

g_data = soup.find_all('ul', {'class': 'span5'})

for item in g_data:
    h_data = item.find_all('a')
    for item2 in h_data:
        new_link = "<p><a href='https://www.clevelandfilm.org/{}'>{}</a></p>\n".format(item2.get('href'), item2.text)
        file.write(new_link)
        print(item2.get('href'), item2.text)

file.close()

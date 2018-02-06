import requests
from bs4 import BeautifulSoup
from slugify import slugify

with open('links.html') as fp:
    soup = BeautifulSoup(fp, "html.parser")

# for link in soup.find_all('a'):
r = requests.get("https://www.clevelandfilm.org/films/2017/zip-zap-and-the-captains-island")
movie_soup = BeautifulSoup(r.content, "html.parser")
main_content = movie_soup.find('div', {'id': 'ciff-left'})
title = main_content.find('h1', {'itemprop': 'name'})
slugged_title = slugify(title.text)
f = open("{}.html".format(slugged_title),"w+") # line where problem lies
info = main_content.find('p', {'class': 'info'})
country_meta = info.find('span', {'itemprop': 'countryOfOrigin'})
country = country_meta.find('span', {'itemprop': 'name'})
runtime = info.find('span', {'itemprop': 'duration'})
description_meta = main_content.find('span', {'itemprop': 'description'})
description = description_meta.find('p')
write_data = '''<h1>{}</h1>    
<p>Country: {}</p>
<p>Runtime: {}</p>
<p>Description: {}</p>'''.format(title.text, country.text, runtime.text, description.text)
f.write(write_data)
f.close()

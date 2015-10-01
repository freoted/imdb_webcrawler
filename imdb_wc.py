# notes
# imdb web crawler

# Example - Shawshank Redemption
# http://www.imdb.com/title/tt0111161/
# Page of filming locations
# http://www.imdb.com/title/tt0111161/locations?ref_=tt_dt_dt

# Relevant div id
# <div id="filming_locations_content" class="header">

import requests
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/chart/top?ref_=nv_ch_250_4'
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")


for link in soup.find_all('td',{'class':'titleColumn'}):
	href = link.find('a').get('href')
	print (href)
print ('done')
	

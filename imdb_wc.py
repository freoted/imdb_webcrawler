# notes
# imdb web crawler

# Example - Shawshank Redemption
# http://www.imdb.com/title/tt0111161/
# Page of filming locations
# http://www.imdb.com/title/tt0111161/locations?ref_=tt_dt_dt

# Relevant div id
# <div id="filming_locations_content" class="header">

#import dependencies
import requests
from bs4 import BeautifulSoup

#This page lists the current top 250 movies on imdb
url = 'http://www.imdb.com/chart/top?ref_=nv_ch_250_4'

#grabs all the text from this page, and makes it a BeautifulSoup object
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

#searches through BS4 object for all the title links
for link in soup.find_all('td',{'class':'titleColumn'}):
	href = link.find('a').get('href')
	#just print bit of link that you need
	short_href = href[:17]
	#http://www.imdb.com/title/tt0111161/locations?ref_=tt_dt_dt
	#locationlink
	location_link = 'http://www.imdb.com' + short_href + 'locations?ref_=tt_dt_dt'
	print (location_link)
	
print ('done')
	

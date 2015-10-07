
#import dependencies
import requests
from bs4 import BeautifulSoup
import re

#This page lists the current top 250 movies on imdb
url = 'http://www.imdb.com/search/title?count=100&groups=oscar_best_picture_winners&sort=year,desc&ref_=nv_ch_osc_3'

#grabs all the text from this page, and makes it a BeautifulSoup object
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

#sets a counter so only the first few links are printed (for testing purposes)
link_count = 0

oscars_f = open('oscars.txt', 'a')
print ("printing file")
#searches through BS4 object for all the title links
for link in soup.find_all('td',{'class':'title'}):
        #limits search results to first three links (testing purposes)
        #if link_count < 5:
        href = link.find('a').get('href')
        #just print bit of link that you need
        short_href = href[:17]
        #http://www.imdb.com/title/tt0111161/locations?ref_=tt_dt_dt
        #locationlink
        location_link = 'http://www.imdb.com' + short_href + 'locations?ref_=tt_dt_dt'
        title = link.find('a')
        location_source_code = requests.get(location_link)
        location_plain_text = location_source_code.text
        location_soup = BeautifulSoup(location_plain_text, "html.parser")

        #prints name of location only
        for loc_link in location_soup.find_all('div',{'id':'filming_locations_content'}):
                for dt_links in loc_link.find_all('dt'):
                        for loc_name in dt_links.find_all('a'):
                                oscars_f.write((title.contents[0])+ "," + (loc_name.contents[0]))
                #link_count = link_count + 1
##        else:
##                "program completed"
##                break
                
oscars_f.close()
print ('done')
	

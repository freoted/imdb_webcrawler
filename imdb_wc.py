# notes
# imdb web crawler

#Future work:
##Get rid of the 'x of y found this interesting'
##Change initial page to best picture winner from imdb instead of Top 250 movies.
##Get name of the movie
##Use while loop to limit number of results (for testing) - DONE
##Get map format that calculates number of overlapping variables and displays that no
##on the map
##Put each variable (movie name, link, location) in a new column, or seperated by comma
##Export to excel?


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

#sets a counter so only the first few links are printed (for testing purposes)
link_count = 0

#searches through BS4 object for all the title links
for link in soup.find_all('td',{'class':'titleColumn'}):
        #limits search results to first three links (testing purposes)
        if link_count < 3:
                href = link.find('a').get('href')
                #just print bit of link that you need
                short_href = href[:17]
                #http://www.imdb.com/title/tt0111161/locations?ref_=tt_dt_dt
                #locationlink
                location_link = 'http://www.imdb.com' + short_href + 'locations?ref_=tt_dt_dt'
                print (location_link)
                
                location_source_code = requests.get(location_link)
                location_plain_text = location_source_code.text
                location_soup = BeautifulSoup(location_plain_text, "html.parser")

                #prints name of location but also '7 of 7 found this interesting'
                for loc_link in location_soup.find_all('div',{'id':'filming_locations_content'}):
                        for i in loc_link.find_all('a'):
                                print (i.contents[0])
                link_count = link_count + 1
        else:
                "program completed"
                break
                
print ('done')
	

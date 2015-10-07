# notes
# imdb web crawler

#This version - try reusing function for BeautifulSoup

#import dependencies
import requests
from bs4 import BeautifulSoup
import re

def soupRecipe(url):
        source_code = requests.get(url)
        plain_text = source_code.text
        return BeautifulSoup(plain_text, "html.parser")


def main():
        #open oscars file
        oscars_f = open('oscars.txt', 'a')
        print ("printing file")

        #This page lists the current best picture winning movies on imdb
        best_pic_url = 'http://www.imdb.com/search/title?count=100&groups=oscar_best_picture_winners&sort=year,desc&ref_=nv_ch_osc_3'

        #call soup function
        best_pic_soup = soupRecipe(best_pic_url)
                
        #searches through BS4 object for all the title links
        for link in best_pic_soup.find_all('td',{'class':'title'}):
                href = link.find('a').get('href')
                #just print bit of link that you need
                short_href = href[:17]
                print (short_href)

                location_link = 'http://www.imdb.com' + short_href + 'locations?ref_=tt_dt_dt'

                title = link.find('a')

                location_soup = soupRecipe(location_link)

                #prints name of location only
                for loc_link in location_soup.find_all('div',{'id':'filming_locations_content'}):
                        for dt_links in loc_link.find_all('dt'):
                                for loc_name in dt_links.find_all('a'):
                                        oscars_f.write((title.contents[0])+ "," + (loc_name.contents[0]))

                
        oscars_f.close()
        print ('done')
        

main()

# notes
# imdb web crawler

#This version - add country of origin

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

                #get title so you can print it in text file later
                title = link.find('a')
                href = link.find('a').get('href')
                page_link = 'http://www.imdb.com' + href
                location_link = page_link + 'locations?ref_=tt_dt_dt'

                country_of_origin_soup = soupRecipe(page_link)
                
                for item1 in country_of_origin_soup('div', {'class' : 'txt-block'}):
                        for item2 in item1.find_all('a'):
                                if '/country/' in item2['href']:
                                        print (item2.contents[0])
                        
                filming_location_soup = soupRecipe(location_link)
                
                for loc_link in filming_location_soup.find_all('div',{'id':'filming_locations_content'}):
                        for dt_links in loc_link.find_all('dt'):
                                for loc_name in dt_links.find_all('a'):
                                        oscars_f.write((title.contents[0])+ "," + (loc_name.contents[0]))

                
        oscars_f.close()
        
main()


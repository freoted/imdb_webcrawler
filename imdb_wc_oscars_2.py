# notes
# imdb web crawler

#This version - make function for BeautifulSoup

#import dependencies
import requests
from bs4 import BeautifulSoup
import re

def soupRecipe(url):
        source_code = requests.get(url)
        plain_text = source_code.text
        return BeautifulSoup(plain_text, "html.parser")


def main():

        #sets a counter so only the first few links are printed (for testing purposes)
        link_count = 0
        
        #This page lists the current top 250 movies on imdb
        url = 'http://www.imdb.com/search/title?count=100&groups=oscar_best_picture_winners&sort=year,desc&ref_=nv_ch_osc_3'

        soup = soupRecipe(url)
                
        #searches through BS4 object for all the title links
        for link in soup.find_all('td',{'class':'title'}):
                href = link.find('a').get('href')
                #just print bit of link that you need
                short_href = href[:17]
                print (short_href)
        print ('done')

main()

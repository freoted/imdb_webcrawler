#this version - print from one link only

#import dependencies
import requests
from bs4 import BeautifulSoup
import re

def soupRecipe(url):
        source_code = requests.get(url)
        plain_text = source_code.text
        return BeautifulSoup(plain_text, "html.parser")


def main():

        slave_url = 'http://www.imdb.com/title/tt2024544'
        slave_soup = soupRecipe(slave_url)
##        print(slave_soup.prettify())

# mydivs = soup.findAll("div", { "class" : "stylelistrow" })
#<div class="txt-block">
#    <h4 class="inline">Country:</h4>

#challenge - at the moment, this is getting every thing from every text block
#how do I get just the links under h4 country?
        for item1 in slave_soup.find_all('div', {'class' : 'txt-block'}):
                print(item1)

        print ('done')
main()

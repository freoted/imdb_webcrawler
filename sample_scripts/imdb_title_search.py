

#Importing the modules

import re

import requests

#Ask for movie title

title = input("Please enter a movie title: ")

#Ask for which year

year = input("which year? ")

#Search for spaces in the title string

raw_string = re.compile(r' ')

#Replace spaces with a plus sign

searchstring = raw_string.sub('+', title)

#Prints the search string

print(searchstring)

#The actual query

url = "http://www.imdbapi.com/?t=" + searchstring + "&y="+year

response = requests.get(url)

print(response.json())

#!/usr/bin/python3

import bs4, csv, sys
import urllib.request as urllib

goodStuff = []

CITY_NAME=sys.argv[1]

for x in range(25):
    mainsite = urllib.urlopen("http://"+CITY_NAME+".craigslist.org/sss/index"+str(x)+'00.html')
    soup = bs4.BeautifulSoup(mainsite)

    links = list(soup.find_all('a'))
    for link in links:
        try:
            link['class']
        except KeyError:
            try:
                link['href']
            except KeyError:
                continue
            if len(link['href'].split('/')) in [3, 4] and link['href'] \
            not in ['https://accounts.craigslist.org', '/sss/']:
                linkTitle=[]
                for letter in str(link.string):
                    if letter != '.':
                        linkTitle.append(letter)
                    else:
                        linkTitle.append(' ')
                linkTitle = "".join(linkTitle)
                goodStuff.append(["http://"+CITY_NAME+"craigslist.org/"+link['href'], linkTitle])

mainFile = open("./links"+CITY_NAME.lower()+".csv", 'w')
thingWriter = csv.writer(mainFile, delimiter=',')
thingWriter.writerows(goodStuff)
print("Average page len:", len(goodStuff)/25)

#!/usr/bin/python3

import timeit

import bs4, csv, sys
import urllib.request as urllib

goodStuff = []
if len(sys.argv) > 1:
    CITY_NAME=sys.argv[1]
else:
    CITY_NAME=input("City name: ")


for x in range(25):
    print(x)
    mainsite = urllib.urlopen("http://"+CITY_NAME+".craigslist.org/sss/index"+str(x)+'00.html')
    soup = bs4.BeautifulSoup(mainsite)

    links = list(soup.find_all('a'))
    for link in links:
        print("New Index", x)
        try:
            link['class']
        except KeyError:
            try:
                link['href']
            except KeyError:
                continue
            if len(link['href'].split('/')) in [3, 4] and link['href'] \
            not in ['https://accounts.craigslist.org', '/sss/'] and len(link['href'].split('/')[-1]):
                linkTitle=[]
                for letter in str(link.string):
                    if letter != ',':
                        linkTitle.append(letter)
                    else:
                        linkTitle.append(' ')
                linkTitle = "".join(linkTitle)
                lat, lon = 0, 0
                try:
                    subsite = urllib.urlopen("http://"+CITY_NAME+".craigslist.org/"+link['href'])
                    subsoup = bs4.BeautifulSoup(subsite)
                    sublinks = list(subsoup.find_all('div'))
                    for sublink in sublinks:
                        print(".o.", end="")
                        try:
                            if sublink['id'] == "map":
                                print("Success", end=" ")
                                lat, lon = sublink['data-latitude'], sublink['data-longitude']
                                continue
                        except:
                            pass
                except:
                    pass
                goodStuff.append(["http://"+CITY_NAME+".craigslist.org"+link['href'], linkTitle, lat, lon])

mainFile = open("./links"+CITY_NAME.lower()+".csv", 'w')
thingWriter = csv.writer(mainFile, delimiter=',')
thingWriter.writerows(goodStuff)


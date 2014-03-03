#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import cgitb, cgi
cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print()

import bs4
def Search(name, body, termstring):
    terms = termstring.split(" ")
    soup = bs4.BeautifulSoup(body)
    sections = soup.find_all('section')
    body = ""
    for section in sections:
        print()
        try:
            print(2)
            if section['id'] == 'postingbody':
                body = section.string  
                print(body)
        except:
            print(3)  
    for term in terms:
        if body.lower().find(term.lower()) != -1 or name.lower().find(term.lower()) != -1:
            return True
    return False

print("""<html>
<head>
<title>Search Results</title>
<link rel="stylesheet" href="../searchstyle.css">
</head>
<body>""")
import csv
f = open("linksauburn.csv", encoding='utf-8')
r = csv.reader(f, delimiter=',')
form = cgi.FieldStorage()
search = form.getvalue("search")
print('<strong>Results:</strong><br><br><br><table>')
try:
    for i in r:
        if Search(name=i[1], body=i[4], termstring=search):
            print("<tr>"+"<a href=\""+i[0]+"\">"+i[0]+"</a></tr><tr></br>"+i[1]+"<br><br><br></tr>")
except ValueError:
    print()
print("""</table></body><footer>
<a href="../about/xu.html">About Zan</a>
<a href="../about/levy.html">About Judah</a>
<a href="../about/index.html">About Craig's Map</a>
<a href="../index.html">Search Hard-Link</a>
</footer></html>""")


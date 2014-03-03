#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# enable debugging

import cgitb, cgi
cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print()

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
print("You searched for %s" % (search))
print('<strong>Results:</strong><br><br><br><table>')
try:
    for i in r:
        print("<tr>"+"<td><a href=\""+i[0]+"\">"+i[0]+"</a></td>"+"<td>"+i[1]+"</td>"+"<td>"+i[2]+"</td>"+"<td>"+i[3]+"</td>"+"</tr>")
except:
    print()
print("""</table></body><footer><br><br><br>
<a href="../about/xu.html">About Zan</a>
<a href="../about/levy.html">About Judah</a>
<a href="../about/index.html">About Craig's Map</a>
<a href="../index.html">Search Hard-Link</a>
</footer></html>""")


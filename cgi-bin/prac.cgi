#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb, cgi
cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print()

print("<html><title>lol</title>")
import csv
f = open("linksauburn.csv", encoding='utf-8')
r = csv.reader(f, delimiter=',')
print('<table border=1>')
try:
    for i in r:
        print("<tr>"+"<td><a href=\""+i[0]+"\">"+i[0]+"</a></td>"+"<td>"+i[1]+"</td>"+"<td>"+i[2]+"</td>"+"<td>"+i[3]+"</td>"+"</tr>")
except:
    print()
print("</table></html>")

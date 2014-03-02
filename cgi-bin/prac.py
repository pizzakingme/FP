#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# enable debugging
import cgi

import cgitb
cgitb.enable()

print("Content-Type: text/plain;charset=utf-8")
print()

import csv
f = open("linksauburn.csv", encoding='utf-8')
r = csv.reader(f, delimiter=',')
print("<table>")
try:
    for i in r:
        print("<tr>"+i[1]+'</tr>')
except:
    print()
print("</table>")

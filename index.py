#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb, csv
cgitb.enable()

print("Content-Type: text/plain;charset=utf-8")
print()

f = open("/resources/linksauburn")
n = f.read()

print(n)

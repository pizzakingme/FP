#!/usr/local/bin/python2
print "Content-type: text/html"
print
print "<pre>"
import os, sys, cgitb
from cgi import escape
cgitb.enable()
print "<strong>Python %s</strong>" % sys.version
keys = os.environ.keys()
keys.sort()
for k in keys:
    print "%s\t%s" % (escape(k), escape(os.environ[k]))
print "</pre>"

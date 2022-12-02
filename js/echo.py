# Python script 
# Prints a table of submitted key=value pairs.
# It should be placed on the web server, in the directory configured for CGI scripts.
# THIS SCRIPT IS FOR DEMONSTRATION PURPOSES ONLY.

import cgi

form = cgi.FieldStorage( )

print('Content-Type:text/html; charset=utf-8')

print('\r\n\r\n' )

print('''<!DOCTYPE HTML>
<html><title>Web Server Response</title>
<style>tr,th,td{border:2px solid Gray}</style>''')

print( '<table style="width:500px"><tr><th>Key<th>Value' )

for i in form.keys( ):
  key = str( i )
  val = str( form.getvalue( key ) )
  print( '<tr><td>' + key + '<td>' + val )
  
print('''</tr></table>
<img src="pwrabyss.gif"> </html>''')
import pyshorteners

url = input('Enter URL : ')

print('URL After Shortening :', pyshorteners.Shortener().tinyurl.short(url))
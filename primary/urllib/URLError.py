from urllib import request, error
try:
    response = request.urlopen('https://kldsfs.com/index.html')
except error.URLError as e:
    print(e.reason)

from urllib import request, error
try:
    response = request.urlopen('https://www.kdfjsl.com/index.html')
except error.HTTPError as e:
    print(e.reason, e.code, seq='\n')
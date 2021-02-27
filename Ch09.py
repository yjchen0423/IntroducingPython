"""Ch. 09"""

"""Ch. 9.1.2"""

import urllib.request as ur
url = 'http://www.example.com'
conn = ur.urlopen(url)
print(conn)
print(conn.status)

data = conn.read()
print(data[:50])

'''Convert the bytes to strings'''
str_data = data.decode('utf8')
print(str_data[:50])


'''use requests'''
import requests
url = 'http://www.example.com'
resp = requests.get(url)
print(resp)
print(resp.text[:50])


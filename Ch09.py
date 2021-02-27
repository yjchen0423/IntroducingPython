"""Ch. 09"""

"""Ch. 9.1.2"""

import urllib.request as ur
url = 'http://www.example.com'
conn = ur.urlopen(url)
print(conn)
print(conn.status)
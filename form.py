
import requests
from base64 import b64encode
import Queue

import  urllib2


bucket = 'leaves'
operator = 'admin'
operator_password = 'weihao123'

url = 'http://v0.api.upyun.com/' + bucket + '/'
method = 'GET'

headers = {
            'Authorization':  'Basic ' + b64encode(operator + ':' + operator_password),
            'x-list-iter': '300'
            }

res = requests.request(method, url, headers=headers)



item_header = res.headers['x-upyun-list-iter']
if item_header == 'g2gCZAAEbmV4dGQAA2VvZg':
    s = res.content.split("`")
    items = s[0].split("\n")
    items =[dict(zip(['name', 'type', 'size', 'time'],
        x.split('\t')))for x in items] + items[1].split()
    print s
    print items







#print res.headers
print res.status_code


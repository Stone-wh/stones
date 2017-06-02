import datetime
import hashlib
import os
import requests
import base64

GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
DATE = datetime.datetime.utcnow().strftime(GMT_FORMAT)
bucket = 'test20160418'
operator = 'admin'
METHOD = 'PUT'
PASSWORD = 'weihao123'
pd = hashlib.md5(PASSWORD.encode('utf-8'))
pd1 = pd.hexdigest()
print(pd1)

p = operator + ':' + PASSWORD
pas = base64.b64encode(p)


#length = str(os.path.getsize('/home/stone/image/20111119822.jpg'))


for f in os.listdir('/home/stone/image/'):
	print (f)

#filename = requests.get.get('/home/stone/image/')
files = {'file': open('/home/stone/image/20111119822.jpg','rb')}



url = 'http://v0.api.upyun.com/test20160418/5.jpg'

headers = {
    'Authorization': 'Basic ' + pas,
    'Date': DATE,
 #   'Content-Length':length,
    }
res = requests.request('PUT',url,data = files ,headers = headers)

if res.status_code == 200:
	print('upload success')
else:
	print('failed')


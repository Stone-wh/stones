import datetime
import hashlib
import requests
import hmac
import os


bucket = ''
operator = ''
operator_password = ''
method = 'PUT'

GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
DATE = datetime.datetime.utcnow().strftime(GMT_FORMAT)
password = hashlib.md5(operator_password.encode('utf-8')).hexdigest()
print password

for root,dirs,files in os.walk('/home/stone/image/'):
        root = root
        dirs = dirs
        files = files
        for f in  files:
            url = 'http://v0.api.upyun.com/'+ bucket +'/' + f
            print url
            URI = '/' + bucket + '/' + f
            print URI
            path =  '/home/stone/image/' + f
            length = os.path.getsize(path)
            sig =  method + '&' + URI +  '&'  + DATE
            print sig
            sign = hmac.new(password,sig,hashlib.sha1).digest().encode('base64').rstrip()
            
            
            
            headers = {
                    'Authorization': 'UPYUN ' + operator + ':' + sign,
                    'Date': DATE,                    
                    'x-upyun-multi-stage':'initiate',
                    'x-upyun-multi-length':str(length)
                    }
            conm = requests.request(method, url, data=open(path), headers=headers)

            headers = {
                    'Authorization': 'UPYUN ' + operator + ':' + sign,
                    'Date': DATE,
                    'x-upyun-multi-stage':'upload',
                    'x-upyun-multi-uuid':conm.headers['x-upyun-multi-uuid'],
                    'x-upyun-part-id':conm.headers['x-upyun-next-part-id']
                    }
            
            
            conm = requests.request(method, url, data=open(path), headers=headers)
           
            headers = {
                    'Authorization': 'UPYUN ' + operator + ':' + sign,
                    'Date': DATE,
                    'x-upyun-multi-stage':'complete',
                    'x-upyun-multi-uuid':conm.headers['x-upyun-multi-uuid'],
                    }
            
            
            conm = requests.request(method, url, data=open(path), headers=headers)

            
            if conm.status_code == 204 or conm.status_code == 201:
                print ('*****upload success*****')
            else:
                print ('****upload failed*****')


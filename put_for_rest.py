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

for root,dirs,files in os.walk('/home/stone/image/'):
        root = root
            dirs = dirs
                files = files
                for f in  files:
                        url = 'http://v0.api.upyun.com/'+ bucket +'/'+ f
                            URI = '/' + bucket + '/' + f
                                path =  '/home/stone/image/' + f
                                    length = os.path.getsize(path)
                                        sig =  method + '&' + URI +  '&'  + DATE
                                            sign = hmac.new(password,sig,hashlib.sha1).digest().encode('base64').rstrip()

                                                headers = {
                                                                'Authorization': 'UPYUN ' + operator + ':' + sign,
                                                                        'Date': DATE,
                                                                                'Content-length':str(length),
                                                                                        }
                                                    conm = requests.request(method, url, data=open(path), headers=headers)
                                                    print conm.status_code
                                                    if conm.status_code == 200:
                                                            print ('*****upload success*****')
                                                        else:
                                                                print ('****upload failed*****')


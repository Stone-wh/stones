
import datetime
import hashlib
import requests
import hmac
import base64
import json

bucket = ''
operator = ''
method = ''
operator_password = 'weihao123'

GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
DATE = datetime.datetime.utcnow().strftime(GMT_FORMAT)
password = hashlib.md5(operator_password.encode('utf-8')).hexdigest()
api = 'http://p0.api.upyun.com/pretreatment/'
URI = '/pretreatment/'
notify_url = 'http://httpbin.org/post'

tasks = [{
        'sources':'/compress/compress.zip',      #压缩时候sources是数组，解压缩是字符串
            'save_as':'/2017/'
            }]

json = base64.b64encode(json.dumps(tasks))
data = {
            'service':bucket,
                'notify_url':notify_url,
                    'app_name':'depress',
                        'tasks':json
                            }


sig = method + '&' + URI + '&' + DATE
sign = hmac.new(password,sig,hashlib.sha1).digest().encode('base64').rstrip()

headers = {
                'Authorization': 'UPYUN ' + operator + ':' + sign,
                            'Date': DATE
                                    }
conm = requests.request(method,api,data=data, headers=headers)


print conm.status_code
print conm.text
print conm.headers

if conm.status_code == 200:
        print ('*****哇哦，bingo*****')
    else:
            print ('****我擦嘞*****')124.193.0.2	mr1.doubanio.com

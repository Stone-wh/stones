import datetime
import hashlib
import requests
import hmac
import base64
import json

bucket = ''
operator = ''
method = ''
operator_password = ''

GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
DATE = datetime.datetime.utcnow().strftime(GMT_FORMAT)
password = hashlib.md5(operator_password.encode('utf-8')).hexdigest()
api = 'http://p0.api.upyun.com/pretreatment/'
URI = '/pretreatment/'
notify_url = 'http://httpbin.org/post'
tasks = [{
        'url' : 'http://pic55.nipic.com/file/20141208/19462408_171130083000_2.jpg',
            'random':False,
                'overwrite':True,
                    'save_as':'/ll/spaiderman.jpg'
                    }]

json = base64.b64encode(json.dumps(tasks))
data = {
            'service':bucket,
                'notify_url':notify_url,
                    'app_name':'spiderman',
                        'tasks':json
                            }


sig =  method + '&' + URI +  '&'  + DATE
sign = hmac.new(password,sig,hashlib.sha1).digest().encode('base64').rstrip()

headers = {
                'Authorization': 'UPYUN ' + operator + ':' + sign,
                        'Date': DATE,
                                }
conm = requests.request(method,api,data = data, headers = headers)


print conm.status_code
print conm.text
print conm.headers

if conm.status_code == 200:
        print ('*****哇哦，拉取成功*****')
    else:
            print ('****我擦嘞，拉取失败*****')

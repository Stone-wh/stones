#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import hashlib
import requests
import hmac
import base64
import json

bucket = ''
operator = ''
operator_password = ''
method = 'POST'


GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
DATE = datetime.datetime.utcnow().strftime(GMT_FORMAT)
password = hashlib.md5(operator_password.encode('utf-8')).hexdigest()

api = 'http://p0.api.upyun.com/pretreatment/'
URI = '/pretreatment/'

sig = method + '&' + URI + '&' + DATE
sign = hmac.new(password,sig,hashlib.sha1).digest().encode('base64').rstrip()
print sign
notify_url = 'http://httpbin.org/post'

tasks = [{
        'type':'video',
        'avopts':'/s/240p(4:3)/as/1/r/30',
        'retun_info': True,
        'save_as':'/a/b.mp4'
            }]

jsons = base64.b64encode(json.dumps(tasks))
data = {
            'service': bucket,
            'notify_url': notify_url,
            'accept': json,
            'source': '/ai.mp4',
            'tasks': jsons
                            }




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
        print ('****我擦嘞*****')




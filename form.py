#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import hashlib
import requests
import hmac
import os
import time
import base64
import json
from requests_toolbelt import MultipartEncoder




bucket = ''
operator = ''
operator_password = ''



method = 'POST'
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
DATE = datetime.datetime.utcnow().strftime(GMT_FORMAT)
expiration = int(time.time()) + 1000000
password = hashlib.md5(operator_password.encode('utf-8')).hexdigest()

for root, dirs, files in os.walk('/home/stone/image/', topdown=False):
        root = root
        dirs = dirs
        files = files
        for f in files:
                url = 'http://v0.api.upyun.com/' + bucket
                URI = '/' + bucket
                path = '/home/stone/image/' + f
                p = {'bucket': bucket,
                     'save-key': '/form/{year}/{mon}/{day}/{hour}_{min}_{sec}_{filename}{.suffix}',
                     'expiration': expiration
                     }
                policy = base64.b64encode(json.dumps(p))

                sig = method + '&' + URI + '&' + policy

                sign = hmac.new(password, sig, hashlib.sha1).digest().encode('base64').rstrip()
                payload = MultipartEncoder(
                    fields={
                        'authorization': 'UPYUN ' + operator + ':' + sign,
                        'policy': policy,
                        'file': ('filename', open(path, 'rb'))
                    }
                )
                re = requests.post(url, data=payload, headers={'Content-Type': payload.content_type})
                try:
                    status = re.status_code
                    if status == 200:
                        content = re.text
                except Exception as e:
                    print e
                time.sleep(2)
                print re.text
                if re.status_code == 200:
                    print ('*****upload success*****')
                else:
                    print ('****upload failed*****')


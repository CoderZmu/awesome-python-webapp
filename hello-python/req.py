from urllib import request
import json
req = request.Request(url='http://news-at.zhihu.com/api/4/news/latest')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', json.loads(f.read().decode('utf-8')))
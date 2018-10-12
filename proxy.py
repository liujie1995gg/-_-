import re,time,redis
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request
from urllib.request import urlopen
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
url = 'http://www.xicidaili.com/wt/'
class R(object):
    def __init__(self):
        r_pool =redis.ConnectionPool(host='127.0.0.1',db=0,password=None,
                                     port=6379)
        self.redis_obj = redis.Redis(connection_pool=r_pool)
    def setex(self,name,value,time):
        return self.redis_obj.setex(name,value,time)

    def get(self,name):
        return self.redis_obj.get(name)

def url_response(url,redis_obj):
    response = urlopen(Request(url,headers=headers)).read()
    response = response.decode()
    pattern='<td>(.*?)</td>\s+<td>(\d+)</td>\s+<td>\s+<a href="/.*?">[\u4e00-\u9fa5]+</a>\s+</td>\s+<td class="country">高匿</td>\s+<td>(\w+)</td>\s+<td class="country">\s+<div title="(\d.\d+)秒"'
    regex = re.compile(pattern)
    ip_list = regex.findall(response)
    for i in ip_list:
        out_time = float(i[3])
        ip_ = i[0]+':'+i[1]
        if redis_obj.get(ip_):
            print('重复数据跳过')
            continue
        if out_time < 1:
            redis_obj.setex(ip_,1,60*30)
            print('插入成功，',ip_)
        else:
            pass
r = R()
T = ThreadPoolExecutor(4)
for i in range(1,5):
    _ = url+str(i)
    T.submit(url_response,_,r)
print('执行完成 ')
T.shutdown()

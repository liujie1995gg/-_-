import time,datetime

def show_time(times=None):
      '''#无参返回当前格式化时间，文本型
    如果time = None,则取当前时间，
    有参，返回时间类型文本'''
    if times == None:
        times = time.strftime( '%Y-%m-%d %H:%M:%S',time.localtime())
        return times#返回时间文本型
    else:
        times = datetime.datetime.strptime(times,'%Y-%m-%d %H:%M:%S')
        return times

a = show_time('2018-09-17 09:38:58')
print(a)
b = show_time()
b = show_time(b)
print(b)
print(b -a)


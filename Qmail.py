import smtplib,time
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import asyncio
my_sender='1043453579@qq.com' # 发件人邮箱账号
my_pass = 'niyusfcmzdwmbcge' # 发件人邮箱密码
my_user=['937527422@qq.com'] # 收件人邮箱账号，
async def mail(my_user,tp=False):
    if not tp:
        try:
            msgroot = MIMEMultipart('related',)
            msg=MIMEText('填写邮件内容[验证码]<a href="http://www.baidu.com">这里是一个跳转链接</a><h1>图片演示</h1><p><img src="cid:image1"></p>','html','utf-8')
            msgroot.attach(msg)
            msgroot['From']=formataddr(["来自刘大大",my_sender]) # 显示发件人
            msgroot['To']=formataddr(["FK",my_user]) # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msgroot['Subject']="设置标题" # #=显示标题
            server=smtplib.SMTP_SSL("smtp.qq.com", 465) # 发件人邮箱中的SMTP服务器，端口是25
            #*************发送图片
            # fp = open('101.jpg', 'rb')
            # msgImage = MIMEImage(fp.read())
            # fp.close()
            # 定义图片 ID，在 HTML 文本中引用
            # msgImage.add_header('Content-ID', '<image1>')
            # msgroot.attach(msgImage)
            #*************
            server.login(my_sender, my_pass) # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender,[my_user,],msgroot.as_string()) # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit() # 关闭连接
            print("邮件发送成功")
        except Exception as e : # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            print(e)
            print("邮件发送失败")
            with open('false1.txt','w+') as f:
                f.write(my_user+'\n')
look = asyncio.get_event_loop()
a = []
b = True
t = time.time()

if len(my_user)>1:
    for i in my_user:
        a.append(mail(i))
        if len(a)>10:
            print('进来一次')
            look.run_until_complete(asyncio.wait(a))
            a=[]
            b = False
    if b:
        look.run_until_complete(asyncio.wait(a))
else:
    look.run_until_complete(mail(my_user[0]))
print(time.time()-t,'完成时间')
look.close()
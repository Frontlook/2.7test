#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

mail_host="smtp.126.com"  #设置服务器
mail_user="r3390660@126.com"    #用户名
mail_pass="rongzhongyu@106"   #口令

receivers = ['597234417@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = formataddr(["东方红", 'r3390660@126.com'])
message['To'] = formataddr(["太阳升", '597234417@126.com'])
message['Subject']="Test email"

try:
    smtpObj = smtplib.SMTP(mail_host, 25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(mail_user, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
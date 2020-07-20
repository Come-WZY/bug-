# from email.mime.text import MIMEText
# """
# SMTP是发送邮件的协议,python内置对SMTP的支持可以发送纯文本邮件/HTML邮件以及带附件的邮件.
# """
# #导入python内置的SMTP
# msg=MIMEText("hello,send by python3","plain","utf8")
# #输入电子邮件地址和口令:
# from_addr=input("From:")#2294780201@qq.com
# password=input("password:")#密码:
# #输入收件人地址:
# to_addr=input("To:")#731957734@qq.com
# #输入SMTP服务器地址:
# smtp_server=input("SMTP server:")#smtp.qq.com
#
# import smtplib
#
# server=smtplib.SMTP(smtp_server,25)
#
# server.set_debuglevel(1)
#
# server.login(from_addr,password)#登录服务器
#
# server.sendmail(from_addr,[to_addr],msg.as_string())
#
# server.quit()




# from email.mime.text import MIMEText
# import smtplib
#
# # 实例化MIMEText 第一个参数邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定用utf-8编码保证多语言兼容性。
# msg = MIMEText('此邮件为测试邮件!', 'plain', 'utf-8')
# from_addr = input('From:')  # 发件人地址(邮箱)
# password = input('password:')  # 发件人地址(邮箱)密码 这里指授权码##  aufkqrbgetsgbaih
# to_addr = input('To:')  # 收件人地址(邮箱)
# smtp_server = input('SMTP server:')  # SMTP服务器地址 不同的供应商有不同的服务器比如QQ的smtp.qq.com 163的smtp.163.com
#
#
# server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口一般是25 SSL端口一般为465
# server.set_debuglevel(1)  # 与SMTP服务器交互的所有信息
# server.login(from_addr, password)  # 验证登录
# server.sendmail(from_addr, [to_addr], msg.as_string())  # sendmail方法发送邮件，参数一发件人地址，
# # 参数二可以为一个list由于可以一次发给多个人 参数三邮件正文是一个str，as_string()把MIMEText对象变成str
# server.quit()

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(0)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
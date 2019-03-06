#encoding=utf-8
#使用stmp发送一封简单邮件
#1、导入模块
import email
from email.mime.text import  MIMEText
import smtplib
import  traceback
mark=False
try:
  session=smtplib.SMTP_SSL("smtp.qq.com",465,30)
  msg=MIMEText("test email  smtp this is a test email! ","plain")
  msg['subject']='Python 发送邮件测试'
  msg['from']='1634217611@qq.com'
  msg['to']='1634217611@qq.com'
  session.login('1634217611@qq.com',"yhevfpvfpioofaeg")
  session.sendmail('1634217611@qq.com','1634217611@qq.com',str(msg))
  mark=True
except Exception as  e:
    print(traceback.print_exc())
if mark==True:
    print("邮件发送成功!")



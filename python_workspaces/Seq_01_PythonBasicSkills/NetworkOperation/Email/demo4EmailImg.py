# 发送IMG的电子信箱
"""
1、导入模块
2、设置邮件会话对象
3、设置邮件信息（邮件内容，邮件类型，标题，发送人，接收人）
4、登录发送邮箱
5、发送邮件
"""
import smtplib
import traceback
from email.mime.text import MIMEText

try:
    session = smtplib.SMTP_SSL("smtp.qq.com", 465, 30)
    message = MIMEText(
        "<h1>这是HTML邮件</h1><h2>是带有图片的</h2><p>demo</p><img src='http://img05.tooopen.com/images/20150820/tooopen_sy_139205349641.jpg'/>",
        "html", "utf-8")
    message['subject'] = "HTML邮件中包含图片"
    message['from'] = "419795232@qq.com"
    message['to'] = "jianglp2018@qq.com"
    session.login("419795232@qq.com", "此处填写您的授权码")
    session.sendmail("419795232@qq.com", "jianglp2018@qq.com", str(message))
    print("Ok")
except:
    print(traceback.print_exc())

# 发送纯文本的电子信箱
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
    message = MIMEText("这是一封纯文本的邮件,测试使用！", "plain", "utf-8")
    message['subject'] = "纯文本"
    message['from'] = "419795232@qq.com"
    message['to'] = "2357194926@qq.com"
    session.login("419795232@qq.com", "此处填写您的授权码")
    session.sendmail("419795232@qq.com", "2357194926@qq.com", str(message))
    print("Ok")
except:
    print(traceback.print_exc())

# coding=utf-8
# 1、导入模块
import smtplib
from email.mime.text import MIMEText
import traceback

result = False
# 2、邮件会话(SSL)对象
session = smtplib.SMTP_SSL("smtp.qq.com", 465, 30)
# 3、设置邮件信息(包括正文、邮件类型 、标题、发送人、接收人)
try:
    # 设置正文为符合邮件格式的HTML内容
    msg = MIMEText("<h1>Hi</h1><p>test mail from czf3</p><p><img src='https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo_top_ca79a146.png'/></p>", 'html')

    # 设置邮件标题
    msg['subject'] = "This is a python stmp test mail"

    # 设置发送人
    msg['from'] = "1634217611@qq.com"

    # 设置邮件接收人
    msg['to'] = "1634217611@qq.com"
    # 4、 登陆邮箱(后面那个是授权码)
    session.login("1634217611@qq.com", "yhevfpvfpioofaeg")
    # 5、 发送邮件
    session.sendmail("1634217611@qq.com", "1634217611@qq.com", msg.as_string())
    result = True
except Exception:
    traceback.print_exc()
finally:
    print(result)
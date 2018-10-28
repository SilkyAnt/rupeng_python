#发送带附件的邮件   不知道为什么图片不行
'''
1、导入模块
2、设置邮件会话对象
3、设置邮件信息（邮件内容，邮件类型，标题，发送人，接收人）
4、登录发送邮箱
5、发送邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback
try:
    session = smtplib.SMTP_SSL("smtp.qq.com",465,30)
    message = MIMEMultipart()
    message['subject'] = "发送带附件的邮件"
    message['from'] = "419795232@qq.com"
    message['to']="jianglp2018@qq.com"

    emailTest = MIMEText("<h5>这是用Python开发带附近啊的邮件例子</h5>","html","utf-8")
    message.attach(emailTest)

    att1 = MIMEText(open('龙猫.jpg', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # 附件名称非中文时的写法
    # att["Content-Disposition"] = 'attachment; filename="readme.txt")'
    # 附件名称为中文时的写法
    att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", "龙猫.jpg"))
    message.attach(att1)

    session.login("419795232@qq.com","此处填写您的授权码")
    session.sendmail("419795232@qq.com","jianglp2018@qq.com",str(message))
    print("Ok")
except:
    print(traceback.print_exc())

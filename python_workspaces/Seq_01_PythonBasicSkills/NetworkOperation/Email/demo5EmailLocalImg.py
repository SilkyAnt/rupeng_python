#发送一张本地IMG的电子信箱
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
from email.mime.image import MIMEImage
import traceback
try:
    session = smtplib.SMTP_SSL("smtp.qq.com",465,30)
    message = MIMEMultipart()

    htmlText='''
        <h1>信箱里包含本地图片</h1>
        <img src="cid:image1"></img>
    '''
    emailText = MIMEText(htmlText,"html","utf-8")

    f=open("龙猫.jpg",mode="rb")
    emailImg = MIMEImage(f.read())
    f.close()

    emailImg.add_header("Content-ID","image1")

    message.attach(emailText)
    message.attach(emailImg)

    message['subject'] = "HTML邮件中包含本地图片"
    message['from'] = "419795232@qq.com"
    message['to']="jianglp2018@qq.com"
    session.login("419795232@qq.com","此处填写您的授权码")
    session.sendmail("419795232@qq.com","jianglp2018@qq.com",str(message))
    print("Ok")
except:
    print(traceback.print_exc())

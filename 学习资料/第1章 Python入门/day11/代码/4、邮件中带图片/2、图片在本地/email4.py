#encoding=utf-8
#在邮件中显示图片
#1、导入模块
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import traceback
try:
    # 2、邮件会话(SSL)对象
    session=smtplib.SMTP_SSL("smtp.qq.com",465,30)
    # 3、创建一个可以带图片和超链接的MIMEMultipart对象
    msg=MIMEMultipart("related")
    # 4、设置邮件信息(包括正文、邮件类型 、标题、发送人、接收人)
    msg['subject']='邮件中有图片'
    msg['from']='1634217611@qq.com'
    msg['to']='1634217611@qq.com'
    # 邮件正文内容
    mail_msg = """
      <p>Python 邮件发送测试...</p>
      <p><a href="http://www.rupeng.com">如鹏教育网</a></p>
      <p>图片演示：</p>
      <p><img src="cid:image1"></p>
      """
    msg.attach(MIMEText(mail_msg,"html","utf-8"))
    # 5、选中图片
    img=open("1.jpg",mode="rb")
    emailImg=MIMEImage(img.read())
    img.close()
    #6、定义图片ID，在HTML文本中引用
    emailImg.add_header("Content-ID","image1")
    # 7、 登陆邮箱
    msg.attach(emailImg)
    session.login('1634217611@qq.com', "yhevfpvfpioofaeg")
    # 8、 发送邮件  
    session.sendmail('1634217611@qq.com', '1634217611@qq.com', str(msg))
    print("ok")
except:
    print(traceback.print_exc())



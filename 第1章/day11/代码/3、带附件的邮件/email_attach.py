#coding=utf-8
#1、导入模块 
import smtplib  
from email.mime.text import MIMEText  
import traceback
from email.mime.multipart import MIMEMultipart
result = False 
#2、邮件会话(SSL)对象  
session = smtplib.SMTP_SSL("smtp.qq.com", 465, 30) 
try:  
#3、创建一个带附件的实例
    message = MIMEMultipart()
#4、设置邮件信息(包括正文、邮件类型 、标题、发送人、接收人) 
        # 设置发送人 
    message['From'] = "12345678@qq.com" 
        # 设置邮件接收人 
    message['To'] = "12345678@qq.com" 
        # 设置邮件标题  
    message['Subject'] = 'Python SMTP 邮件附件测试'   
    #邮件正文内容
    message.attach(MIMEText('这是Python 邮件附件发送测试……', 'plain', 'utf-8'))    
    # 5、构造附件1，传送当前目录下的 czf.txt 文件
    att1 = MIMEText(open('czf.txt', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="czf.txt"'
    message.attach(att1)  

#5、 登陆邮箱  
    session.login("12345678@qq.com", "czf_qq_96944")  
#6、 发送邮件  
    session.sendmail("12345678@qq.com","12345678@qq.com", message.as_string())  
    result = True  
except Exception:  
    traceback.print_exc()  
finally:  
    print(result)  
#coding=utf-8
#1������ģ�� 
import smtplib  
from email.mime.text import MIMEText  
import traceback
from email.mime.multipart import MIMEMultipart
result = False 
#2���ʼ��Ự(SSL)����  
session = smtplib.SMTP_SSL("smtp.qq.com", 465, 30) 
try:  
#3������һ����������ʵ��
    message = MIMEMultipart()
#4�������ʼ���Ϣ(�������ġ��ʼ����� �����⡢�����ˡ�������) 
        # ���÷����� 
    message['From'] = "12345678@qq.com" 
        # �����ʼ������� 
    message['To'] = "12345678@qq.com" 
        # �����ʼ�����  
    message['Subject'] = 'Python SMTP �ʼ���������'   
    #�ʼ���������
    message.attach(MIMEText('����Python �ʼ��������Ͳ��ԡ���', 'plain', 'utf-8'))    
    # 5�����츽��1�����͵�ǰĿ¼�µ� czf.txt �ļ�
    att1 = MIMEText(open('czf.txt', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # �����filename��������д��дʲô���֣��ʼ�����ʾʲô����
    att1["Content-Disposition"] = 'attachment; filename="czf.txt"'
    message.attach(att1)  

#5�� ��½����  
    session.login("12345678@qq.com", "czf_qq_96944")  
#6�� �����ʼ�  
    session.sendmail("12345678@qq.com","12345678@qq.com", message.as_string())  
    result = True  
except Exception:  
    traceback.print_exc()  
finally:  
    print(result)  
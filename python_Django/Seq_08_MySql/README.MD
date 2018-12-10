### 连接MySQL
* 需要的包
    * 安装命令：pip install mysqlclient
* 配置settings中的参数
* 初始化数据库
    * 需要执行的命令
        * python manage.py makemigrations
        * python manage.py migrate
* 设置上下文
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'Seq_08_MySql.settings'
django.setup()

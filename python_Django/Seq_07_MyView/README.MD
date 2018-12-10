### 高级查询
* 初始化数据库
    * 需要执行的命令
        * python manage.py makemigrations
        * python manage.py migrate

* 如果要执行main方法，一定要设置上下文环境

import os

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'Seq_07_MyView.settings'

django.setup()
* 设置上下文环境结束

### 测试
如果是使用tests.py这个文件测试
需要执行如下代码：
python manage.py test
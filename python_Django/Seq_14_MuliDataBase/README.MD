### 混合使用数据库
* 创建应用的命令
    python manage.py startapp hello
    python manage.py startapp app01
    python manage.py startapp app02
* 配置seetings.py文件
    'hello',
    'app01',
    'app02',
* 配置三个数据库
* 设置app对应的数据库路由表
* 设置数据库的路由规则方法


* 初始化数据库
    * 需要执行的命令
        * python manage.py makemigrations
        * python manage.py migrate --database=db01
        * python manage.py migrate --database=db02
        * python manage.py migrate

* 配置admin.py文件
* 创建超级用户
    python manage.py createsuperuser
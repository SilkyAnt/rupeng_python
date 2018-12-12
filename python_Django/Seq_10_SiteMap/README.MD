### SiteMap 网站地图的使用
* 需要的包
    * 安装命令：pip install mysqlclient
* 配置settings中的参数
    * 给INSTALLED_APPS后面追加属性值
    'django.contrib.sites',
    'django.contrib.sitemaps',
* 定义的类一定要有 get_absolute_url 方法   
* 初始化数据库
    * 需要执行的命令
        * python manage.py makemigrations
        * python manage.py migrate

* 生成的网站地图中的域名的数据
    * 数据源于表 django_site
    update django_site set name = 'celine-zhi.com',domain='celine-zhi.com'
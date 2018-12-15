### 混合使用数据库
* 配置seetings.py文件

* 为了避免错误：Can't find msguniq. Make sure you have GNU gettext tools 0.15 or newer installed.
    * 先安装软件：https://mlocati.github.io/articles/gettext-iconv-windows.html
    * 选择 64bit static的版本就OK

* 初始化数据库
    * 需要执行的命令
        * python manage.py makemigrations
        * python manage.py migrate
        * django-admin makemessages -l zh_CN
        * 生成了文件django.po，然后通过记事本软件打开再自行翻译
        * django-admin compilemessages
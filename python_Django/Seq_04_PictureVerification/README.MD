### 需要用到的包
* 安装命令
    pip install django-simple-captcha
* 在setting.py中配置一下
    'captcha',
* 初始化数据库
    * 需要执行的命令
        * python manage.py makemigrations
        * python manage.py migrate
* 配置urls不可遗漏
    url(r"^captcha", include("captcha.urls")),     
    如果没有这个配置，图片验证码将不显示
    
以上是 图片验证码需要注意的事项

### 文件上传下载
* 无需额外的包
* 下载时候：中文文件名的问题
* 下载时候：大文件的问题

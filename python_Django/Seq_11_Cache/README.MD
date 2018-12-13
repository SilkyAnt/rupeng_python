### 缓存的使用
* 初始化数据库
    * 需要执行的命令
        * python manage.py makemigrations
        * python manage.py migrate

* 用cmd的命令建缓存表
    命令：python manage.py createcachetable cachetable
    这个cachetable是表名
   
* 注解一定要加
    @cache_page
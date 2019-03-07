### 个人博客系统
* 使用Seq_17_Blogvenv中的python运行环境
* 全文检索需要的模块
    * pip install django-haystack
    * pip install whoosh
    * pip install jieba
    
* 配置数据库
    * 建库脚本
    create database blogDemo;
 
* 初始化数据库
    * 需要执行的命令
        * python manage.py makemigrations
        * python manage.py migrate

* 初始化超级用户
    * python manage.py createsuperuser
    
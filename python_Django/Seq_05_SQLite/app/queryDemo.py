# 如果要执行main方法，一定要设置上下文环境
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'Seq_05_SQLite.settings'
django.setup()
# 设置上下文环境结束

from app.models import Stu

# 查询所有对象
print(Stu.objects.all())
# 遍历对象集合
for t in Stu.objects.all():
    print(t.id, t.name)

# 带条件的查询
print("#########################")
print(Stu.objects.all().get(id=2))
print(Stu.objects.all().get(name="czf"))

# 过滤查询
print("#########################")
print(Stu.objects.all().filter(name='czf'))
print(Stu.objects.all().filter(name__exact='czf'))  # 严格区分大小写
print(Stu.objects.all().filter(name__iexact='czf'))  # 不区分大小写
print(Stu.objects.all().filter(name__contains='f'))  # 包含字母f
print(Stu.objects.all().filter(name__regex='^cz'))  # 正则表达式
print(Stu.objects.all().filter(id=4))
print(Stu.objects.all().filter(id__gt=2))
print(Stu.objects.all().filter(id__lte=2))
print(Stu.objects.all().filter(id__lt=2))
print(Stu.objects.all().filter(id__in=(1, 3)))
print(Stu.objects.all().filter(id__range=(1, 3)))

print("#########################")

# 排除
print(Stu.objects.all().exclude(name__endswith='f'))  # 正则表达式
print("#########################")

# 其他查询操作
print(Stu.objects.all()[1:4:2])
print(Stu.objects.all()[:2])

# 排序
print("#########################")
print(Stu.objects.all().order_by("-id"))  # 倒序
print(Stu.objects.all().exists())
print(Stu.objects.count())  # 建议使用这个方法
print(len(Stu.objects.all()))

# 非查询操作
Stu.objects.all().get(name="abc123").delete()  # 删除一个对象
Stu.objects.all().filter(name="abc").delete()  # 删除一个或者多个对象

# 方法一
s1 = Stu.objects.get(id="4")
s1.name = "jianglp"
s1.save()
# 方法二 如果是 get 则没有 update这个方法
Stu.objects.all().filter(id="4").update(name="we1234")
# 方法三
obj, created = Stu.objects.update_or_create(
    defaults={"name": "abc456"}, name="abc123")
print(obj, created)

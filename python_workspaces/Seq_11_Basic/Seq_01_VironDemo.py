import os

# 获取环境变量的对象
envir = os.environ
# print(envir)
# 通过调用get(key)方法获取value
print(envir.get("JAVA_HOME"))
# 遍历所有的环境变量
for key in envir:
    print("key={0},value={1}".format(key, envir.get(key)))

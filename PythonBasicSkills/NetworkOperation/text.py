f = open("pycharm-professional-2018.2.1.exe",mode="rb+")
fcontent = f.read(1024*1024)
n = 1
while fcontent:
    fcontent = f.read(1024*1024)
    n = n + 1
print(n)
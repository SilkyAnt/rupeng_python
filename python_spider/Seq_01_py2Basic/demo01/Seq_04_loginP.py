# encoding=utf-8
# 采用post方法使用网络爬虫实现登录功能
# 两大步
# 第一步：从http://localhost:8080爬取name='csrfmiddlewaretoken' value=''
# 第二步：把用户名、密码和csrf令牌采用post传递给http://localhost:8080/login

# encoding=utf-8
# 通过登录去爬虫
# 首先要有用户名和密码
# encoding=utf-8
# 通过登录去爬虫
# 首先要有用户名和密码
import urllib
import urllib2
import cookielib
# lxml库 html.etree解析html
from lxml import html

# 设置请求头信息
head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}


# 给opener加上cookie
def makeMyOpener(head):
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookielib.CookieJar()
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib2.build_opener(handler)
    header = []
    # 遍历请求头信息
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    # 设置opener的请求头信息
    opener.addheaders = header
    return opener


# 爬登录的页面，里面包含
# <input type='hidden' name='csrfmiddlewaretoken'
# value='Vx2uPbh68onVF4IA5RKzuv2SjTImW9Z0Gp2yjbnNdeulq9ex71AV6AEpQ8Ho1Qlk' />
oper = makeMyOpener(head)
uop = oper.open('http://127.0.0.1:8000', timeout=10000)
data = uop.read()
print("data", data)
# lxml提取 csrfmiddlewaretoken
selector = html.etree.HTML(data)
# XPATH返回的不一定就是唯一的节点，而是符合条件的所有节点
# //book    选取所有 book 子元素，而不管它们在文档中的位置。
# //@lang   选取名为 lang 的所有属性。
links = selector.xpath('//form/input[@name="csrfmiddlewaretoken"]/@value')
for link in links:
    csrfmiddlewaretoken = link
print("csrfmiddlewaretoken", csrfmiddlewaretoken)
url = 'http://127.0.0.1:8000/login'
datas = {'csrfmiddlewaretoken': csrfmiddlewaretoken, 'username': 'admin', 'userpwd': '123456'}
data_encoded = urllib.urlencode(datas)
response = oper.open(url, data_encoded)
content = response.read()
# html = content.decode()
print(content)

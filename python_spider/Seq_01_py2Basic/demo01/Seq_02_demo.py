# encoding=utf-8
# 运行结果和demo01完全一样的，只不过中间多了一个request对象，推荐大家这么写，
# 因为在构建请求时还需要加入好多内容，通过构建一个request，
# 服务器响应请求得到应答，这样显得逻辑上清晰明确。
import urllib2

request = urllib2.Request("http://www.rupeng.com")
response = urllib2.urlopen(request)
print(response.read())

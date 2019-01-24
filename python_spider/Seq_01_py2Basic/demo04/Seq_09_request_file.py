# coding=utf-8
'''
流式传输定义很广泛，现在主要指通过网络传送流媒体（如视频、音频）的技术总称。
其特定含义为通过Internet 将影视节目传送到PC机。
实现流式传输有两种方法：
    实时流式传输（Realtime streaming）和顺序流式传输（progressive streaming）。
requests 是支持流式上传的，这允许你发送大的数据流或文件而无需先把它们读入内存。
要使用流式上传，仅需为你的请求体提供一个类文件对象即可
'''
import requests

url = 'http://httpbin.org/post'
# 只是个例子,音乐文件我就没有上传到GitHub了
with open('Beyond.mp3', mode="rb") as f:
    r = requests.post(url, data=f)
print(r.text)

# coding=utf-8
import requests

proxies = {
    "http": "http://60.216.177.152:8118",
}
response = requests.get("https://www.taobao.com", proxies=proxies)
print(response.text)
print(response.status_code)

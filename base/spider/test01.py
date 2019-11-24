import urllib.request

response = urllib.request.urlopen('http://www.qiubaichengnian.com/index.html')
# result = response.read().decode('utf-8')
result = response.read().decode('gbk')
print(result)

# 简单的爬虫测试
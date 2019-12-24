import urllib.request
import urllib.error



def getHeader(url,origin):
  return {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Host': 'www.chinabidding.cc',
    'Origin': origin,
    'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
  }




def get_list(url,origin):
  try:
    header = getHeader(url,origin)
    req = urllib.request.Request(url, headers=header )
    print(req)
    html = urllib.request.urlopen(req)
    print(html)
    # content = html.read()

  except urllib.error.URLError as e:
      if hasattr(e, 'reason'):
          print('错误原因是' + str(e))
  except urllib.error.HTTPError as e:
      if hasattr(e, 'code'):
          print('错误状态码是' + str(e.code))
  else:
      print('请求成功通过。')
      

origin = 'https://tai.changingedu.com'
businessKey = 'qingqing'


url = '%s/api/data/leads-track-result/stats-list?key=%s&page=1&size=10' % (origin,businessKey)
print(url)
get_list(url,origin)

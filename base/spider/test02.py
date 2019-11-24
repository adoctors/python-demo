import urllib.request
import urllib.error

try:
  header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Cookie': '__jsluid_h=43a8c9faf4062503f3295006bb521b09; client_login_info=a954Hx4YlHjUhyzlfx.e51vrNsJlRo61upp9wt1xWdl.OBBOMOgeJerCi1JknOwoSVyHyndVc1Di2QPPPw5UKH5u52nJ; Hm_lvt_93352b09c212b481a8db685016fa5723=1574430627,1574433222; Hm_lpvt_93352b09c212b481a8db685016fa5723=1574436157; clientlogin=0a3es.3S4EMZnT9mB66sARTO3DWVt3PLgV91ZoC2ZTwnHOjdxTeZD3ZcuyXPRDu02dwat7nQm1gDwEUvHpcxDZAluD9a.TcY0GWqYe3bzJ9ub3HfWag_Rg; __jsl_clearance=1574437465.292|0|OlkH0cXQAenKDojqIuIOC1qDwgU%3D',
    'Host': 'www.chinabidding.cc',
    'Origin': 'http://www.chinabidding.cc',
    'Referer': 'http://www.chinabidding.cc/search/index.html?keyword=%E4%B8%89%E7%9B%9F&h_lx=11&date=365&search_field=0&vague=0&h_province=0&submit=+',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
  }

  url = 'http://www.chinabidding.cc/search/index.html?keyword=%E4%B8%89%E7%9B%9F&h_lx=11&date=365&search_field=0&vague=0&h_province=0&submit=+'
  response = urllib.request.Request(url, headers=header )
  html = urllib.request.urlopen(response)
  result = html.read()

except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print('错误原因是' + str(e))
except urllib.error.HTTPError as e:
    if hasattr(e, 'code'):
        print('错误状态码是' + str(e.code))
else:
    print('请求成功通过。')
    print(result)

# headers伪装用户行为，headers里的 Cookie记得更新 




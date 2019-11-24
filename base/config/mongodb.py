from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017')

db = client.spiders
coll_bid = db.bid
coll_qiubai = db.qiubai

coll_sm = db.sm
coll_dtw = db.dtw
coll_jz = db.jz
coll_ly = db.ly


# company = [
#   {
#     name:'三盟',
#     short_name:'sm'
#   },
#   {
#     name:'南京迪塔维数据技术有限公司',
#     short_name:'dtw'
#   },
#   {
#     name:'江苏金智教育信息股份有限公司',
#     short_name:'jz'
#   },
#   {
#     name:'联奕科技有限公司',
#     short_name:'ly'
#   },
# ]


def getHeader(url,cookie):
  return {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Cookie': cookie,
    'Host': 'www.chinabidding.cc',
    'Origin': 'http://www.chinabidding.cc',
    'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
  }


def get_detail_header(url,cookie,list_url):
  return {
    'Accept': 'ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': cookie,
    'Host': 'www.chinabidding.cc',
    'Origin': 'http://www.chinabidding.cc',
    'Referer': list_url,
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
  }


bid_data = {
  'company_name':'xx',
  'area': 'xx',
  'customer_name': '招标人',
  'project_name':'xx',
  'bid_time': 'xx',
  'hit_time': '',
  'hit_money': '中标金额',
  'hit_content':'',
  'list_url':'xx',
  'detail_url':'xx',
  'other':'',
}  




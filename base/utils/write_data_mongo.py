from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017')

db = client.spiders
coll_req_list = db.req_list

for i in range(50,501):
  url = "/other/req_list/%d" % i
  data = {
    'req_url': url
  }
  coll_req_list.insert_one(data)

# /other/req_list/:id
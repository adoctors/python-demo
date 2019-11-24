from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017')
db = client.spiders
coll_bid = db.bid

# 插入数据
# coll_bid.insert_one({'company_name':'公司','area':'洛阳','customer_name':'customer_name'})

# 批量插入
# coll_bid.insert_many([{'company_name':'公司1','area':'洛阳1','customer_name':'customer_name'},{'company_name':'公司2','area':'洛阳2','customer_name':'customer_name'}])

# 删除数据
# coll_bid.delete_one({'company_name':'公司','area':'洛阳'})

## 删除多个
# coll_bid.delete_many({'company_name':'公司','area':'洛阳'})

# 查数据
# for op in coll_bid.find():
  # print(op)

# 更新数据

# op = {'area':'洛阳1'}
# bids = coll_bid.find_one(op)
# bids['url'] = 'www.baidu.com'
# coll_bid.update_one(op,{'$set':bids})

# 封装更新方法

# def update_coll(query,coll_name,key,val):
#   coll = coll_name.find_one(query)
#   coll[key] = val
#   coll_name.update_one(query,{'$set':coll})

# update_coll({'area':'洛阳2'},coll_bid,'url2','www.baidu.com')


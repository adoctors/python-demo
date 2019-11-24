import re

str1 = '招标人名称：汕头市中心医院'
str2 = '招标人联系人：林吉跃'

def verify(strs):
  target1 = '2，招标人名称(：|:)'
  target2 = '招标联系人'
  target3 = '成交金额(：|:)'
  target4 = '（3）成交金额：柒拾叁万伍仟捌佰元整（￥735,800.00）'

  # if target1 in strs:
  #   print(re.sub(target1,'',strs,1))
  # elif target2 in strs:
  #   print(strs.replace(target2,''))
  # else:
  #   print('无')


  if re.match(target1,strs):
    print(re.sub(target1,'',strs,1))
  elif re.match(target2,strs):
    print(re.sub(target2,'',strs,1))
  else:
    print('无')

# verify(str1)

str3 = '（3）成交金额：柒拾叁万伍仟捌佰元整（￥735,800.00）'
str4 = '成交金额：2000'
str5 = '2、成交金额：3000'

def verify2(strs):
  conditions = [
    '(成交|合同|中标|总中标)金额(：|:)',
    '(（\d）|\d、)成交金额(：|:)',
    '(（\d）|\d、)成交 金额(：|:)',
    '成交 金额(：|:)',
    '中标(金额（人民币）|\(成交\)金额)(：|:)',
    '合同总金',
  ]

  for item in conditions:
    if re.match(item,strs):
      # print(re.sub(item,'',strs,1))
      return re.sub(item,'',strs,1).strip()

# verify2(str3)   
print(verify2('中标(成交)金额：人民币 贰佰叁拾陆万元（￥2360000.00元）'))  
print(verify2('中标金额（人民币）：陆拾捌万陆仟元整（￥686000.00元）'))  

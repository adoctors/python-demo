import xlwt
from datetime import datetime
import sys
sys.path.append('../config')


from mongodb import coll_sm
from mongodb import coll_dtw
from mongodb import coll_jz
from mongodb import coll_ly

# 实例化一个Workbook()对象(即excel文件)
wbk = xlwt.Workbook()
# 获取查询的总条数，之前的count废弃
# print(coll_dtw.estimated_document_count())

def write_data_to_excel(coll_name,sheet_name):
  result = []
  for x in coll_name.find():
    result.append(x)

  # 新建一个名为Sheet1的excel sheet。此处的cell_overwrite_ok =True是为了能对同一个单元格重复操作。
  sheet = wbk.add_sheet(sheet_name,cell_overwrite_ok=True)

  # 可优化在第一行加表头

  for i in range(0,len(result)):
    # print(i)
    #对result的每个子元素作遍历，
    for j in range(0,8):
       # 将每一行的每个元素按行号i,列号j,写入到excel中。
      if(j == 0):
        sheet.write(i,j,result[i]['company_name'])
      if(j == 1):
        sheet.write(i,j,result[i]['area'])
      if(j == 2):
        sheet.write(i,j,result[i]['project_name'])
      if(j == 3):
        sheet.write(i,j,result[i]['hit_time'])
      if(j == 4):
        sheet.write(i,j,result[i]['list_url'])
      if(j == 5):
        sheet.write(i,j,result[i]['detail_url'])
      if(j == 6):
        try:
          sheet.write(i,j,result[i]['hit_money'])
        except:
          print('无')
      if(j == 7):
        try:
          sheet.write(i,j,result[i]['hit_money_res'])
        except:
          print('无')    


write_data_to_excel(coll_dtw,'南京迪塔维数据技术有限公司')
write_data_to_excel(coll_sm,'三盟')
write_data_to_excel(coll_jz,'江苏金智教育信息股份有限公司')
write_data_to_excel(coll_ly,'联奕科技有限公司')

# 获取当前日期，得到一个datetime对象如：(2016, 8, 9, 23, 12, 23, 424000)
today = datetime.today()
# 将获取到的datetime对象仅取日期如：2016-8-9
today_date = datetime.date(today) 
# 以传递的name+当前日期作为excel名称保存。
wbk.save('表'+str(today_date)+'.xls')




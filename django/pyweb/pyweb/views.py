from django.http import HttpResponse
from django.http import JsonResponse

def ErrorResponse(code, message):
  data = {}
  data['status'] = 'ERROR'
  data['code'] = code
  data['message'] = message
  return JsonResponse(data)

def SuccessResponse(res):
  data = {}
  data['status'] = 'SUCCESS'
  data['code'] = 0
  data['data'] = res
  return JsonResponse(data)

def index(request):
  return HttpResponse('Hello world!')


def userInfo(request):
  res = {
    'name': 'adoctors',
    'age': 18
  }
  return SuccessResponse(res)

def test(request, year, month):
  print('获取url中params数据：', year, month)
  day = request.GET.get('day', 1) # 获取url的页面参数（GET请求）
  print('获取url的页面参数（GET请求）：', day)
  return HttpResponse('test!')


def postTest(request):
  print(request.method)
  if(request.method == 'POST'):
    print("the POST method")
    concat = request.POST
    postBody = request.body
    print(concat)
    print(type(postBody))
    print(postBody)
  return HttpResponse('postTest!')
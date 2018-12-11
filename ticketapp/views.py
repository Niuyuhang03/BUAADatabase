from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from . import models

# Create your views here.

def index(request):
    print(request.session.get('foo'))
    return render(request, "ticketapp/index.html")

def sign(request):
    return render(request, "ticketapp/sign.html")

def ajax_register(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        print(data['username'])
        # 从数据库中认证用户名是否为注册
        is_register = 1
        return HttpResponse(is_register)

def ajax_login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data['username'])
        # 查询数据库中用户表，用户名或者密码是否正确
        # is_login= 2 #0 for no user, 1 for wrong passwd, 2 for ok
        response = JsonResponse({'foo':'bar'})
        is_sign = 1
        request.session['foo'] = 'bar'
        return response
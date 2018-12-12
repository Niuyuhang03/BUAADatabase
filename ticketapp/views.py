from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from . import models

# Create your views here.

def index(request, id):
    if request.session.get('userid'):
        return render(request, "ticketapp/index.html")
    else:
        return HttpResponseRedirect("../../sign/")

def home(request):
    print (request.session.get('userid'))
    if request.session.get('userid'):
        return render(request, "ticketapp/home.html")
    else:
        return HttpResponseRedirect("../sign/")

def personpage(request):
    print(request.session.get('userid'))
    if request.session.get('userid'):
        return render(request, "ticketapp/personpage.html")
    else:
        return HttpResponseRedirect("../sign/")

def release(request):
    print(request.session.get('userid'))
    if request.session.get('userid'):
        return render(request, "ticketapp/release.html")
    else:
        return HttpResponseRedirect("../sign/")

def purchase(request):
    print(request.session.get('userid'))
    if request.session.get('userid'):
        return render(request, "ticketapp/purchase.html")
    else:
        return HttpResponseRedirect("../sign/")

def sign(request):
    return render(request, "ticketapp/sign.html")



def ajax_register(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        # 从数据库中认证用户名是否为注册
        try:
            models.user.objects.get(username=data['username'])
            is_register = 1
            return HttpResponse(is_register)
        except:
            models.user.objects.create(username=data['username'], userpwd=data['passwd'], usersex=data['usersex'])
            is_register = 0
            return HttpResponse(is_register)

def ajax_login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        # 查询数据库中用户表，用户名或者密码是否正确
        # is_login= 0 for no user, 1 for wrong passwd, 2 for ok
        try:
            cur_user = models.user.objects.get(username=data['username'])
            if cur_user.userpwd == data['passwd']:
                is_sign = 2
                request.session['userid'] = cur_user.userid
            else:
                is_sign = 1
        except:
            is_sign = 0
        return HttpResponse(is_sign)

def ajax_log_out(request):
    if request.method == 'POST':
        request.session.flush()
        return HttpResponse(1)

def ajax_showinfo(request):
    if request.method == 'GET':
        cur_user = models.user.objects.get(userid=request.session['userid'])
        return_data = {'userid':cur_user.username, "username":cur_user.username, "sex":cur_user.usersex}
        return JsonResponse(return_data)

def ajax_search(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data['info'])

        #TODO:根据info去商品数据库寻找信息

        return_data = {
            "info": [
                {"id": "1", "name": "话剧", "time": "2018.12.12", "address": "晨兴", "money": "100"},
                {"id": "2", "name": "足球", "time": "2018.12.13", "address": "足球场", "money": "200"},
                {"id": "3", "name": "篮球", "time": "2018.12.14", "address": "篮球场", "money": "300"}
            ]
        }

        return JsonResponse(return_data)

def ajax_goodinfo(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data['good_id'])
        good_id = data['good_id']
        #TODO:根据goodid查询信息

        return_data = {
            "name": "话剧票", "date": "2018.12.12", "address": "北航", "dec": "就是一张票子", "price": "200"
        }
        return JsonResponse(return_data)

def ajax_purchase(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        user_id = data['user_id']
        good_id = data['good_id']

        #TODO

        succ = 1
        return HttpResponse(succ)

def ajax_modi_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        # succ = 1:修改成功 0:用户名已存在，修改失败 2:新用户名和当前用户名相同，修改失败
        try:
            cur_user = models.user.objects.get(username=data['name'])
            if request.session.get('userid') == cur_user.userid:
                succ = 2
            else:
                succ = 0
        except:
            succ = 1
            models.user.objects.filter(pk=request.session.get('userid')).update(usersex=data['sex'], username=data['name'])
        return HttpResponse(succ)

def ajax_modi_passwd(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        #succ = 0:密码错误 1:修改成功
        cur_user = models.user.objects.get(pk=request.session.get('userid'))
        if cur_user.userpwd != data['old_passwd']:
            succ = 0
        else:
            succ = 1
            models.user.objects.filter(pk=request.session.get('userid')).update(userpwd=data['new_passwd'])
        return HttpResponse(succ)

def ajax_query_purchase(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        #TODO:

        return_data = {
            "info": [
                {"id": "1", "name": "话剧", "time": "2018.12.12", "address": "晨兴", "money": "100"},
                {"id": "2", "name": "足球", "time": "2018.12.13", "address": "足球场", "money": "200"},
                {"id": "3", "name": "篮球", "time": "2018.12.14", "address": "篮球场", "money": "300"}
            ]
        }
        return JsonResponse(return_data)

def ajax_query_release(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        return_data = {"info": []}
        # TODO:
        my_tickets_id = models.user_ticket.objects.filter(userid=request.session.get('userid'))
        for my_ticket_id in my_tickets_id:
            my_ticket = models.ticket.objects.get(ticketid=my_ticket_id.ticketid)
            return_data['info'].append({"id":my_ticket.ticketid, "name":my_ticket.ticketname, "time":my_ticket.tickettime, "address":my_ticket.ticketlocation, "money":my_ticket.ticketprice})
        print(return_data)
        return JsonResponse(return_data)

def ajax_release(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        cur_ticket = models.ticket(ticketname=data['name'], ticketlocation=data['address'], tickettime=data['date'], ticketinfo=data['dec'], ticketprice=data['price'], ticketstatus=0)
        cur_ticket.save()
        print("info:")
        print(request.session.get('userid'))
        print(cur_ticket.ticketid)
        models.user_ticket.objects.create(userid=request.session.get('userid'), ticketid=cur_ticket.ticketid)
        succ = 1
        return HttpResponse(succ)
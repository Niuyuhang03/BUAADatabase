import datetime
import os

from django.db.models import Q
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
        return_data = {'userid':cur_user.username, "username":cur_user.username, "sex":cur_user.usersex, "userimg":cur_user.userimg}
        return JsonResponse(return_data)

def ajax_search(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        return_data = {"info": []}
        tickets = models.ticket.objects.filter(Q(ticketname__icontains=data['info'])|Q(ticketinfo__icontains=data['info'])|Q(ticketlocation__icontains=data['info']))
        for my_ticket in tickets:
            if my_ticket.ticketstatus == 0:
                return_data['info'].append({"id":my_ticket.ticketid, "name":my_ticket.ticketname, "time":my_ticket.tickettime, "address":my_ticket.ticketlocation, "money":my_ticket.ticketprice})
        return JsonResponse(return_data)

def ajax_goodinfo(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        cur_ticket = models.ticket.objects.get(ticketid=data['good_id'])
        print("status")
        print(cur_ticket.ticketstatus)
        return_data = {
            "name": cur_ticket.ticketname, "date": cur_ticket.tickettime, "address": cur_ticket.ticketlocation, "dec": cur_ticket.ticketinfo, "price": cur_ticket.ticketprice, "status": cur_ticket.ticketstatus, "img": cur_ticket.ticketimg
        }
        return JsonResponse(return_data)

def ajax_purchase(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        cur_ticket = models.ticket.objects.get(ticketid=data['good_id'])
        if cur_ticket.ticketstatus == 0:
            if models.user_ticket.objects.get(ticketid=cur_ticket.ticketid).userid == request.session.get('userid'):
                succ = 0
            else:
                models.ticket.objects.filter(ticketid=data['good_id']).update(ticketstatus=1)
                print(datetime.datetime.now())
                cur_order = models.orderlist(ordertime=datetime.datetime.now())
                cur_order.save()
                models.user_order.objects.create(userid=request.session.get('userid'), orderid=cur_order.orderid)
                models.ticket_order.objects.create(ticketid=data['good_id'], orderid=cur_order.orderid)
                succ = 1
        else:
            succ = 2
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
        return_data = {"info": []}
        my_orders_id = models.user_order.objects.filter(userid=request.session.get('userid'))
        for my_order_id in my_orders_id:
            my_order = models.orderlist.objects.get(orderid=my_order_id.orderid)
            my_ticket = models.ticket.objects.get(ticketid=(models.ticket_order.objects.get(orderid=my_order.orderid).ticketid))
            return_data['info'].append(
                {"id": my_ticket.ticketid, "name": my_ticket.ticketname, "time": my_ticket.tickettime,
                 "address": my_ticket.ticketlocation, "money": my_ticket.ticketprice})
        return JsonResponse(return_data)

def ajax_query_release(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        return_data = {"info": []}
        my_tickets_id = models.user_ticket.objects.filter(userid=request.session.get('userid'))
        for my_ticket_id in my_tickets_id:
            my_ticket = models.ticket.objects.get(ticketid=my_ticket_id.ticketid)
            return_data['info'].append({"id":my_ticket.ticketid, "name":my_ticket.ticketname, "time":my_ticket.tickettime, "address":my_ticket.ticketlocation, "money":my_ticket.ticketprice})
        return JsonResponse(return_data)

def ajax_release(request):
    if request.method == 'POST':
        cur_ticket = models.ticket(ticketname=request.POST.get('name'), ticketlocation=request.POST.get('addr'), tickettime=request.POST.get('date'), ticketinfo=request.POST.get('dec'), ticketprice=request.POST.get('price'), ticketstatus=0)
        cur_ticket.save()

        file_obj = request.FILES.get('file')
        if file_obj:  # 处理附件上传到方法
            request_set = {}
            print('file--obj', file_obj)
            # user_home_dir = "upload/%s" % (request.user.userprofile.id)
            accessory_dir = 'F:/BUAA/数据库/课设/任务2/ticketsystem/ticketapp/static/images/ticketImages'
            # if not os.path.isdir(accessory_dir):
            #     os.mkdir(accessory_dir)
            upload_file = "%s/%s" % (accessory_dir, str(cur_ticket.ticketid) + ".JPG")
            recv_size = 0
            f = open(upload_file, 'wb')
            for chunk in file_obj.chunks():
                f.write(chunk)
            f.close()
        models.ticket.objects.filter(ticketid=cur_ticket.ticketid).update(ticketimg=str(cur_ticket.ticketid) + ".JPG")
        models.user_ticket.objects.create(userid=request.session.get('userid'), ticketid=cur_ticket.ticketid)
        succ = 1
        return HttpResponse(succ)


def ajax_uploadimg(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        if file_obj:  # 处理附件上传到方法
            request_set = {}
            print('file--obj', file_obj)
            # user_home_dir = "upload/%s" % (request.user.userprofile.id)
            accessory_dir = 'F:/BUAA/数据库/课设/任务2/ticketsystem/ticketapp/static/images/userImages'
            # if not os.path.isdir(accessory_dir):
            #     os.mkdir(accessory_dir)
            upload_file = "%s/%s" % (accessory_dir, str(request.session.get('userid'))+".JPG")
            recv_size = 0
            f = open(upload_file, 'wb')
            for chunk in file_obj.chunks():
                f.write(chunk)
            f.close()
            models.user.objects.filter(userid=request.session.get('userid')).update(userimg=str(request.session.get('userid'))+".JPG")
            return HttpResponse(1)
from django.urls import path
from . import views

app_name = 'ticketapp'

urlpatterns =[
    path('index/id=<int:id>/', views.index, name='index'),
    path('sign/', views.sign, name='sign'),
    path('home/', views.home, name='home'),
    path('personpage/', views.personpage, name='personpage'),
    path('release/', views.release, name='release'),
    path('purchase/', views.purchase, name='purchase'),
    path('ajax_register/', views.ajax_register, name='ajax_register'),
    path('ajax_login/', views.ajax_login, name='ajax_login'),
    path('ajax_log_out/', views.ajax_log_out, name='ajax_log_out'),
    path('ajax_showinfo/', views.ajax_showinfo, name='ajax_showinfo'),
    path('ajax_search/', views.ajax_search, name='ajax_search'),
    path('ajax_goodinfo/', views.ajax_goodinfo, name='ajax_goodinfo'),
    path('ajax_purchase/', views.ajax_purchase, name='ajax_purchase'),
    path('ajax_modi_info/', views.ajax_modi_info, name='ajax_modi_info'),
    path('ajax_modi_passwd/', views.ajax_modi_passwd, name='ajax_modi_passwd'),
    path('ajax_query_purchase/', views.ajax_query_purchase, name='ajax_query_purchase'),
    path('ajax_query_release/', views.ajax_query_release, name='ajax_query_release'),
    path('ajax_release/', views.ajax_release, name='ajax_release'),
    path('ajax_uploadimg/', views.ajax_uploadimg, name='ajax_uploadimg'),
]
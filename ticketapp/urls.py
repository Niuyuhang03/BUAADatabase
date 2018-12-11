from django.urls import path
from . import views

app_name = 'ticketapp'

urlpatterns =[
    path('index/', views.index, name='index'),
    path('sign/', views.sign, name='sign'),
    path('ajax_register/', views.ajax_register, name='ajax_register'),
    path('ajax_login/', views.ajax_login, name='ajax_login'),
]
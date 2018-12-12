from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.address)
admin.site.register(models.orderlist)
admin.site.register(models.picture)
admin.site.register(models.telephone)
admin.site.register(models.ticket)
admin.site.register(models.user)
admin.site.register(models.user_ticket)
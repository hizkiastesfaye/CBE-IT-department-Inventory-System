from django.contrib import admin
from .models import User,Request, staffDescription
# Register your models here.
admin.site.register(User)
admin.site.register(Request)
admin.site.register(staffDescription)
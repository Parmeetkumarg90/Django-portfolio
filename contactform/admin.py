from django.contrib import admin
from django.contrib.admin.sites import site
from .models import contact_data
# Register your models here.
class contact_admin(admin.ModelAdmin):
    list_display = ('user_name','user_email','user_phone','user_message')
admin.site.register(contact_data,contact_admin)
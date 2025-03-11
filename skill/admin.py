from django.contrib import admin
from django.contrib.admin.sites import site
from .models import newskill

# Register your models here.

class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_img','skill_name')

admin.site.register(newskill,SkillAdmin)
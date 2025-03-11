from django.db import models

# Create your models here.
class newskill(models.Model):
    skill_img = models.FileField(upload_to='',max_length=50,null=True,default=None) # make a file upload field in admin panel
    skill_name = models.CharField(max_length=10)
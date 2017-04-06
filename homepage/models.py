from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField('title', max_length=256)
    content = models.TextField('content')
 
    pub_date = models.DateTimeField('publish-time', auto_now_add=True, editable = True)
    update_time = models.DateTimeField('update-time',auto_now=True, null=True)

    def __unicode__(self):
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
 
    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name of the person"
    full_name = property(my_property)
    
class TeacherInfo(models.Model):
    tec_title = models.CharField(max_length=100)
    tec_age = models.IntegerField(default=0)
    tec_area = models.CharField(max_length=50)
    tec_info = models.CharField(max_length=200)
    tec_limit_price = models.FloatField(default=0)
    tec_max_price = models.FloatField(default=0)
    tec_evaluation_num = models.IntegerField(default=0)
    tec_other_info = models.CharField(max_length=100)

    def __unicode__(self):
        return self.tec_title
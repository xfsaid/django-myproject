# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from django.db import models

# Create your models here.
# class Article(models.Model):
#     title = models.CharField('title', max_length=256)
#     content = models.TextField('content')
 
#     pub_date = models.DateTimeField('publish-time', auto_now_add=True, editable = True)
#     update_time = models.DateTimeField('update-time',auto_now=True, null=True)

#     def __unicode__(self):
#         return self.title
    
GENDER_CHOICES = (
    ('S', 'Sec'),
    ('M', 'Male'),
    ('F', 'Female'),
)
    
class Subject(models.Model):
    #grade_level = models.ForeignKey(Grade, verbose_name='所属年级')
    subject_name = models.CharField("科目名称",max_length = 100)
    slug = models.CharField("科目地址",max_length = 100)
    intro = models.CharField("科目介绍",max_length = 100)
    
    #def my_property(self):
    #    return '[' + self.grade_level.level + '] ' + self.subject_name
    #my_property.short_description = "[Grade] Subject"
    #display = property(my_property)

    def __unicode__(self):
        return self.subject_name#在路径地址中有显示

class GradeSubject(models.Model):
    level = models.CharField("年级等级",max_length = 100)
    slug = models.CharField("等级地址",max_length = 100)
    intro = models.CharField("等级介绍",max_length = 100)
    subject = models.ManyToManyField(Subject,verbose_name = "科目列表")

    def __unicode__(self):
        return self.level


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image_path = models.ImageField(upload_to='./static/upload/images/teachers',blank=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    area = models.CharField(max_length=50)
    info = models.CharField(max_length=200)
    limit_price = models.FloatField(default=0)
    max_price = models.FloatField(default=0)
    evaluation_num = models.IntegerField(default=0)
    skill = models.ManyToManyField(GradeSubject,verbose_name = "grade_subject")
    skill2 = models.ForeignKey(Subject,default='default',verbose_name = "subject")
    other_info = models.CharField(max_length=100)

    pub_date = models.DateTimeField('publish-time', auto_now_add=True, editable = True)
    update_time = models.DateTimeField('update-time',auto_now=True, null=True)

    def __unicode__(self):
        return self.first_name + '.' + self.last_name
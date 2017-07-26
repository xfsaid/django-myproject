# -*- coding: UTF-8 -*-

from django.contrib import admin
from .models import Article,Person,TeacherInfo,GradeSubjectMenu,Grade,Subject
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

class TeacherInfoAdmin(admin.ModelAdmin):
    list_display = ('tec_title',)

class GradeSubjectMenuAdmin(admin.ModelAdmin):
    list_display = ('display',)

class GradeAdmin(admin.ModelAdmin):
    list_display = ('level','slug','intro')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('display','subject_name','slug','intro') #可以显示ManyToManyField的数据



admin.site.register(Article,ArticleAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(TeacherInfo,TeacherInfoAdmin)
admin.site.register(GradeSubjectMenu,GradeSubjectMenuAdmin)
admin.site.register(Grade,GradeAdmin)
admin.site.register(Subject,SubjectAdmin)
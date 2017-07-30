# -*- coding: UTF-8 -*-

from django.contrib import admin
from .models import Article,Person,TeacherInfo,GradeSubjectMenu,GradeInfo,SubjectInfo

# Register your models here.
# fields = ('subject_name','intro')#排除一些不想被其他人编辑[不填]的fields
# search_fields = ('subject_name','slug','intro')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

class TeacherInfoAdmin(admin.ModelAdmin):
    list_display = ('tec_title',)

class GradeSubjectMenuAdmin(admin.ModelAdmin):
    list_display = ('display',)

class GradeInfoAdmin(admin.ModelAdmin):
    list_display = ('level','slug','intro')
    filter_horizontal = ('subject',)

class SubjectInfoAdmin(admin.ModelAdmin):
    list_display = ('subject_name','slug','intro')
    list_filter = ('subject_name',)
    



admin.site.register(Article,ArticleAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(TeacherInfo,TeacherInfoAdmin)
admin.site.register(GradeSubjectMenu,GradeSubjectMenuAdmin)
admin.site.register(GradeInfo,GradeInfoAdmin)
admin.site.register(SubjectInfo,SubjectInfoAdmin)
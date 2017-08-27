# -*- coding: UTF-8 -*-

from django.contrib import admin
from .models import Teacher,GradeSubject,Subject

# Register your models here.
# fields = ('subject_name','intro')#排除一些不想被其他人编辑[不填]的fields
# search_fields = ('subject_name','slug','intro')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')

class GradeSubjectAdmin(admin.ModelAdmin):
    list_display = ('level','slug','intro')
    filter_horizontal = ('subject',)

class SubjectInfoAdmin(admin.ModelAdmin):
    list_display = ('subject_name','slug','intro')
    list_filter = ('subject_name',)
    


admin.site.register(Teacher,TeacherAdmin)
admin.site.register(GradeSubject,GradeSubjectAdmin)
admin.site.register(Subject,SubjectInfoAdmin)
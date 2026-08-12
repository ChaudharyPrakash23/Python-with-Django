from django.contrib import admin
from Student.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','age','city')
    search_fields=('name','city')
    list_filter=('name','city')
    ordering=('age',)
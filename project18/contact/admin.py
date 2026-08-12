from django.contrib import admin
from contact.models import Contact

@admin.register (Contact)
class ContactForm(admin.ModelAdmin):
    list_display=('name','message')
    ordering=('name',)
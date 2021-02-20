from django.contrib import admin
from .models import Contact, Career
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin


admin.site.unregister(Group)

# Register your models here.


@admin.register(Contact)
class ContactDisplay(ImportExportModelAdmin,admin.ModelAdmin):
   list_display = ['name', 'email']
   search_fields = ['name', 'email']
   list_filter = ['name','email']
   pass

@admin.register(Career)
class CareerDisplay(ImportExportModelAdmin,admin.ModelAdmin):
   list_display = ['firstName', 'email', 'selected','date_applied']
   search_fields = ['firstName', 'email']
   list_filter = ['firstName','email','experience']
   pass
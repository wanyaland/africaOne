from django.contrib import admin
from core.models import Category,Features,Business
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(Category)
admin.site.register(Features)
admin.site.register(Business)
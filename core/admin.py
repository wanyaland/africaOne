from django.contrib import admin
<<<<<<< HEAD
from core.models import Category,Business,Features
=======
from core.models import Category,Features,Business
from import_export.admin import ImportExportModelAdmin
>>>>>>> parent of 3abcea8... Merged with master. Admin core.
# Register your models here.

admin.site.register(Category)
admin.site.register(Features)
admin.site.register(Business)

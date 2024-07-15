from django.contrib import admin
from .models import DataItem
from import_export.admin import ImportExportModelAdmin


admin.site.register(DataItem)
from django.contrib import admin
from .models import DataModel
# Register your models here.

@admin.register(DataModel)
class DataModelAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']
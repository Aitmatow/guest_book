from django.contrib import admin
from webapp.models import Records

# Register your models here.
class RecordsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'email', 'record', 'create_date', 'edited_date', 'status']
    list_filter = ['status']
    search_fields = ['name', 'status']
    fields = ['name', 'email', 'record', 'status']
    list_display_links = ['pk']

admin.site.register(Records, RecordsAdmin)
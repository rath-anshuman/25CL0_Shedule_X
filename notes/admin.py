from django.contrib import admin

# Register your models here.
from .models import Notes

admin.site.register(Notes)
# admin.py
from django.contrib import admin

# Customizing the Admin panel title and header
admin.site.site_header = "Schedule -X-"
admin.site.site_title = "Admin Schedule -X-"
admin.site.index_title = "Schedule -X- Admin Panel"

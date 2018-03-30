from django.contrib import admin

# Register your models here.

from .models import Vendor, Advertisement, Watch

admin.site.register(Vendor)
admin.site.register(Advertisement)
admin.site.register(Watch)
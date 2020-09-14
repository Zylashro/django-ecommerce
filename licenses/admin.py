from django.contrib import admin

from .models import License

class LicenseInline(admin.StackedInline):
    model = License

admin.site.register(License, LicenseInline)

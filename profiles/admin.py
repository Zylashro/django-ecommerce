from django.contrib import admin

from .models import UserProfile
from licenses.admin import LicenseInline

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [
        LicenseInline,
    ]

admin.site.register(UserProfile, UserProfileAdmin)

from django.contrib import admin

from .models import UserProfile
from licenses.models import License

class LicenseInline(admin.StackedInline):
    model = License
class UserProfileAdmin(admin.ModelAdmin):
    inlines = [LicenseInline,]

admin.site.register(UserProfile, UserProfileAdmin)

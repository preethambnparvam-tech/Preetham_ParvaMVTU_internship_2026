from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('phone_number', 'gender', 'usn', 'college', 'branch', 'semester', 'profile_picture', 'temporary_address', 'permanent_address', 'terms_agreed')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)


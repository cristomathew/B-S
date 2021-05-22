from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser
from django.utils.translation import gettext as _

from Core import models

class UserAdmin(BaseUser):
    ordering = ['id']
    list_display = ['id', 'username', 'email', 'first_name']
    list_display_links = ['id', 'username']
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'phone','favourites','rate_listing')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'password1', 'password2')
        }),
    )

admin.site.register(models.User, UserAdmin)
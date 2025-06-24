from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.forms import TextInput, Textarea
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('phone_number', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'gender')
    search_fields = ('phone_number', 'email', 'first_name', 'last_name')
    ordering = ('phone_number',)

    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'email', 'bio', 'avatar', 'gender')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)

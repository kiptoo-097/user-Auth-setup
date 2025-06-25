from django.contrib import admin
from .models import NavLink, DropdownLink

class DropdownInline(admin.TabularInline):
    model = DropdownLink
    extra = 1

class NavLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'is_dropdown', 'order']
    inlines = [DropdownInline]

admin.site.register(NavLink, NavLinkAdmin)

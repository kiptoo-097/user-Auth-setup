from django.contrib import admin
from django.utils.html import format_html
from .models import Category, SubCategory

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1
    ordering = ('-order',)
    fields = ('name', 'slug', 'order', 'is_active', 'template_name')
    prepopulated_fields = {'slug': ('name',)}
    verbose_name = "Subcategory"
    verbose_name_plural = "Subcategories"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'slug',
        'order', 
        'is_active',
        'show_in_navbar',
        'template_name',
        'get_subcategory_count'
    )
    list_editable = ('order', 'is_active', 'show_in_navbar', 'template_name')
    list_filter = ('is_active', 'show_in_navbar')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SubCategoryInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'order', 'is_active', 'show_in_navbar')
        }),
        ('Advanced Options', {
            'fields': ('template_name',),
            'classes': ('collapse',)
        }),
    )
    
    def get_subcategory_count(self, obj):
        count = obj.subcategories.count()
        url = f"/admin/navigation/subcategory/?category__id__exact={obj.id}"
        return format_html('<a href="{}">{}</a>', url, count)
    get_subcategory_count.short_description = 'Subcategories'

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'slug',
        'order',
        'is_active',
        'template_name'
    )
    list_editable = ('order', 'is_active', 'template_name')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'slug', 'category__name')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'category', 'order', 'is_active')
        }),
        ('Advanced Options', {
            'fields': ('template_name',),
            'classes': ('collapse',)
        }),
    )
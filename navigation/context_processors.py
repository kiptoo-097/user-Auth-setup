from .models import Category

def navbar_links(request):
    return {
        'navigation_categories': Category.objects.filter(
            is_active=True,
            show_in_navbar=True
        ).prefetch_related('subcategories').order_by('-order', 'name')
    }
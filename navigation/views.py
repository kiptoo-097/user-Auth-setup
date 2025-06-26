from django.shortcuts import render, get_object_or_404
from django.template import TemplateDoesNotExist
from django.http import Http404
from .models import Category, SubCategory

def category_view(request, slug):
    """
    View for displaying category pages with template override support
    """
    category = get_object_or_404(Category, slug=slug, is_active=True)
    
    # Determine which template to use
    template_name = category.template_name if category.template_name else 'navigation/category.html'
    
    try:
        return render(request, template_name, {
            'category': category,
            'subcategories': category.subcategories.filter(is_active=True).order_by('-order', 'name'),
        })
    except TemplateDoesNotExist:
        # Fallback to default template if custom template doesn't exist
        return render(request, 'navigation/category.html', {
            'category': category,
            'subcategories': category.subcategories.filter(is_active=True).order_by('-order', 'name'),
            'template_error': f"Custom template '{template_name}' not found. Using default."
        })

def subcategory_view(request, slug):
    """
    View for displaying subcategory pages with template override support
    """
    subcategory = get_object_or_404(SubCategory, slug=slug, is_active=True)
    
    # Determine which template to use
    template_name = subcategory.template_name if subcategory.template_name else 'navigation/subcategory.html'
    
    try:
        return render(request, template_name, {
            'subcategory': subcategory,
            'category': subcategory.category,
        })
    except TemplateDoesNotExist:
        # Fallback to default template if custom template doesn't exist
        return render(request, 'navigation/subcategory.html', {
            'subcategory': subcategory,
            'category': subcategory.category,
            'template_error': f"Custom template '{template_name}' not found. Using default."
        })
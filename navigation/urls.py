from django.urls import path
from . import views

app_name = 'navigation'

urlpatterns = [
    path('categories/<slug:slug>/', views.category_view, name='category'),
    path('subcategories/<slug:slug>/', views.subcategory_view, name='subcategory'),
]
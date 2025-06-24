from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views
from core import views as core_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),  
    path('accounts/', include('accounts.urls')),
]

# Serve media files (like avatars) in development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

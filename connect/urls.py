from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from user.views import profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('chat.urls')),
    path('profile/', include('user.urls')),
    path('@<username>/', profile_view, name='profile')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

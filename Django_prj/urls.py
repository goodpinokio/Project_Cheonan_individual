from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('blog/',include('blog.urls')),
    path('accounts/', include('allauth.urls')),
    path('',include('single_pages.urls')),
    path('practice/',include('practice.urls')),
    path('forcast/',include('forcast.urls')),
    path('baemin/',include('baemin.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)